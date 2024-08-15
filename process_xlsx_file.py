import os  
import json  
import requests  
import pandas as pd  
from csv import DictWriter  
  
  
def appendrow(output_file, Order_Number, Item_Qty, Item_SKU, Item_Options, Due_Dates, Custom_Field3):  
    combined_dict = {  
        "Order - Number": Order_Number,  
        "Item - Qty": Item_Qty,  
        "Item - SKU": Item_SKU,  
        "Item - Options": Item_Options,  
        "Item - Name": Due_Dates,  
        "Custom - Field 3": Custom_Field3  
    } 

    # Read the existing CSV file into a DataFrame  
    try:  
        df = pd.read_csv(output_file)  
    except FileNotFoundError:  
        df = pd.DataFrame(columns=combined_dict.keys())  
  
    # Check for duplicates  
    is_duplicate = (  
        (df['Order - Number'] == Order_Number) &  
        (df['Item - Qty'] == Item_Qty) &  
        (df['Item - SKU'] == Item_SKU) &  
        (df['Item - Options'] == Item_Options) &  
        (df['Item - Name'] == Due_Dates) &  
        (df['Custom - Field 3'] == Custom_Field3)  
    ).any()  
  
    if not is_duplicate:  
        with open(output_file, 'a', newline='') as f_object:  
            dictwriter_object = DictWriter(f_object, fieldnames=combined_dict.keys())  
  
            # Write header if the file is empty  
            if f_object.tell() == 0:  
                dictwriter_object.writeheader()  
  
            dictwriter_object.writerow(combined_dict)  
    else:  
        print("Duplicate row found. No row appended.")  
  
  
def remove_duplicates(output_file):  
    try:  
        # Read the existing CSV file into a DataFrame  
        df = pd.read_csv(output_file)  
        # Drop duplicate rows  
        df.drop_duplicates(inplace=True)  
  
        # Save the DataFrame to the Downloads folder  
        df.to_csv(output_file, index=False)  
        print(f"The file {output_file} has been created.")  
  
        print("Duplicates removed successfully.")  
    except FileNotFoundError:  
        print(f"The file {output_file} does not exist.")  
    except Exception as e:  
        print(f"An error occurred: {e}")  
  
  
def order_details(output_file, barcode, due_date):
    print('')
    print(f"Converting Order Number: {barcode}")
    url = "https://apicall"  
    payload = json.dumps({"OrderNumber": barcode})  
    headers = {'Content-Type': 'application/json'}  
    try:  
        response = requests.request("GET", url, headers=headers, data=payload)  
        dictr = response.text  
        response_dict = json.loads(dictr)  
        jsonob = response_dict["items"]  
  
        for count in (enumerate(jsonob)):  
            Item_ID = (count[1]["name"])  
            Qty = (count[1]["quantity"])  
            SKU = (count[1]["sku"])  
            for i in range(Qty):  
                i = "{0}".format(i+1)  
                appendrow(output_file, barcode, Qty, SKU, f'{Item_ID}', due_date, "CustomField3") 

    except:  
        print("API CALL FAIL: Order number", barcode)  
  
  

def process_xlsx(file_stream):  
    df = pd.read_excel(file_stream)  

    DOWNLOAD_FOLDER = os.path.join(os.path.expanduser("~"), "Downloads")  
    output_file = os.path.join(DOWNLOAD_FOLDER, "combined.csv")  
  
    for index, row in df.iterrows():  
        if 'Package ID' in df.columns:  
            order_number = str(row['Package ID'])  
        else:  
            break  
        due_date = str(row['Ship By Date'])  
        order_details(output_file, order_number, due_date)  
    remove_duplicates(output_file)  
    print("CSV READY FOR LABEL GENERATION")  
      
    # Read the processed CSV file into a DataFrame  
    processed_df = pd.read_csv(output_file)  
      
    # Convert the DataFrame to a list of lists (similar to CSV data)  
    processed_data = processed_df.values.tolist()  
    # Add the column names as the first row  
    processed_data.insert(0, list(processed_df.columns))  
  
    print('')
    print(f".XLSX converted. CSV exported to {DOWNLOAD_FOLDER}.")
    print('')
    return {"csv_url": "/csv/combined.csv"}