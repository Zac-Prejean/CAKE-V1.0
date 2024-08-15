
from config import *

used_numbers = set()  
  
def generate_custom_id_tag():  
    current_date = datetime.now().strftime("%m%d")  
    random_number = random.randint(1000, 9999)  
    while random_number in used_numbers:  
        random_number = random.randint(1000, 9999)  
    used_numbers.add(random_number)  
    return f"{current_date}{random_number}"  
 
def create_txt_file(order_number, item_options, sku, index, order_total_qty, txt_output_folder, custom_field_3, customtagID):  
    current_datetime = datetime.now().strftime("%m-%d-%Y %H:%M")  
    file_path = os.path.join(txt_output_folder, f"{custom_field_3}.txt")  
    archive_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), '\\\\sharedrive', 'Batch.txt', 'archive', f"{custom_field_3}_archive.txt")  
  
    with open(file_path, 'a') as file:  
        file.write(f"{customtagID}_{order_number}_{item_options}_{order_total_qty}_{sku}_{custom_field_3}_Designed_{current_datetime}_0\n")  
  
    with open(archive_path, 'a') as archive_file:  
        archive_file.write(f"{customtagID}_{order_number}_{item_options}_{order_total_qty}_{sku}_{custom_field_3}_Archive_{current_datetime}_0\n")  
  
    return customtagID 

def process_csv(file_path, order_number, item_qty, item_options, customtagID):  
    with open(file_path, newline='') as csvfile:  
        reader = csv.DictReader(csvfile)  
        for row in reader:  
            item_id = item_options  # Assuming Item_ID is stored in 'Item - Options'  
            get_order_images(order_number, item_qty, item_id, customtagID)  
  
def get_order_images(order_number, item_qty, item_id, customtagID):  
    url = "https://apicall"  
    payload = json.dumps({"OrderNumber": order_number})  
    headers = {'Content-Type': 'application/json'}  
  
    try:  
        response = requests.request("GET", url, headers=headers, data=payload)  
        if response.status_code != 200:  
            print(f"API call failed with status code: {response.status_code}")  
            return  
          
        dictr = response.text  
        response_dict = json.loads(dictr)  
        jsonob = response_dict["items"]  
        storeName = str(response_dict["advancedOptions"]['storeName'])  
   
        if storeName == "Zazzle":  
            for item in jsonob:  
                if item["name"] == item_id:  
                    download_images(item, item_id, customtagID)  
                    break  
                  
    except Exception as e:  
        print(f"Order_Number {order_number} has failed please check. Error: {e}")  
  
def download_images(item, item_id, customtagID):  
    if str(item["options"][0]["name"]) == "print_sku":  
        if str(item["options"][4]["value"]) == "front":   
            preview_url = "{0}".format(item["options"][1]["value"])  
            file_name_front = customtagID + "_" + item_id + "_front_mockup.png"  
            download_png(preview_url, file_name_front)  
            art_url = "{0}".format(item["options"][2]["value"])  
            file_name_back = customtagID + "_" + item_id + "_front.png"  
            download_png(art_url, file_name_back) 
            print("front only") 
        else:    
            preview_url = "{0}".format(item["options"][1]["value"])  
            file_name_front = customtagID + "_" + item_id + "_back_mockup.png"  
            download_png(preview_url, file_name_front)  
            art_url = "{0}".format(item["options"][2]["value"])  
            file_name_back = customtagID + "_" + item_id + "_back.png"  
            download_png(art_url, file_name_back)  
            print("back only") 
    else:  
        try:  
            preview_url = "{0}".format(item["options"][6]["value"])  
            file_name_front = customtagID + "_" + item_id + "_front.png"  
            download_png(preview_url, file_name_front)  
            preview_url = "{0}".format(item["options"][10]["value"])  
            file_name_front = customtagID + "_" + item_id + "_front_mockup.png"  
            download_png(preview_url, file_name_front)  
            preview_url = "{0}".format(item["options"][8]["value"])  
            file_name_front = customtagID + "_" + item_id + "_back.png"  
            download_png(preview_url, file_name_front)  
            preview_url = "{0}".format(item["options"][11]["value"])  
            file_name_front = customtagID + "_" + item_id + "_back_mockup.png"  
            download_png(preview_url, file_name_front) 
            print("front and back") 
        except:  
            preview_url = "{0}".format(item["options"][6]["value"])  
            file_name_front = customtagID + "_" + item_id + "_front.png"  
            download_png(preview_url, file_name_front)  
            preview_url = "{0}".format(item["options"][9]["value"])  
            file_name_front = customtagID + "_" + item_id + "_front_mockup.png"  
            download_png(preview_url, file_name_front)  
            preview_url = "{0}".format(item["options"][8]["value"])  
            file_name_front = customtagID + "_" + item_id + "_back.png"  
            download_png(preview_url, file_name_front)  
            preview_url = "{0}".format(item["options"][10]["value"])  
            file_name_front = customtagID + "_" + item_id + "_back_mockup.png"  
            download_png(preview_url, file_name_front) 
            print("front and back") 
  
def download_png(url, file_name):  
    DOWNLOAD_FOLDER = str(Path.home() / 'Downloads')  
    dtg_folder = os.path.join('\\\\sharedrive')  
    full_path_down = os.path.join(dtg_folder, file_name)  
      
    try:  
        urllib.request.urlretrieve(url, full_path_down)  
        print(f"Downloaded {file_name}")  
        return full_path_down  
    except Exception as e:  
        print(f"Failed to download {file_name}. Error: {e}")  
        return None 
