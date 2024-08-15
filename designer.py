import os
import json  
from config import *
# from app import app  
from config import get_processed_font_color
from PIL import Image, ImageDraw, ImageFont

os.chdir(os.path.dirname(os.path.abspath(__file__)))

def get_order_quantities(df):  
    order_quantities = {}  
    order_skus = {}  
    for _, row in df.iterrows():  
        order_number = str(row['Order - Number']).strip()  
        item_qty = int(row['Item - Qty'])  
        item_sku = row['Item - SKU']  
        if order_number not in order_quantities:  
            order_quantities[order_number] = 0  
            order_skus[order_number] = set()  
        order_quantities[order_number] += item_qty  
        order_skus[order_number].add(item_sku)  
    return order_quantities, order_skus  

def process_personalization_text(text, clean_sku):      
    lines = [line for line in text.split('\n') if line.strip()]      
    lines = [re.sub(r'(line \d+: ?|name[s]?: ?|title[s]?: ?|top name[s]?: ?|bottom name[s]?: ?|kids name[s]?: ?)', '', line, flags=re.IGNORECASE).strip('\r') for line in lines]      
    lines = [line for line in lines if line.strip()]      
      
    processed_lines = []      
    for line_index, line in enumerate(lines):      
        line = re.sub(r',$', '', line)  # remove comma at the end of the line  
  
        for text, skus in skip_line["line1"].items():      
            if clean_sku in skus:      
                pattern = re.compile(text, flags=re.IGNORECASE)      
                line = pattern.sub('', line).strip()      
      
        for text, skus in skip_line["line2"].items():      
            if clean_sku in skus and line_index == 1:      
                pattern = re.compile(text, flags=re.IGNORECASE)      
                line = pattern.sub('', line).strip() 

        for text, skus in skip_line["line3"].items():        
            if clean_sku in skus and line_index == 2:        
                pattern = re.compile(text, flags=re.IGNORECASE)        
                line = pattern.sub('', line).strip() 

        for text, skus in skip_line["line4"].items():
            if clean_sku in skus and line_index == 3:        
                pattern = re.compile(text, flags=re.IGNORECASE)        
                line = pattern.sub('', line).strip()       

        # special rules
        if lines:  
            processed_line = process_special_rules(clean_sku, line, line_index)            
            processed_lines.append(processed_line)  
        else:  
            print("Error: lines list is empty in process_personalization_text")  
 

    return '\n'.join(processed_lines) 


    
# Load font from the given font path and font size    
def load_font(font_path, font_size):    
    try:    
        font = ImageFont.truetype(font_path, font_size)    
    except OSError:    
        print(f"Error loading font: {font_path}. Using default font.")    
        font = ImageFont.load_default()    
    return font    
    
def get_font_path(clean_sku):    
    font_path = sku_to_font.get(clean_sku, 'arial.ttf')    
    return font_path    

# line placement 
def calculate_font_size_and_placement(sku, text, num_chars, item_options): 

    values = sku_to_fontsize_placement.get(sku, {}).get(num_chars, (200, None, 100))    
      
    if len(values) == 2:      
        font_size, y = values      
        x = None      
    else:      
        font_size, x, y = values      
    print(f"1st Num chars: {num_chars}")      
    return font_size, x, y  

# line 2    
def calculate_second_font_size_and_placement(sku, num_chars, item_options):      

    font_size, x, y = get_font_size_placement_from_sku(sku, num_chars)  
    print(f"2nd Num chars: {num_chars}")
    return font_size, x, y

# line 3  
def calculate_third_font_size_and_placement(sku, num_chars, item_options):     

    values = sku_to_third_fontsize_placement.get(sku, {}).get(num_chars, (200, None, 100))  
      
    if len(values) == 2:  
        font_size, y = values  
        x = None  
    else:  
        font_size, x, y = values  
    print(f"3rd Num chars: {num_chars}")
    return font_size, x, y

# line 4  
def calculate_fourth_font_size_and_placement(sku, num_chars, item_options):        
   
    font_size, x, y = sku_to_fourth_fontsize_placement.get(sku, {}).get(num_chars, (200, None, 100))   
    
    return font_size, x, y  


def get_font_size_placement_from_sku(sku, num_chars):  
    sku_fontsize_placement = sku_to_second_fontsize_placement.get(sku, {})      
    values = sku_fontsize_placement.get(num_chars, (200, None, 100))      
    if len(values) == 2:      
        font_size, y = values      
        x = None      
    else:      
        font_size, x, y = values  
      
    return font_size, x, y   
    
# white background for RNG   
def draw_white_background(draw, x, y, text_width, text_height, margin_left= 0, margin_right=-70,):  
    draw.rectangle([x + margin_left, y, x + text_width + margin_right, y + text_height], fill=(255, 255, 255))   
  
# Process each row from the dataframe    
def process_row(index, row, folder_name, sku, clean_sku, qty_index, load_font, order_quantities, order_skus, process_label, process_pick, order_item_count, process_image):  
    print('')  
    print(f"Processing row: {index}, clean_sku: {clean_sku}")  
    sku = row['Item - SKU']  
    order_number = str(row['Order - Number']).strip('"')  
    order_total_qty = order_quantities[order_number]  # Already passed, ensure it's used correctly  
    txt_output_folder = os.path.join('\\\\sharedrive', 'Batch.txt', 'status')  
    item_options = str(row['Item - Options'])  
    item_qty = int(row['Item - Qty'])  
    custom_field_3 = row['Custom - Field 3']  
  
    if process_label:  
        customtagID = generate_custom_id_tag()  # Generate customtagID for each item within the order  
        get_order_images(order_number, item_qty, item_options, customtagID)  
        create_txt_file(order_number, item_options, sku, index, order_total_qty, txt_output_folder, custom_field_3, customtagID)  
        create_labels(index, row, folder_name, sku, clean_sku, order_quantities, order_skus, process_label, order_item_count, order_total_qty, txt_output_folder, customtagID)
        
  
    # Image processing code  
    clean_sku_match = re.search(r"(?:DSWCLR001)?UVP[A-Z0-9]+|JMUG11WB[A-Z0-9]+", sku)  
    if not clean_sku_match:  
        clean_sku_match = re.search(r"CLABEL[A-Z0-9]*", sku)  
    if not clean_sku_match:  
        clean_sku_match = re.search(r"GLS[A-Z0-9]+", sku)  
    if not clean_sku_match:  
        return  
  
    clean_sku = clean_sku_match.group(0)  
    background_image_path = sku_to_image.get(clean_sku)  
    font_path = get_font_path(clean_sku)  
  
    # skus without personalization_text  
    personalization_text = row['Item - Options']  
    if not personalization_text or not str(personalization_text).strip() or str(personalization_text).lower() == "nan":  
        is_saved, image_path = save_image_without_options(sku, clean_sku, order_number, index, qty_index, background_image_path, folder_name, row, load_font, item_qty, order_quantities, order_skus)  
        if is_saved:  
            image = Image.open(image_path)  
            draw = ImageDraw.Draw(image)  
            add_order_indicators(draw, sku, row, item_qty, order_quantities, order_skus)  
            image.save(image_path)  
        else:  
            print(f"Error saving {sku}")  
        return  
  
    if save_blank_image(row, sku, clean_sku, sku_to_font, order_number, index, background_image_path, folder_name, load_font):  
        return  
  
    inscriptions_match = re.findall(r'(?:Left|Right) Inscription:\s*([\s\S]+?)(?:,|$)', str(item_options))  
    if inscriptions_match:  
        personalization_text = '\n'.join(inscriptions_match).strip()  
    else:  
        match = re.search(r'(?:Personalization|Custom Name|Personalization Text Box):([\s\S]+)', str(item_options))  
        if match:  
            personalization_text = match.group(1)  
        else:  
            personalization_text = ''  
  
    lines = [line for line in personalization_text.split('\n') if line.strip()]  
    lines = [re.sub(r'Line \d+: ?', '', line).strip('\r') for line in lines]  
    lines = [line.strip() for line in lines if line.strip()]  
  
    if not lines:  
        return  
    else:  
        num_chars_line1 = len(lines[0])  
        # check to skip the text specified in the skip_line dictionary  
        skip_text = skip_line.get("skip_line1_text", {}).get(clean_sku)  
        if skip_text and len(lines) > 0 and lines[0] == skip_text:  
            lines.pop(0)  
            print(f"First line removed: {lines}")  
  
    # special rules to split sku for different design options  
    design_option_match = re.search(r'Design Options:\s*([\w\s-]+)', str(row['Item - Options']))  
    if design_option_match:  
        design_option = design_option_match.group(1).upper().replace(" ", "_")  
        if clean_sku in ('UVPPSBASTUVP', 'UVPPSCFDNPUVP'):  
            background_image_path = sku_to_image.get(f'{clean_sku}-{design_option}')  
  
    # special rules to personalization text and font color  
    processed_text = process_personalization_text(personalization_text, clean_sku)  
    lines = [line for line in processed_text.split('\n') if line.strip()]  
    num_chars_line1 = len(lines[0])  
  
    font_size_line1, x_line1, y_line1 = calculate_font_size_and_placement(clean_sku, lines[0], num_chars_line1, item_options)  
    if len(lines) > 1:  
        num_chars_line2 = len(lines[1])  
        font_size_line2, x_line2, y_line2 = calculate_second_font_size_and_placement(clean_sku, num_chars_line2, item_options)  
    else:  
        font_size_line2, x_line2, y_line2 = None, None, None  
    if len(lines) > 2:  
        num_chars_line3 = len(lines[2])  
        font_size_line3, x_line3, y_line3 = calculate_third_font_size_and_placement(clean_sku, num_chars_line3, item_options)  
    if len(lines) > 3:  
        num_chars_line4 = len(lines[3])  
        font_size_line4, x_line4, y_line4 = calculate_fourth_font_size_and_placement(clean_sku, num_chars_line4, item_options)  
  
    # create image with personalized text  
    image = Image.open(background_image_path) if background_image_path else Image.new('RGB', (3250, 1750), color='white')  
    draw = ImageDraw.Draw(image)  
    image_width, _ = image.size  
  
    # hard set the font color  
    font_color = get_processed_font_color(clean_sku, item_options, color_name_to_rgb, get_font_color_for_dswclr001, process_font_color)  
    # draw each line separately  
    for i, line in enumerate(lines):  
        # load the font for the current line  
        font_path = sku_to_second_line_font.get(clean_sku, font_path) if i == 1 else get_font_path(clean_sku)  
        # font_path = sku_to_third_line_font.get(clean_sku, font_path) if i == 2 else get_font_path(clean_sku)  
        font_size = font_size_line1  
        if i == 1:  
            font_size = font_size_line2  
        elif i == 2:  
            font_size = font_size_line3  
        elif i == 3:  
            font_size = font_size_line4  
        font = load_font(font_path, font_size)  
  
        text_y = y_line1  
        if i == 1:  
            text_y = y_line2  
        elif i == 2:  
            text_y = y_line3  
        elif i == 3:  
            text_y = y_line4  
  
        # center the text if x-coordinate is not provided  
        if i == 1 and x_line2 is not None:  
            text_x = x_line2  
        elif x_line1 is not None:  
            text_x = x_line1  
        else:  
            left, _, right, _ = font.getbbox(line)  
            text_width = right - left  
            text_x = (image_width - text_width) // 2  
  
        # draw the current line  
        draw.text((text_x, text_y), line, fill=process_font_color(font_color, clean_sku, i), font=font)  
  
    # flip the image horizontally and add barcode  
    image, draw = flip_mug_image(image, sku)  
    add_order_number_to_jmug(draw, sku, row, load_font)  
    # add indicators  
    if sku.startswith("JMUG11WB"):  
        add_order_indicators(draw, sku, row, item_qty, order_quantities, order_skus)  
    # name the saved png  
    image_result = save_image_with_subfolders(clean_sku, sku, order_number, index, qty_index, item_options, folder_name, image)  
    if image_result is not None:  
        image_path, image_name = image_result  


script_dir = os.path.dirname(os.path.abspath(__file__))  
background_pdf_path = os.path.join(script_dir, 'background', 'clabel', 'pick_list.pdf')  

# export images from the given dataframe    
def export_images(df, full_folder_path, process_image, process_label, process_pick):  
    if df.empty:  
        return {"error": "Please load a CSV file first."}  
  
    try:  
        order_quantities, order_skus = get_order_quantities(df)  
        order_data = [['Order - Number', 'Item - Qty', 'Item - SKU', 'Item - Options', 'Item - Name', 'Custom - Field 3']]  
        order_item_counts = {}  
  
        for index, row in df.iterrows():  
            if pd.isna(row['Item - SKU']):  
                continue  
            clean_sku = row['Item - SKU'].strip()  
            item_qty = int(row['Item - Qty'])  
            order_number = str(row['Order - Number']).strip('"')  
            if order_number not in order_item_counts:  
                order_item_counts[order_number] = 0  
            order_item_counts[order_number] += 1  
  
            order_total_qty = order_quantities[order_number]  # Get the total quantity for the current order  
  
            for qty_index in range(item_qty):  
                sku = row['Item - SKU'].strip()  
                process_row(index, row, full_folder_path, sku, clean_sku, qty_index, load_font, order_quantities, order_skus, process_label, process_pick, order_item_count=order_item_counts[order_number], process_image=process_image)  
  
            txt_output_folder = os.path.join('\\\\sharedrive', 'Batch.txt', 'status')  
            custom_field_3 = row['Custom - Field 3']  
            if not custom_field_3 or str(custom_field_3).strip().lower() == "nan":  
                custom_field_3 = "DefaultStatus"  
  
            order_data.append([  
                row['Order - Number'],  
                row['Item - Qty'],  
                row['Item - SKU'],  
                row['Item - Options'],  
                row['Item - Name'],  
                row['Custom - Field 3']  
            ])  
  
        if process_pick:  
            create_pick_list_pdf(order_data, background_pdf_path, match_sku_to_item_description, process_pick)  
        print('')  
        print(f"Process complete. Images exported to {full_folder_path}.")  
        print('===================')  
        return {"success": True}  
    except Exception as e:  
        print(f"An error occurred: {e}")  
        return {"error": str(e)}  

    