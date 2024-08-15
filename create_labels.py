
from config import * 
from blabel_config import add_order_number_to_blabel_pdf  
  
def create_labels(index, row, folder_name, sku, clean_sku, order_quantities, order_skus, process_label, order_item_count, order_total_qty, txt_output_folder,  customtagID):  
    DOWNLOAD_FOLDER = str(Path.home() / 'Downloads')  
    dtg_folder = os.path.join(os.path.dirname(os.path.realpath(__file__)), '\\\\sharedrive')  
  
    custom_field_3 = row['Custom - Field 3']  
    sku = row['Item - SKU']  
    order_number = str(row['Order - Number']).strip('"')  
    item_options = str(row['Item - Options'])  
    item_qty = int(row['Item - Qty']) 
  
    def match_sku_to_item_description(sku):  
        if getattr(sys, 'frozen', False):  
            bundle_dir = sys._MEIPASS  
        else:  
            bundle_dir = os.path.dirname(os.path.abspath(__file__))  
        
        json_path = Path(bundle_dir)  # This should be outside the else block  
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
  
    sku_description = match_sku_to_item_description(clean_sku)  
  
    blabel_item_name = sku_description  
    clabel_item_name = sku_description + ', ' + row['Item - Name']  
    item_list_description = sku_description + ', ' + row['Item - Name']  
  
    # "BLABEL" orders  
    if clean_sku.startswith("BLABEL"):  
        png_path_front = None  
        png_path_back = None  
  
        # Find print_url_front  
        art_location_match_front = re.search(r'Art_Location(?:_Front)?:\s*(https://[\w\./?=-]+(?:[\w\./?=&-]+)?)', item_options)  
        if art_location_match_front:  
            art_location_url_front = art_location_match_front.group(1)  
            response_front = requests.get(art_location_url_front)  
            if response_front.status_code == 200:  
                # Save the .png file  
                png_path_front = create_blabel_path(folder_name, order_number.replace('*', ''), index, "front")  
                with open(png_path_front, 'wb') as f:  
                    f.write(response_front.content)  
            else:  
                print(f"Error downloading PDF from Art_Location_Front: {art_location_url_front}")  
  
        # Find print_url_back  
        art_location_match_back = re.search(r'Art_Location(?:_Back)?:\s*(https://[\w\./?=-]+(?:[\w\./?=&-]+)?)', item_options)  
        if art_location_match_back:  
            art_location_url_back = art_location_match_back.group(1)  
            response_back = requests.get(art_location_url_back)  
            if response_back.status_code == 200:  
                # Save the .png file  
                png_path_back = create_blabel_path(folder_name, order_number.replace('*', ''), index, "back")  
                with open(png_path_back, 'wb') as f:  
                    f.write(response_back.content)  
            else:  
                print(f"Error downloading PDF from Art_Location_Back: {art_location_url_back}")  
  
        if process_label:
            front_png_name = f"{customtagID}_{item_options}_front.png"  
            back_png_name = f"{customtagID}_{item_options}_back.png"  
            front_png_path = os.path.join(dtg_folder, front_png_name)  
            back_png_path = os.path.join(dtg_folder, back_png_name)  
            front_png_exists = os.path.exists(front_png_path)  
            back_png_exists = os.path.exists(back_png_path)  
            add_order_number_to_blabel_pdf(sku, row, folder_name, blabel_item_name, index, item_qty, order_quantities, order_skus, order_item_count, customtagID, front_png_exists, back_png_exists)  
  
        return  
  
    # "CLABEL" orders and 'C' orders  
    if clean_sku.startswith("CLABEL") or order_number.startswith('C'):  
        file_path = None  
        if clean_sku.startswith("CLABEL"):  
            pattern = r'print_url(?:_1)?:\s*(https://[\w\./?=-]+(?:[\w\./?=&-]+)?)'  
        elif order_number.startswith('C'):  
            pattern = r'Art Location 1:\s*(https://[\w\./?=]+)'  
        # Add support for Dropbox URLs  
        pattern += r'|(https://(?:www\.)?dropbox\.com/[\w\./?=&-]+)'  
  
        art_location_match = re.search(pattern, item_options)  
        if art_location_match:  
            art_location_url = art_location_match.group(1) or art_location_match.group(2)  
            # Convert Dropbox URL to a direct download URL  
            if "dropbox.com" in art_location_url:  
                art_location_url = art_location_url.replace("www.dropbox.com", "dl.dropboxusercontent.com")  
            response = requests.get(art_location_url)  
            if response.status_code == 200:  
                content_type = response.headers['content-type']  
                if 'pdf' in content_type:  
                    extension = '.pdf'  
                elif 'png' in content_type:  
                    extension = '.png'  
                else:  
                    print(f"Unsupported content type: {content_type}")  
                    return  
                file_name = f"{order_number}{index}{extension}"  
                file_path = os.path.join(folder_name, file_name)  
                with open(file_path, 'wb') as f:  
                    f.write(response.content)  
            else:  
                print(f"Error downloading file from Art Location: {art_location_url}")  
        else:  
            print(f"Art Location not found in Item - Options: {item_options}")  
  
        if process_label:  
            if file_path is not None:  
                add_order_number_to_clabel_pdf(sku, row, folder_name, index, custom_field_3, item_qty, clabel_item_name, item_list_description, file_path, order_number, order_quantities, order_skus, process_label)  
            else:  
                create_label_with_blank_image(sku, row, folder_name, index, custom_field_3, item_qty, clabel_item_name, item_list_description, order_number, order_quantities, order_skus, process_label)  
  
        return  

    
