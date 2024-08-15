import os      
import re    
import io 
import qrcode
import datetime
from PIL import Image
from reportlab.pdfgen import canvas
from PyPDF2 import PdfReader, PdfWriter      
from reportlab.pdfbase import pdfmetrics 
from reportlab.lib.pagesizes import letter
from reportlab.lib.utils import simpleSplit 
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase.ttfonts import TTFont

script_dir = os.path.dirname(os.path.abspath(__file__))      
    
# pixel font 
PixelTandy_font_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'fonts', 'Pixel-Tandy.ttf') 
pdfmetrics.registerFont(TTFont("Pixel-Tandy", PixelTandy_font_path))
# Add the get_order_quantities function here  

def create_blabel_path(folder_name, order_number, index, side):    
    png_name = f"{order_number}{index}_{side}.png"    
    png_path = os.path.join(folder_name, png_name)    
    return png_path  
  
sku_indices = {} 

def add_order_number_to_blabel_pdf(sku, row, folder_name, blabel_item_name, index, item_qty, order_quantities, order_skus, order_item_count, customtagID, front_png_exists, back_png_exists):      

    # Draw a QR code image on the canvas 
    def process_qr_image(qr_img, x, y, new_width, new_height, aspect_ratio=None):      
        img_width, img_height = qr_img.size      
        padding_to_remove = 10      
        crop_box = (padding_to_remove, padding_to_remove, img_width - padding_to_remove, img_height - padding_to_remove)      
        qr_img = qr_img.crop(crop_box)      
        img_width, img_height = qr_img.size  
        
        if not aspect_ratio:  
            aspect_ratio = float(img_width) / float(img_height)  
        
        qr_img = qr_img.resize((new_width, new_height), Image.LANCZOS)      
        c.drawImage(ImageReader(qr_img), x, y, new_width, new_height)  

    
    if re.match(r"BLABEL[A-Z0-9]*", sku):    
    
        # Add the background PDF    
        background_image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'clabel', 'blank_2X2.pdf')    
    
        with open(background_image_path, 'rb') as background_file:    
            # Read the background PDF    
            background_pdf = PdfReader(background_file)    
            background_page = background_pdf.pages[0]    
    
            # Create a new PDF canvas    
            packet = io.BytesIO()    
            c = canvas.Canvas(packet, pagesize=letter)

            # FRONT white square   
            if not front_png_exists:  
                # Remove the white square if the front PNG exists  
                EX_x = 100      
                EX_y = 24      
                EX_rectangle_width = 42    
                EX_rectangle_height = 25   
                c.setFillColorRGB(1, 1, 1)    
                c.setStrokeColorRGB(1, 1, 1)    
                c.rect(EX_x, EX_y, EX_rectangle_width, EX_rectangle_height, fill=1)  

            
            # BACK white square
            if not back_png_exists:  
                # Remove the white square if the front PNG exists  
                EX_x = 100      
                EX_y = 0      
                EX_rectangle_width = 42    
                EX_rectangle_height = 25   
                c.setFillColorRGB(1, 1, 1)    
                c.setStrokeColorRGB(1, 1, 1)    
                c.rect(EX_x, EX_y, EX_rectangle_width, EX_rectangle_height, fill=1) 

            # EXPEDITED white square
            order_number = str(row['Order - Number']).strip('"')
            expedited_order = order_number[-1].upper() == 'R' or 'EXP' in order_number.upper()  
            if not expedited_order:
                # Remove the white square if the order is a redo or expedited
                EX_x = 3    
                EX_y = 46    
                EX_square_size = 25    
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
                ML_x = 31.5     
                ML_y = 46      
                ML_square_size = 25      
                c.setFillColorRGB(1, 1, 1)      
                c.setStrokeColorRGB(1, 1, 1)      
                c.rect(ML_x, ML_y, ML_square_size, ML_square_size, fill=1)  
            else:
                pass  
            
            # MULTI ORDER white square
            order_total_qty = order_quantities.get(order_number, 0)
            multi_order = order_total_qty > 1

            # QR code for bin_design_number 
            # if multi_order:
            bin_design_number = str(row['Item - Options']).strip('"')
            qr_bin = qrcode.QRCode(  
                version=1,  
                error_correction=qrcode.constants.ERROR_CORRECT_L,  
                box_size=3,  
                border=4.5,  
            )  
            qr_bin.add_data(bin_design_number)  
            qr_bin.make(fit=True)  
            qr_img_bin = qr_bin.make_image(fill_color="black", bin_color="white")  
            # Draw the bin QR code   
            process_qr_image(qr_img_bin, 60, 2, 40, 40) # (x, y, width, height)

            if not multi_order:   
                # Remove the white square if more then one orders are found 
                MO_x = 3  
                MO_y = 18  
                MO_square_size = 25  
                c.setFillColorRGB(1, 1, 1)
                c.setStrokeColorRGB(1, 1, 1)
                c.rect(MO_x, MO_y, MO_square_size, MO_square_size, fill=1)

            # DUPLACATE ORDER white square
            duplacate_order = item_qty > 1

            if not duplacate_order:    
                # Remove the white square if more then one quantity
                DO_x = 31.5 
                DO_y = 18 
                DO_square_size = 25  
                c.setFillColorRGB(1, 1, 1)
                c.setStrokeColorRGB(1, 1, 1)
                c.rect(DO_x, DO_y, DO_square_size, DO_square_size, fill=1)
            
            processed_font_color = (0, 0, 0)  # font color  
            
            # Get the current date and format it    
            current_date = datetime.datetime.now().strftime("%m%d%Y")
            due_date = row['Item - Name'].replace(" 4:00:00 PM", "")
            # Set font, font size, and font color for the date    
            font_size_date = 5      
            c.setFont("Pixel-Tandy", font_size_date)      
            c.setFillColorRGB(*processed_font_color)   
            # Draw the date
            # c.drawString(8, 2, current_date)
            c.drawString(8, 2, due_date)
            

            # Draw the quanty  
            font_size_qty = 5  
            c.setFont("Pixel-Tandy", font_size_qty)  
            c.setFillColorRGB(*processed_font_color)

            # Draw the item discription  
            font_size_item_name = 7 
            c.setFont("Pixel-Tandy", font_size_item_name)  
            c.setFillColorRGB(*processed_font_color)  
            # Define a bounding box for the item name  
            bounding_box_width = 75 
            # Wrap the item name text  
            wrapped_item_name = simpleSplit(blabel_item_name, "Pixel-Tandy", font_size_item_name, bounding_box_width)  

            # Draw the wrapped item discription inside the bounding box  
            text_object = c.beginText(65, 130) # (x, y)
            for line in wrapped_item_name:
                text_object.textLine(line + " ")
            
            # Draw the order number  
            order_number = str(row['Order - Number']).strip('"')  
            # Check if the order_number is in the order_quantities dictionary  
            order_total_qty = order_quantities.get(order_number, 0)
            font_size_order_number = 5 # font size
            c.setFillColorRGB(*processed_font_color)    
            c.setFont("Pixel-Tandy", font_size_order_number)
            
            item_options = row["Item - Options"]  
            front_url_match = re.search(r'Art_Location(?:_Front)?:\s*(https://[\w\./?=-]+(?:[\w\./?=&-]+)?)', str(item_options))
            back_url_match = re.search(r'Art_Location(?:_Back)?:\s*(https://[\w\./?=-]+(?:[\w\./?=&-]+)?)', str(item_options))
            
            def generate_order_number_qr(item_options, box_size=3, border=4.5):  
                qr = qrcode.QRCode(        
                    version=1,        
                    error_correction=qrcode.constants.ERROR_CORRECT_L,        
                    box_size=box_size,        
                    border=border,        
                )        
                qr.add_data(customtagID)          
                qr.make(fit=True)        
                qr_order_number_img = qr.make_image(fill_color="black", back_color="white")  
                return qr_order_number_img

            # QR code for order_number
            # qr_order_number_img = generate_order_number_qr(str(row[3]).replace("Art_Location_Front: ", "").replace("Art_Location_Back: ", ""))
            tagID = (str(row[3]).replace("Art_Location_Front: ", "").replace("Art_Location_Back: ", ""))        
            qr_order_number_img = generate_order_number_qr(tagID)  
            # Draw the order number QR code on the canvas with the desired size  
            process_qr_image(qr_order_number_img, 7, 83.5, 52, 52, aspect_ratio=1) # (x, y, width, height)
            
            # Save the current state of the canvas  
            c.saveState() 
            
            #2X2
            c.drawString(8, 10, str(item_qty) + " of " + str(order_total_qty))
            c.drawString(8, 74, customtagID) # (x, y)
            c.drawText(text_object)
            # 1.5X3
            # c.drawString(26, 1, current_date)
            # process_qr_image(qr_img_front, 44, 53.5)
            # process_qr_image(qr_img_back, 44, 8)
            # Rotate the canvas by 270 degrees  
            # c.rotate(270)
            # Calculate the new x and y coordinates  
            # new_x = -letter[1] + 642  
            # new_x_qty = -letter[1] + 645 
            # Draw the rotated text (note the adjusted x and y coordinates)  
            # c.drawString(new_x_qty, 10, str(item_qty) + " of " + str(order_total_qty))
            # Draw the rotated text (note the adjusted x and y coordinates)  
            # c.drawString(new_x, 22, order_number) # (x, y)
            # c.translate(-letter[1] + 650, -20)
            # c.drawText(text_object)

            # Restore the canvas to its original state  
            c.restoreState()

            # Save the canvas as a PDF    
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
            
            # Create a single label for each item  
            sku_without_blabel = row['Item - SKU'].replace("BLABEL", "")  
            image_name = f"{sku_without_blabel}_{customtagID}_{order_number.replace('*', '')}.pdf"  
            image_path = os.path.join(folder_name, image_name)  
            with open(image_path, 'wb') as output_file:  
                output_pdf.write(output_file)  
            print('')    
            print(f"Label: {image_name}")  
             