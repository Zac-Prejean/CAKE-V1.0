import os  
import re  
import io  
import qrcode  
import datetime  
import tempfile  
from PIL import Image  
from PIL import Image as PILImage  
from reportlab.pdfgen import canvas  
from reportlab.pdfbase import pdfmetrics  
from reportlab.lib.pagesizes import letter  
from reportlab.lib.utils import simpleSplit  
from reportlab.lib.utils import ImageReader  
from reportlab.pdfbase.ttfonts import TTFont  
from wand.image import Image as WandImage  
from PyPDF2 import PdfReader, PdfWriter  

# install ghostscript and ImageMagick
# https://ghostscript.com/releases/gsdnld.html
# https://imagemagick.org/script/download.php#windows
  
script_dir = os.path.dirname(os.path.abspath(__file__))  
  
# barcode  
IDAutomationHC39M_font_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'fonts', 'IDAutomationHC39M.ttf')  
pdfmetrics.registerFont(TTFont("IDAutomationHC39M", IDAutomationHC39M_font_path))  
  
# montserrat  
Montserrat_font_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'fonts', 'Montserrat.ttf')  
pdfmetrics.registerFont(TTFont("Montserrat-Regular", Montserrat_font_path))  
  
  
def create_png_path(folder_name, order_number, index):  
    png_name = f"{order_number}{index}.png"  
    png_path = os.path.join(folder_name, png_name)  
    return png_path  
  
  
def apply_logic(c, row, order_skus, order_quantities, custom_field_3, item_qty, clabel_item_name, index, item_list_description, ):  
    # EXPEDITED white square  
    order_number = str(row['Order - Number']).strip('"')  
    expedited_order = order_number[-1].upper() == 'R' or 'EXP' in order_number.upper()  
    if not expedited_order:  
        # Remove the white square if the order is a redo or expedited  
        EX_x = 211  
        EX_y = 397  
        EX_square_size = 27  
        c.setFillColorRGB(1, 1, 1)  
        c.setStrokeColorRGB(1, 1, 1)  
        c.rect(EX_x, EX_y, EX_square_size, EX_square_size, fill=1)  
  
    # MULTI LINE white square  
    order_number = str(row['Order - Number'])  
    order_skus_for_order_number = order_skus[order_number]  
    # Check if the order has different SKUs  
    different_skus = False  
    first_sku = next(iter(order_skus_for_order_number))  
    for sku in order_skus_for_order_number:  
        if sku != first_sku:  
            different_skus = True  
            break  
  
    if not different_skus:  
        # Remove the white square if different SKUs are found  
        ML_x = 241  
        ML_y = 397  
        ML_square_size = 27  
        c.setFillColorRGB(1, 1, 1)  
        c.setStrokeColorRGB(1, 1, 1)  
        c.rect(ML_x, ML_y, ML_square_size, ML_square_size, fill=1)  
    else:  
        pass  
  
    # MULTI ORDER white square  
    order_total_qty = order_quantities.get(order_number, 0)  
    multi_order = order_total_qty > 1  
  
    if not multi_order:  
        # Remove the white square if more then one orders are found  
        MO_x = 211  
        MO_y = 367  
        MO_square_size = 27  
        c.setFillColorRGB(1, 1, 1)  
        c.setStrokeColorRGB(1, 1, 1)  
        c.rect(MO_x, MO_y, MO_square_size, MO_square_size, fill=1)  
  
    # DUPLICATE ORDER white square  
    duplicate_order = item_qty > 1  
  
    if not duplicate_order:  
        # Remove the white square if more than one quantity  
        DO_x = 241  
        DO_y = 367  
        DO_square_size = 27  
        c.setFillColorRGB(1, 1, 1)  
        c.setStrokeColorRGB(1, 1, 1)  
        c.rect(DO_x, DO_y, DO_square_size, DO_square_size, fill=1)  
  
    processed_font_color = (0, 0, 0)  # font color  
  
    # Get the current date and format it  
    current_date = datetime.datetime.now().strftime("%m%d%Y")  
    # Set font, font size, and font color for the date  
    font_size_date = 8  
    c.setFont("Montserrat-Regular", font_size_date)  
    c.setFillColorRGB(*processed_font_color)  
    # Draw the date  
    c.drawString(210, 340, current_date)  
  
    # Draw the custom field 3  
    font_size_custom_field = 8  
    c.setFont("Montserrat-Regular", font_size_custom_field)  
    c.setFillColorRGB(*processed_font_color)  
    c.drawString(20, 340, str(custom_field_3))  
  
    # Draw the quantity  
    font_size_qty = 8  
    c.setFont("Montserrat-Regular", font_size_qty)  
    c.setFillColorRGB(*processed_font_color)  
    c.drawString(20, 137, str(item_qty) + " of " + str(order_total_qty))  
  
    # Draw the item name  
    font_size_item_name = 8  
    c.setFont("Montserrat-Regular", font_size_item_name)  
    c.setFillColorRGB(*processed_font_color)  
    # Define a bounding box for the item name  
    bounding_box_width = 200  
    # Wrap the item name text  
    if re.match(r"CLABEL[A-Z0-9]*", sku):  
        wrapped_item_name = simpleSplit(clabel_item_name, "Montserrat-Regular", font_size_item_name, bounding_box_width)  
    else:  
        wrapped_item_name = simpleSplit(item_list_description, "Montserrat-Regular", font_size_item_name, bounding_box_width)  
    # Draw the wrapped item name
    text_object = c.beginText(50, 137)  
    for line in wrapped_item_name:  
        text_object.textLine(line)  
    c.drawText(text_object)  
  
    # Draw the order number  
    order_number = "*" + str(row['Order - Number']).strip('"') + "*"  
    font_size_order_number = 13  # font size  
    c.setFillColorRGB(*processed_font_color)  
    c.setFont("IDAutomationHC39M", font_size_order_number)  
    page_width = letter[0]  
    text_width = c.stringWidth('*' + order_number + '*', "IDAutomationHC39M", font_size_order_number)  
    # Calculate the x-coordinate to center the text  
    x_coordinate = ((page_width - text_width) // 2) - 150  # shift amount  
    # index_x_coordinate = ((page_width - text_width) // 2) - 155  
    c.drawString(x_coordinate, 15, order_number)  # (x, y)  
  
    # QR code  
    combined_order_number = str(row['Order - Number']).strip('"') + str(index)  
    qr = qrcode.QRCode(  
        version=1,  
        error_correction=qrcode.constants.ERROR_CORRECT_L,  
        box_size=3,  
        border=4.5,  
    )  
    qr.add_data(combined_order_number)  
    qr.make(fit=True)  
  
    # Create QR code image  
    qr_img = qr.make_image(fill_color="black", back_color="white")  
    # Calculate the new size of the image while maintaining its aspect ratio  
    img_width, img_height = qr_img.size  
    padding_to_remove = 10  
    crop_box = (padding_to_remove, padding_to_remove, img_width - padding_to_remove, img_height - padding_to_remove)  
    qr_img = qr_img.crop(crop_box)  
  
    # Draw the resized image on the canvas at the specified coordinates  
    c.drawImage(ImageReader(qr_img), 21.5, 370, 50, 50)  # (x, y)  
  
    return c

def add_order_number_to_clabel_pdf(sku, row, folder_name, index, custom_field_3, item_qty, clabel_item_name, item_list_description, file_path, order_number, order_quantities, order_skus, process_clabel):   
    if (re.match(r"CLABEL[A-Z0-9]*", sku) or order_number.startswith('C')) and process_clabel:   
  
        # Add the background PDF  
        background_image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'clabel', 'blank_clabel.pdf')  
  
        with open(background_image_path, 'rb') as background_file:  
            # Read the background PDF  
            background_pdf = PdfReader(background_file)  
            background_page = background_pdf.pages[0]  
  
            # Create a new PDF canvas  
            packet = io.BytesIO()  
            c = canvas.Canvas(packet, pagesize=letter)  
  
            # Check the file extension  
            file_extension = os.path.splitext(file_path)[-1].lower()  
  



            if file_extension == '.png':  
                # Open the PNG image using Pillow and convert it to RGBA mode  
                img = Image.open(file_path).convert("RGBA")  
            
                # Calculate the aspect ratio of the original image  
                img_width, img_height = img.size  
                aspect_ratio = float(img_width) / float(img_height)  
            
                # Determine the new height and width while preserving the aspect ratio  
                new_width = min(img_width, 145)  # bounding box width  
                new_height = int(new_width / aspect_ratio)  
            
                if new_height > 145:  # bounding box height  
                    new_height = 145  
                    new_width = int(new_height * aspect_ratio)  
            
                # Resize the image  
                img = img.resize((new_width, new_height), Image.LANCZOS)  
            
                # Convert the RGBA image to an RGB image with a white background  
                img_rgb = Image.new("RGB", img.size, (255, 255, 255))  
                img_rgb.paste(img, mask=img.split()[3])  # Use the alpha channel as the mask  
            
                # Draw the resized image on the canvas at the specified coordinates  
                c.drawImage(ImageReader(img_rgb), 70, 181, new_width, new_height) 

                # Save the canvas as a PDF 
                c = apply_logic(c, row, order_skus, order_quantities, custom_field_3, item_qty, clabel_item_name, index, item_list_description)
                c.save()  
        
                # Move the packet's file pointer to the start    
                packet.seek(0)    
        
                # Read the generated PDF data    
                generated_pdf = PdfReader(packet)    
        
                # Merge the generated PDF with the background PDF    
                background_page.merge_page(generated_pdf.pages[0])    
    
                # Create an output PDF and add the merged page    
                output_pdf = PdfWriter()    
                output_pdf.add_page(background_page)    
        
                # Save the output PDF    
                sku_without_clabel = sku.replace("CLABEL", "")  
                image_name = f"LB{order_number.replace('*', '')}_{sku_without_clabel}_{index}.pdf"  
    
                image_path = os.path.join(folder_name, image_name)    
                with open(image_path, 'wb') as output_file:    
                    output_pdf.write(output_file)

            if file_extension == '.pdf':  
                # Open the PDFs  
                with WandImage(filename=file_path, resolution=300) as img:  
                    overlay_image = img.convert('png')  
            
                    # Calculate the aspect ratio and determine the new dimensions within the bounding box  
                    fetched_width, fetched_height = img.size  
                    aspect_ratio = float(fetched_width) / float(fetched_height)  
            
                new_width = min(fetched_width, 145)  # bounding box width  
                new_height = int(new_width / aspect_ratio)  
            
                if new_height > 145:  # bounding box height  
                    new_height = 145  
                    new_width = int(new_height * aspect_ratio)  
            
                # Convert Wand Image to PIL.Image  
                overlay_image_blob = overlay_image.make_blob('png')  
                overlay_image_pil = PILImage.open(io.BytesIO(overlay_image_blob))  
            
                # Save the PIL.Image to a temporary file  
                temp_image_file = tempfile.NamedTemporaryFile(delete=False, suffix='.png')  
                overlay_image_pil.save(temp_image_file.name)  
            
                # Create a canvas for the resized PDF  
                position_x, position_y = 70, 180  
                c = canvas.Canvas("temp_overlay.pdf", pagesize=letter)  
            
                # Draw the overlaying PDF image on the canvas within the bounding box  
                c.drawImage(temp_image_file.name, position_x, position_y, width=new_width, height=new_height)  
                
                c = apply_logic(c, row, order_skus, order_quantities, custom_field_3, item_qty, clabel_item_name, index, item_list_description)
                c.save()
                  
                # Merge the temporary overlay PDF with the original PDF  
                pdf1_reader = PdfReader(background_image_path)  
                pdf2_reader = PdfReader("temp_overlay.pdf")  
                pdf_writer = PdfWriter()  
            
                # Combine the pages  
                background_page = pdf1_reader.pages[0]  
                overlay_page = pdf2_reader.pages[0]  
                background_page.merge_page(overlay_page)  
                pdf_writer.add_page(background_page)  
            
                # Save the output PDF  
                sku_without_clabel = sku.replace("CLABEL", "")  
                image_name = f"LB{order_number.replace('*', '')}_{sku_without_clabel}_{index}.pdf"  
  
                image_path = os.path.join(folder_name, image_name)  
                with open(image_path, 'wb') as output_file:  
                    pdf_writer.write(output_file)
            
                # Clean up the temporary file  
                overlay_image_pil.close()  
                os.close(temp_image_file.file.fileno())  
                os.remove(temp_image_file.name)  
                os.remove("temp_overlay.pdf")  

def create_label_with_blank_image(sku, row, folder_name, index, custom_field_3, item_qty, clabel_item_name, item_list_description, order_number, order_quantities, order_skus, process_clabel):  
    # Add the background PDF  
    background_image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'clabel', 'blank_clabel.pdf')  

    with open(background_image_path, 'rb') as background_file:  
        # Read the background PDF  
        background_pdf = PdfReader(background_file)  
        background_page = background_pdf.pages[0]  

        # Create a new PDF canvas  
        packet = io.BytesIO()  
        c = canvas.Canvas(packet, pagesize=letter)  

        # Use the specified image when the file path is not set  
        blank_image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'clabel', 'blank_image.png')  
        img = Image.open(blank_image_path).convert("RGBA")  

        # Calculate the aspect ratio of the original image  
        img_width, img_height = img.size  
        aspect_ratio = float(img_width) / float(img_height)  

        # Determine the new height and width while preserving the aspect ratio  
        new_width = min(img_width, 145)  # bounding box width  
        new_height = int(new_width / aspect_ratio)  

        if new_height > 145:  # bounding box height  
            new_height = 145  
            new_width = int(new_height * aspect_ratio)  

        # Resize the image  
        img = img.resize((new_width, new_height), Image.LANCZOS)  

        # Convert the RGBA image to an RGB image with a white background  
        img_rgb = Image.new("RGB", img.size, (255, 255, 255))  
        img_rgb.paste(img, mask=img.split()[3])  # Use the alpha channel as the mask  

        # Draw the resized image on the canvas at the specified coordinates  
        c.drawImage(ImageReader(img_rgb), 70, 181, new_width, new_height)  

        # Save the canvas as a PDF  
        c = apply_logic(c, row, order_skus, order_quantities, custom_field_3, item_qty, clabel_item_name, index, item_list_description)  
        c.save()  

        # Move the packet's file pointer to the start  
        packet.seek(0)  

        # Read the generated PDF data  
        generated_pdf = PdfReader(packet)  

        # Merge the generated PDF with the background PDF  
        background_page.merge_page(generated_pdf.pages[0])  

        # Create an output PDF and add the merged page  
        output_pdf = PdfWriter()  
        output_pdf.add_page(background_page)  

        # Save the output PDF  
        sku_without_clabel = sku.replace("CLABEL", "")  
        image_name = f"{order_number.replace('*', '')}_{sku_without_clabel}_{index}.pdf"  

        image_path = os.path.join(folder_name, image_name)  
        with open(image_path, 'wb') as output_file:  
            output_pdf.write(output_file) 
