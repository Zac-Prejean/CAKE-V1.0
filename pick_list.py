import os  
import io  
import sys  
import json  
import qrcode  
import PyPDF2  
import tempfile  
import datetime  
from copy import copy   
from pathlib import Path   
from reportlab.pdfgen import canvas   
from reportlab.pdfbase import pdfmetrics  
from reportlab.lib.utils import ImageReader  
from reportlab.pdfbase.ttfonts import TTFont     
from reportlab.lib.pagesizes import letter   
    
# montserrat    
Montserrat_font_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'fonts', 'Montserrat.ttf')    
pdfmetrics.registerFont(TTFont("Montserrat-Regular", Montserrat_font_path))    
current_date = datetime.datetime.now().strftime('%m.%d.%Y %H:%M')

def match_sku_to_item_description(sku):  
    if getattr(sys, 'frozen', False):  
        bundle_dir = sys._MEIPASS  
    else:  
        bundle_dir = os.path.dirname(os.path.abspath(__file__))  
  
    json_path = Path(bundle_dir)  
    sku_path = json_path / "sku_to_item_description.json"  
    dtg_path = json_path / "dtg_item_description.json"  
  
    # Load SKU to item description mapping from JSON file  
    with sku_path.open() as f:  
        sku_to_item_description = json.load(f)  
  
    # Load DTG to item description mapping from JSON file  
    with dtg_path.open() as f:  
        dtg_to_item_description = json.load(f)  
  
    # Search for SKU in sku_to_item_description  
    for key in sku_to_item_description:  
        if sku.startswith(key):  
            return sku_to_item_description[key]  
  
    # Search for SKU in dtg_to_item_description  
    for key in dtg_to_item_description:  
        if sku.startswith(key):  
            return dtg_to_item_description[key]  
  
    return "Description not found"  

def count_skus(order_data):      
    sku_counts = {}      
    for row in order_data[1:]:      
        sku = row[2]      
        qty = int(row[1])   
    
        # Remove "UVP" and everything after it from the SKU name    
        sku_without_uvp = sku.split("UVP")[0]    
    
        if sku_without_uvp not in sku_counts:      
            sku_counts[sku_without_uvp] = 0      
        sku_counts[sku_without_uvp] += qty   
    return sku_counts    
     
def wrap_text(text, max_width, canvas, font, font_size):    
    text_lines = []    
    current_line = []    
    words = text.split(" ")    
    for word in words:    
        current_line.append(word)    
        line_width = canvas.stringWidth(" ".join(current_line), font, font_size)    
        if line_width > max_width:    
            current_line.pop()  # Remove the last word    
            text_lines.append(" ".join(current_line))    
            current_line = [word]  # Start a new line with the last word    
    text_lines.append(" ".join(current_line))    
    return text_lines 
 
def draw_page_number(c, page_number, total_pages, x, y):  
    c.setFont("Montserrat-Regular", 10)  
    c.setFillColorRGB(0, 0, 0)  
    c.drawString(x, y, f"Page {page_number} of {total_pages}")

def draw_date_and_custom_field_3(c, current_date, custom_field_3):   
    # Set font, font size, and font color for the date        
    font_size_date = 15        
    c.setFont("Montserrat-Regular", font_size_date)        
    c.setFillColorRGB(0, 0, 0)        
    # Draw the date        
    c.drawString(215, 761, current_date)        
  
    # Draw the custom field 3       
    font_size_custom_field = 15        
    c.setFont("Montserrat-Regular", font_size_custom_field)        
    c.setFillColorRGB(0, 0, 0)        
    c.drawString(215, 740, str(custom_field_3))  

def draw_qr_code(c, custom_field_3, x, y, width, height):    
    qr = qrcode.QRCode(    
        version=1,    
        error_correction=qrcode.constants.ERROR_CORRECT_L,    
        box_size=2,    
        border=0,    
    )    
    qr.add_data(str(current_date))  # Use custom_field_3 value for the QR code    
    qr.make(fit=True)    
  
    # Create QR code image    
    qr_img = qr.make_image(fill_color="black", back_color="white")    
  
    # Save the QR code image to a temporary file    
    temp_qr_file = tempfile.NamedTemporaryFile(delete=False, suffix='.png')    
    qr_img.save(temp_qr_file.name)    
  
    # Draw the resized image on the canvas at the specified coordinates    
    c.drawImage(ImageReader(temp_qr_file.name), x, y, width, height)    
  
    # Close and remove the temporary QR code file    
    temp_qr_file.close()    
    os.remove(temp_qr_file.name)

def draw_sku_qr_code(c, sku, x, y, width, height):    
    qr = qrcode.QRCode(    
        version=1,    
        error_correction=qrcode.constants.ERROR_CORRECT_L,    
        box_size=2,    
        border=0,    
    )    
    # remove prefix from the SKU name  
    sku_without_prefix = sku.replace("CLABEL", "").replace("BLABEL", "")  
    qr.add_data(sku_without_prefix)  # Use SKU value without "CLABEL" and "BLABEL" for the QR code  
    qr.make(fit=True)  

    
    # Create QR code image    
    qr_img = qr.make_image(fill_color="black", back_color="white")    
    
    # Save the QR code image to a temporary file    
    temp_qr_file = tempfile.NamedTemporaryFile(delete=False, suffix='.png')    
    qr_img.save(temp_qr_file.name)    
    
    # Draw the resized image on the canvas at the specified coordinates    
    c.drawImage(ImageReader(temp_qr_file.name), x, y, width, height)    
    
    # Close and remove the temporary QR code file    
    temp_qr_file.close()    
    os.remove(temp_qr_file.name)  

def custom_sku_sort_key(sku_count):  
    sku, _ = sku_count  
    if "2616" in sku:  
        return "00" + sku 
    elif "3001" in sku:  
        return "01" + sku
    elif "3321" in sku:  
        return "02" + sku  
    elif "3322" in sku:  
        return "03" + sku
    elif "3739" in sku:  
        return "04" + sku  
    elif "3804" in sku:  
        return "05" + sku 
    elif "4424" in sku:  
        return "06" + sku
    elif "5280" in sku:  
        return "07" + sku
    elif "6004" in sku:  
        return "08" + sku
    elif "6005" in sku:  
        return "09" + sku
    elif "8800" in sku:  
        return "10" + sku 
    elif "F170" in sku:  
        return "11" + sku
    elif "F260" in sku:  
        return "12" + sku  
    elif "G185B" in sku:  
        return "13" + sku
    elif "G500B" in sku:  
        return "14" + sku  
    elif "G500L" in sku:  
        return "15" + sku 
    elif "G500VL" in sku:  
        return "16" + sku
    elif "G570" in sku:  
        return "17" + sku
    elif "G2400" in sku:  
        return "18" + sku
    elif "G5000" in sku:  
        return "19" + sku
    return sku

def draw_all_skus(c, current_date, custom_field_3, sku_counts, font_size_sku, start_x, start_y):   
    
    qr_code_grid_coordinates = [  
        (248, 636), (502, 636),  
        (248, 546), (502, 546),  
        (248, 456), (502, 456),  
        (248, 366), (502, 366),  
        (248, 276), (502, 276),  
        (248, 186), (502, 186),  
        (248, 96), (502, 96),  
    ]
    sku_name_grid_coordinates = [  
        (65, 685), (310, 685),  
        (65, 595), (310, 595),  
        (65, 505), (310, 505),  
        (65, 415), (310, 415),  
        (65, 325), (310, 325),  
        (65, 235), (310, 235),  
        (65, 145), (310, 145),  
    ]  
  
    sorted_skus = sorted(sku_counts.items(), key=custom_sku_sort_key)
  
    idx = 0  
    page_number = 1  
    total_pages = 1 + (len(sorted_skus) - 1) // len(sku_name_grid_coordinates)  
      
    # Draw page number on the first page  
    draw_page_number(c, page_number, total_pages, 500, 50) 
  
    for sku, count in sorted_skus:  
        if idx >= len(sku_name_grid_coordinates):  
            c.showPage()  
            idx = 0  
            page_number += 1  
            draw_page_number(c, page_number, total_pages, 500, 50)  
            draw_date_and_custom_field_3(c, current_date, custom_field_3)  
            draw_qr_code(c, custom_field_3, 483, 730, 60, 60)  
  
        x, y = sku_name_grid_coordinates[idx]  
  
        # Remove "CLABEL" and "BLABEL" prefixes from the SKU name  
        sku_without_prefix = sku.replace("CLABEL", "").replace("BLABEL", "")  
  
        # Remove "UVP" and "Exp" from the SKU name  
        sku_without_uvp = sku_without_prefix.split("UVP")[0]   
        sku_without_exp = sku_without_uvp.split("-EXP")[0]  
  
        # Draw the modified SKU name without the prefixes and the "UVP" part  
        c.setFont("Montserrat-Regular", font_size_sku)  
        c.setFillColorRGB(0, 0, 0)  
        c.drawString(x, y, f"{count}x {sku_without_uvp}") 
        # c.drawString(x, y, f"{count}x {sku_without_exp}")  

  
        # Draw the QR code for the current SKU next to its description using the QR code grid  
        qr_code_x, qr_code_y = qr_code_grid_coordinates[idx]  
        qr_code_width = 40  
        qr_code_height = 40  
        draw_sku_qr_code(c, sku, qr_code_x, qr_code_y, qr_code_width, qr_code_height)  
        
        sku_description = match_sku_to_item_description(sku)  
  
        # Set the font size for the item description  
        font_size_description = 9  
  
        # Wrap the item description text with the new font size  
        wrapped_sku_description = wrap_text(str(sku_description), 175, c, "Montserrat-Regular", font_size_description)  
  
        x_desc, y_desc = sku_name_grid_coordinates[idx]  
        y_desc -= 15  
  
        # Draw the item description with the new font size  
        c.setFont("Montserrat-Regular", font_size_description)  
        for line in wrapped_sku_description:  
            c.drawString(x_desc, y_desc, line)  
            y_desc -= 15  
  
        # Reset the font size back to font_size_sku for the next iteration  
        c.setFont("Montserrat-Regular", font_size_sku)  
  
        idx += 1  
  
def create_pick_list_pdf(order_data, background_pdf_path, match_sku_to_item_description, process_pick):        
    packet = io.BytesIO()
    sku_counts = {}  
    c = canvas.Canvas(packet, pagesize=letter)        
    temp_pdf = 'temp_pick_list.pdf'        
    custom_field_3 = order_data[1][5]  
    final_pdf = os.path.join(output_folder_path, f'{custom_field_3}_pick_list.pdf')
  
  
    # Get the current date and format it   
    def draw_date_and_custom_field_3(c, date, custom_field_3):   
               
        # Set font, font size, and font color for the date        
        font_size_date = 15        
        c.setFont("Montserrat-Regular", font_size_date)        
        c.setFillColorRGB(0, 0, 0)        
        # Draw the date        
        c.drawString(215, 761, current_date)        
  
        # Draw the custom field 3       
        font_size_custom_field = 15        
        c.setFont("Montserrat-Regular", font_size_custom_field)        
        c.setFillColorRGB(0, 0, 0)        
        c.drawString(215, 740, str(custom_field_3))  
  
    # Draw the date and custom field 3 for the first page    
    draw_date_and_custom_field_3(c, current_date, custom_field_3)  
    
    # Draw QR code function    
    def draw_qr_code(c, custom_field_3, x, y, width, height):    
        qr = qrcode.QRCode(    
            version=1,    
            error_correction=qrcode.constants.ERROR_CORRECT_L,    
            box_size=2,    
            border=0,    
        )    
        qr.add_data(str(current_date))  # Use custom_field_3 value for the QR code    
        qr.make(fit=True)    
    
        # Create QR code image    
        qr_img = qr.make_image(fill_color="black", back_color="white")    
    
        # Save the QR code image to a temporary file    
        temp_qr_file = tempfile.NamedTemporaryFile(delete=False, suffix='.png')    
        qr_img.save(temp_qr_file.name)    
    
        # Draw the resized image on the canvas at the specified coordinates    
        c.drawImage(ImageReader(temp_qr_file.name), x, y, width, height)    
    
        # Close and remove the temporary QR code file    
        temp_qr_file.close()    
        os.remove(temp_qr_file.name)   
  
    # Draw the QR code for the first page    
    draw_qr_code(c, custom_field_3, 483, 730, 60, 60)  # (x, y, width, height)   
        
    # Count the SKUs    
    sku_counts = count_skus(order_data)    
    
    font_size_sku = 12  
    c.setFont("Montserrat-Regular", font_size_sku)    
    c.setFillColorRGB(0, 0, 0)    
    
    start_x = 50
    start_y = 700

    # Draw all the SKUs on the pick list PDF without leaving any out  
    draw_all_skus(c, current_date, custom_field_3, sku_counts, font_size_sku, start_x, start_y)
  
    # Save the canvas to 'temp_pick_list.pdf'    
    c.save()        
        
    packet.seek(0)        
    with open(temp_pdf, 'wb') as temp_file:        
        temp_file.write(packet.getbuffer())        
        
    # Merge the background PDF with the temp_pick_list.pdf    
    with open(background_pdf_path, 'rb') as background_file, open(temp_pdf, 'rb') as content_file:    
        background_pdf = PyPDF2.PdfReader(background_file)    
        content_pdf = PyPDF2.PdfReader(content_file)    
        pdf_writer = PyPDF2.PdfWriter()    
    
        # Merge all pages with the background    
        for page_number in range(len(content_pdf.pages)):    
            content_page = content_pdf.pages[page_number]    
            background_page = copy(background_pdf.pages[0])  
            background_page.merge_page(content_page)    
            pdf_writer.add_page(background_page)    
    
        with open(final_pdf, 'wb') as output_file:    
            pdf_writer.write(output_file)    
    
    os.remove(temp_pdf) 
    
    print('')    
    print("Pick-List Processed")  
      
def export_images(df, full_folder_path, background_pdf_path, order_data, process_pick):    
    if df.empty:    
        return {"error": "Please load a CSV file first."}    
    
    # Prepare order data for the pick_list.pdf    
    order_data = [['Order - Number', 'Item - Qty', 'Item - SKU', 'Item - Options', 'Item - Name', 'Custom - Field 3']]    
    for _, row in df.iterrows():    
        order_data.append([    
            row['Order - Number'],    
            row['Item - Qty'],    
            row['Item - SKU'],    
            row['Item - Options'],    
            row['Item - Name'],    
            row['Custom - Field 3']    
        ])    
    
    # Create the pick_list.pdf  
    if process_pick:  
        create_pick_list_pdf(order_data, background_pdf_path, match_sku_to_item_description)   
    return {"message": f"PDF exported to {full_folder_path}!"}    

   
output_folder_path = os.path.join(os.path.expanduser('~\\Downloads'))    
script_dir = os.path.dirname(os.path.abspath(__file__))    
background_pdf_path = os.path.join(script_dir, 'background', 'clabel', 'pick_list.pdf') 


