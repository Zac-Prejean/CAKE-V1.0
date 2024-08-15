import os    
import re    
import io    
import csv
import sys  
import json
import glob
import time
import sched 
import shutil   
import base64
import urllib
import random 
import img2pdf
import requests
import tempfile
import threading 
import subprocess
import pandas as pd
from pathlib import Path 
import process_xlsx_file
from threading import Lock
from datetime import datetime 
from urllib.parse import urlparse
from blabel_config import create_blabel_path
from werkzeug.utils import secure_filename  
from apscheduler.schedulers.background import BackgroundScheduler 
from clabel_config import create_png_path
from reportlab.lib.utils import ImageReader  
from flask import Flask, send_file, jsonify, render_template, request, Response, stream_with_context, redirect, url_for, send_from_directory, session
from PIL import Image, ImageDraw, ImageFont
from reportlab.lib.pagesizes import letter  
from reportlab.pdfgen import canvas 


images_saved_in_subfolder = 0  
current_mug_subfolder = 1 
 
from api_download import (
    create_txt_file, generate_custom_id_tag, process_csv, get_order_images
) 

from batchID import (
     updateStatus, updateAllItemsStatus, getStatus, get_txt_files,
)
from blabel_config import (
    add_order_number_to_blabel_pdf,
)
from clabel_config import (
    add_order_number_to_clabel_pdf, create_label_with_blank_image
)
from create_labels import (
    create_labels,
)
from pick_list import (  
    create_pick_list_pdf, background_pdf_path, export_images, match_sku_to_item_description  
) 
from deskplates_config import (    
    sku_to_image as deskplates_sku_to_image,    
    sku_to_font as deskplates_sku_to_font,    
    sku_to_fontsize_placement as deskplates_sku_to_fontsize_placement,    
    sku_to_second_fontsize_placement as deskplates_sku_to_second_fontsize_placement,    
    sku_to_second_line_font as deskplates_sku_to_second_line_font,    
    get_font_color_for_dswclr001,    
)
from golfballs_config import (    
    sku_to_image as glfbl_sku_to_image,    
    sku_to_font as glfbl_sku_to_font,    
    sku_to_fontsize_placement as glfbl_sku_to_fontsize_placement,
    sku_to_second_fontsize_placement as glfbl_sku_to_second_fontsize_placement,
    sku_to_third_fontsize_placement as glfbl_sku_to_third_fontsize_placement,    
    sku_to_four_fontsize_placement as glfbl_sku_to_four_fontsize_placement, 
)
from mugs_config import (    
    sku_to_image as mug_sku_to_image,    
    sku_to_font as mug_sku_to_font,    
    sku_to_fontsize_placement as mug_sku_to_fontsize_placement,    
    sku_to_second_fontsize_placement as mug_sku_to_second_fontsize_placement,    
    sku_to_second_line_font as mug_sku_to_second_line_font,
    sku_to_third_fontsize_placement as mug_sku_to_third_fontsize_placement,    
    sku_to_third_line_font as mug_sku_to_third_line_font,
    sku_to_four_fontsize_placement as mug_sku_to_four_fontsize_placement, 
    flip_mug_image, add_order_number_to_jmug, add_order_indicators
)
from planks_config import (  
    sku_to_image as planks_sku_to_image,  
    sku_to_font as planks_sku_to_font,  
    sku_to_fontsize_placement as planks_sku_to_fontsize_placement,  
    sku_to_second_fontsize_placement as planks_sku_to_second_fontsize_placement,
    sku_to_third_fontsize_placement as planks_sku_to_third_fontsize_placement,
    sku_to_fourth_fontsize_placement as planks_sku_to_fourth_fontsize_placement,
    sku_to_second_line_font as planks_sku_to_second_line_font,
)   
from tumbler_config import (    
    sku_to_image as tumbler_sku_to_image,    
    sku_to_font as tumbler_sku_to_font,    
    sku_to_fontsize_placement as tumbler_sku_to_fontsize_placement,    
    sku_to_second_fontsize_placement as tumbler_sku_to_second_fontsize_placement,    
    sku_to_second_line_font as tumbler_sku_to_second_line_font,    
    skip_line as tumbler_skip_line,  
)

# Merge dictionaries    
sku_to_image = {**deskplates_sku_to_image, **glfbl_sku_to_image, **mug_sku_to_image, **planks_sku_to_image, **tumbler_sku_to_image}    
sku_to_font = {**deskplates_sku_to_font, **glfbl_sku_to_font, **mug_sku_to_font, **planks_sku_to_font, **tumbler_sku_to_font}    
sku_to_fontsize_placement = {**deskplates_sku_to_fontsize_placement, **glfbl_sku_to_fontsize_placement, **mug_sku_to_fontsize_placement, **planks_sku_to_fontsize_placement, **tumbler_sku_to_fontsize_placement}    
sku_to_second_fontsize_placement = {**deskplates_sku_to_second_fontsize_placement, **glfbl_sku_to_second_fontsize_placement, **mug_sku_to_second_fontsize_placement, **planks_sku_to_second_fontsize_placement, **tumbler_sku_to_second_fontsize_placement}
sku_to_second_line_font = {**deskplates_sku_to_second_line_font, **mug_sku_to_second_line_font, **planks_sku_to_second_line_font, **tumbler_sku_to_second_line_font}
sku_to_third_fontsize_placement = {**glfbl_sku_to_third_fontsize_placement, **mug_sku_to_third_fontsize_placement, **planks_sku_to_third_fontsize_placement} 
sku_to_third_line_font = {**mug_sku_to_third_line_font} 
sku_to_fourth_fontsize_placement = {**glfbl_sku_to_four_fontsize_placement, **planks_sku_to_fourth_fontsize_placement, **mug_sku_to_four_fontsize_placement} 
skip_line = {**tumbler_skip_line}    
  
csv_load_count = 0  

# error skus     
def create_check_csv_image(row, load_font):
    IDAutomationHC39M_font_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'fonts', 'IDAutomationHC39M.ttf')   
    image = Image.new('RGB', (1000, 1000), color='white')  
    draw = ImageDraw.Draw(image)  
  
    # Text font  
    text_font = load_font('arial.ttf', 70)  
    text = "UNKNOWN ORDER"  
    left, _, right, _ = text_font.getbbox(text)  
    text_width = right - left  
    text_x = (1050 - text_width) // 2  
    text_y = (850 - 200) // 2  
    draw.text((text_x, text_y), text, fill=(0, 0, 0), font=text_font)  
  
    # Barcode font  
    barcode_font_size = 50  # font size  
    barcode_font = load_font(IDAutomationHC39M_font_path, barcode_font_size)  
    order_number = "*" + str(row['Order - Number']).strip('"') + "*"  
    barcode_font_color = (0, 0, 0)  # font color (black)  
    draw.text((225, 550), order_number, fill=barcode_font_color, font=barcode_font)  # position  
  
    return image     

# name the saved png
def save_image_with_subfolders(clean_sku, sku, order_number, index, qty_index, item_options, folder_name, image):  
    global images_saved_in_subfolder 
    global current_mug_subfolder  

    def generate_file_name(order_number, sku, index, qty_index, tumbler_color_text=None):  
        if tumbler_color_text and tumbler_color_text != "unknown_color":          
            return f"{order_number}_{sku}_{tumbler_color_text}_{index}_{qty_index + 1}.png"          
        else:          
            return f"{order_number}_{sku}_{index}_{qty_index + 1}.png"      
        
    tumbler_color_match = re.search(        
        r'(?:Tumbler )?Color(?:s)?: ([^,]+)', str(item_options))        
    tumbler_color_text = tumbler_color_match.group(1).replace(" ", "_") if tumbler_color_match else "unknown_color"     

    image_name = generate_file_name(order_number, sku, tumbler_color_text, index, qty_index)

    # create separate folders  
    if clean_sku.startswith("RNG"):  
        sub_folder_name = 'RNG'
    elif clean_sku.startswith("NCK02"):  
        sub_folder_name = 'NCK02'  
    elif clean_sku.startswith("NCK03"):
        sub_folder_name = 'NCK03'  
    elif clean_sku.startswith("NCK04"):  
        sub_folder_name = 'NCK04'
    elif re.match(r"WOOD66[A-Z0-9]*", sku, re.IGNORECASE):  
        sub_folder_name = '6X6'
    elif re.match(r"WOOD88[A-Z0-9]*", sku, re.IGNORECASE):  
        sub_folder_name = '8X8'
    elif re.match(r"WOOD1010[A-Z0-9]*", sku, re.IGNORECASE):  
        sub_folder_name = '10X10'
    elif re.match(r"WOOD1212[A-Z0-9]*", sku, re.IGNORECASE):  
        sub_folder_name = '12X12'
    elif re.match(r"WOOD186[A-Z0-9]*", sku, re.IGNORECASE):  
        sub_folder_name = '18X6'
    elif re.match(r"WOOD2412[A-Z0-9]*", sku, re.IGNORECASE):  
        sub_folder_name = '24X12'
    elif clean_sku.startswith("JMUG11WB"):  
        sub_folder_name = f'MUGS({current_mug_subfolder})'  
        if sub_folder_name not in images_saved_in_subfolder:  
            images_saved_in_subfolder[sub_folder_name] = 0  
  
        if images_saved_in_subfolder[sub_folder_name] >= 30:  
            current_mug_subfolder += 1  
            sub_folder_name = f'MUGS({current_mug_subfolder})'  
            images_saved_in_subfolder[sub_folder_name] = 0  
    else:  
        sub_folder_name = ''  
  
    if sub_folder_name:  
        sub_folder_path = os.path.join(folder_name, sub_folder_name)  
        if not os.path.exists(os.path.join(os.path.expanduser('~\\Downloads'), sub_folder_path)):  
            os.makedirs(os.path.join(os.path.expanduser('~\\Downloads'), sub_folder_path))  
        image_path = os.path.join(os.path.expanduser('~\\Downloads'), sub_folder_path, image_name)
    else:  
        image_path = os.path.join(os.path.expanduser('~\\Downloads'), folder_name, image_name)  
  
    image.save(image_path)  
  
    # Increment the images_saved_in_subfolder counter after saving the image  
    if clean_sku.startswith("JMUG11WB"):  
        images_saved_in_subfolder[sub_folder_name] += 1 
  
# Initialize the variables outside the function  
images_saved_in_subfolder = {}  
current_mug_subfolder = 1 

def save_image_without_options(sku, clean_sku, order_number, index, qty_index, background_image_path, folder_name, row, load_font, item_qty, order_quantities, order_skus):  
    if clean_sku not in sku_to_font:  
        print(f"Saving image without options for SKU: {sku}")  # Debug print  
        image_name = f"{order_number}_{sku}_{index}_{qty_index + 1}.png"  
        sub_folder_name = 'Stable'  
  
        sub_folder_path = os.path.join(folder_name, sub_folder_name)  
        if not os.path.exists(os.path.join(os.path.expanduser('~\\Downloads'), sub_folder_path)):  
            os.makedirs(os.path.join(os.path.expanduser('~\\Downloads'), sub_folder_path))  
        image_path = os.path.join(os.path.expanduser('~\\Downloads'), sub_folder_path, image_name)  
  
        if background_image_path is None:  
            print(f"Error: Personalization not found for {order_number}_{sku}_{index} config.py\line 195")  
            # image = create_check_csv_image()  
        else:  
            image = Image.open(background_image_path)  

        # Add barcode to the image  
        draw = ImageDraw.Draw(image)  
        add_order_number_to_jmug(draw, sku, row, load_font)
          
        image.save(image_path)  
        return True, image_path
    return False, None 
 

def save_blank_image(row, sku, clean_sku, sku_to_font, order_number, index, background_image_path, folder_name, load_font):            
    if (re.match(r"WOOD(66|88|1010|1212|2412)[A-Z0-9]*", sku, re.IGNORECASE) or re.match(r"JMUG11WB[A-Z0-9]*", sku, re.IGNORECASE)) and clean_sku not in sku_to_font and not re.search(r'Personalization', str(row['Item - Options'])):  
        image_name = f"{order_number}_{sku}_{index}.png"    
        sub_folder_name = None   
        image = None
        
        if "JMUG11WB" in sku.upper():    
            sub_folder_name = f'nonCustom_MUGS'
            
        if "WOOD66" in sku.upper():    
            sub_folder_name = '6X6'    
        elif "WOOD88" in sku.upper():    
            sub_folder_name = '8X8'    
        elif "WOOD1010" in sku.upper():    
            sub_folder_name = '10X10'    
        elif "WOOD1212" in sku.upper():    
            sub_folder_name = '12X12'   
        elif "WOOD186" in sku.upper():    
            sub_folder_name = '18X6'    
        elif "WOOD2412" in sku.upper():    
            sub_folder_name = '24X12'   
    
        if not sub_folder_name:    
            return False    
    
        sub_folder_path = os.path.join(folder_name, sub_folder_name)    
        if not os.path.exists(os.path.join(os.path.expanduser('~\\Downloads'), sub_folder_path)):    
            os.makedirs(os.path.join(os.path.expanduser('~\\Downloads'), sub_folder_path))    
        image_path = os.path.join(os.path.expanduser('~\\Downloads'), sub_folder_path, image_name)    
    
        if background_image_path is None:      
            print(f"Error: Personalization not found for {order_number}_{sku}_{index} config.py\line 240")     
        else:      
            image = Image.open(background_image_path)      
                
            draw = ImageDraw.Draw(image)    
            
            if "JMUG11WB" in sku.upper():    
                add_order_number_to_jmug(draw, sku, row, load_font)   
    
        if image is not None:  
            image.save(image_path)  
        else:  
            print(f"Error: Image not found for {order_number}_{sku}_{index}")      
        return True    
    return False     
 
# force font color   
def process_font_color(font_color, clean_sku, line_index):
    # line 1 = teal
    if (clean_sku == "UVPPSDENTTELUVP") and line_index == 0:   
        return (0, 128, 128)
    # line 1 = pink
    if (clean_sku == "JMUG11WBUVPPSNNCMUVP" or clean_sku == "UVPPSDENTPNKUVP") and line_index == 0:   
        return (252, 192, 197)
    # line 1 = grey    
    elif (clean_sku == "JMUG11WBUVPPSLNTBBUVP" or clean_sku == "JMUG11WBUVPPSICG1UVP") and line_index == 0:   
        return (166, 166, 166) 
    elif (clean_sku == "JMUG11WBUVPPSPFCMUVP"):   
        return (223, 4, 4) 
    # black
    if clean_sku.startswith("JMUG11WB") or clean_sku in [  
                # golfballs
                "UVPCCGNHBTUVP",
                # planks  
                 "UVPCCGFSSMUVP", "UVPJMBNSSUVP", "UVPJMASSSUVP", "UVPJMBTSSUVP",                      
                # tumblers  
                 "UVPPSNUBRBUVP", "UVPPSTTPTBUVP", "UVPPSTTPTABUVP", "UVPPSTTOTBUVP",   
                 "UVPPSTTOTABUVP", "UVPPSSLPTBUVP", "UVPPSOPTTBUVP", "UVPPSVETTBUVP",
                 "UVPJMHDBSUVP", "UVPPSDENTBLKUVP",
                 ]:    
        font_color = (0, 0, 0)    
    return font_color  

def process_special_rules(clean_sku, line, line_index):  
    # replace between spaces
    if clean_sku in ["UVPCCGTUMBUVP", "UVPCCGTUMWUVP", "UVPJMMAMATBUVP", "UVPJMMAMATWUVP", "UVPPSAUNTTBUVP", "UVPPSAUNTTWUVP", "UVPJMMNSUVP"] and line_index == 1:  # line 2 edit  
        line = re.sub(r'[ ,]+', '_', line)      
    if clean_sku in ["UVPJMMNSUVP", "JMUG11WBUVPPSGDMNUVP", "JMUG11WBUVPJMMCMWLYUVP"] and line_index == 0:  # line 1 edit  
        line = re.sub(r'[ ,]+', ' * ', line) 
    if clean_sku in ["UVPPSGKNTPUVP", "UVPPSGKNTSUVP"] and line_index == 1:  # line 2 edit  
        line = re.sub(r'[ ,]+', '-*-', line)  
    # replace end spaces  
    if clean_sku in ["UVPPSTTUMBUVP", "UVPPSTTUMWUVP"]:  
        processed_line = f"[_{line}_]"  
    elif clean_sku in ["UVPPSSTILGBHUVP", "UVPPSSTILGWHUVP"]:  
        processed_line = f"{line}_"  
    elif clean_sku in ["UVPJMSLCLBUVP", "UVPJMSLCLWUVP"]:  
        processed_line = f"({line})"
    elif clean_sku in ["UVPCCGTUMBUVP", "UVPCCGTUMWUVP", "UVPJMMAMATBUVP", "UVPJMMAMATWUVP", "UVPPSAUNTTBUVP", "UVPPSAUNTTWUVP"] and line_index == 1:  # line 2 edit  
        processed_line = f"[{line}]"
    else:  
        processed_line = line 
    if clean_sku in["JMUG11WBUVPJMFMEMUVP"]:
        processed_line = f"{line}+"
    if clean_sku in["UVPCCGNHBTUVP"]: 
        processed_line = f"{line} did."
    if clean_sku in["JMUG11WBUVPPSPFCMUVP"]: 
        processed_line = f"(...It’s {line})"

    return processed_line  

# color hexs
color_name_to_rgb = {  
    'blank': (0, 0, 0),
    'black': (0, 0, 0),    
    'white': (255, 255, 255),
    'coral': (255, 65, 103), 
    'purple': (128, 0, 128),
    'rose gold': (183, 110, 121),
    'teal': (92, 225, 230),
    'blush': (255, 192, 203),
    'lilac': (154, 113, 157),
    'maroon': (73, 5, 5),
    'baby blue': (163, 208, 230),
    'royal blue': (53, 82, 200),
    'navy': (50, 59, 96),
    'iceburg': (203, 217, 222),
    'seascape': (190, 233, 229),
    'gold': (255, 174, 51),
    'orange': (255, 145, 75),
    'yellow': (255, 211, 89),
    'gray': (166, 166, 166),
    'mint': (103, 230, 201),
    'baby pink': (254, 189, 198),
    'hot pink': (255, 102, 196),
    'pink': (255, 102, 196),  
     
}

# hard set the font color
def get_processed_font_color(clean_sku, item_options, color_name_to_rgb, get_font_color_for_dswclr001, process_font_color):
    if clean_sku.startswith(("RNG", "NCK", "SRN", "GLS")):
        font_color = (0, 0, 0)
    elif not clean_sku.startswith("DSWCLR001"):
        design_color_match = re.search(
            r'(?:Color of Text|Design Option & Color|Font Color|Wording Color|Design(?: Colors?)?|Custom Text Color):\s*([\w\s]+)',
            item_options)
        if design_color_match:
            design_color_text = design_color_match.group(1).lower()
        else:
            design_color_text = "white"
        font_color = color_name_to_rgb.get(design_color_text, (255, 255, 255))
    else:
        font_color = get_font_color_for_dswclr001(clean_sku)

    processed_font_color = process_font_color(font_color, clean_sku, line_index=0)
    return processed_font_color


# unicodes 
font_to_uni = {  
    "a": "0A01",  
    "b": "0A02",  
    "c": "0A03",  
    "d": "0A04",  
    "e": "0A05",  
    "f": "0A06",

    "g": "0B07",  
    "h": "0B08",  
    "i": "0B09",  
    "j": "0B10",  
    "k": "0B11",  
    "l": "0B12",

    "m": "0C13",  
    "n": "0C14",  
    "o": "0C15",  
    "p": "0C16",  
    "q": "0C17",  
    "r": "0C18",

    "s": "0D19",  
    "t": "0D20",  
    "u": "0D21",  
    "v": "0D22",  
    "w": "0D23",  
    "x": "0D24",

    "y": "0E25",  
    "z": "0E26",  
}

def handle_unicode_characters(clean_sku, processed_line, line_index, font_to_uni):
    # unicoded last letter  
    prefixes = ["NCKGLD", "NCKSIL", "NCKRSG", "NCK02GLD", "NCK02SIL", "NCK02RSG", "NCK03GLD", "NCK03SIL", "NCK03RSG", "NCK04GLD", "NCK04SIL", "NCK04RSG"]  
    if any(clean_sku.startswith(prefix) for prefix in prefixes) or (clean_sku.startswith("RNG") and line_index == 1):  
        last_char = processed_line[-1].lower()  
        unicode_code = font_to_uni.get(last_char)  
        if unicode_code:  
            processed_line = processed_line[:-1] + chr(int(unicode_code, 16))  
        else:  
            print(f"Warning: Unicode character not found for '{last_char}'.")  

    # unicoded first letter  
    month_codes = {  
        "NCKJAN": "1A01",  
        "NCKFEB": "1A02",  
        "NCKMAR": "1A03",  
        "NCKAPR": "1A04",  
        "NCKMAY": "1A05",  
        "NCKJUN": "1A06",  
        "NCKJUL": "1A07",  
        "NCKAUG": "1A08",  
        "NCKSEP": "1A09",  
        "NCKOCT": "1A10",  
        "NCKNOV": "1A11",  
        "NCKDEC": "1A12",  
    }  

    for month, code in month_codes.items():    
        if clean_sku.startswith(month):    
            first_char = processed_line[0]    
            unicode_code = font_to_uni.get(first_char.lower())    
            if unicode_code:    
                processed_line = chr(int(code, 16)) + first_char + processed_line[1:]    
            else:    
                print(f"Warning: Unicode character not found for '{first_char}'.")    
            break

    return processed_line
