from datetime import datetime 
from config import * 

# UPDATE SINGLE ITEMS IN ORDER
def updateStatus(itemID, order_number, itemName, new_status, scanned, filename, cubby_number):    
    
    print('')    
    print(f"Updating status for itemID: {itemID}, order_number: {order_number}, new_status: {new_status}")
    print('')  

    designed_file_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), '\\\\sharedrive', 'Batch.txt', 'status', filename)    
    archive_file_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), '\\\\sharedrive', 'Batch.txt', 'archive', f"{filename.split('.')[0]}_archive.txt")    
    
    for file_path in [designed_file_path, archive_file_path]:    
        if not os.path.exists(file_path):    
            print(f"File not found: {file_path}")    
            continue    
    
        with open(file_path, 'r') as file:    
            lines = file.readlines()    
    
        updated_lines = []    
        current_datetime = datetime.now().strftime("%m-%d-%Y %H:%M")    
        found = False    
        archive_status = new_status if file_path != designed_file_path else None  
  
        for line in lines:    
            stripped_line = line.strip()  
            if (scanned and stripped_line.startswith(f"{itemID}_{order_number}_")) or (not scanned and stripped_line.startswith(f"{itemID}_")):    
                if new_status == "Shipped":    
                    if file_path == designed_file_path:  
                        found = True  # Mark as found, but don't add the line back to updated_lines for designed_file_path  
                    else:  
                        parts = stripped_line.split('_')    
                        parts[6] = archive_status    
                        updated_line = '_'.join(parts) + "\n"    
                        updated_lines.append(updated_line)  # Keep the "Shipped" status line in archive_file_path  
                        found = True  
                else:    
                    parts = stripped_line.split('_')    
                    parts[6] = new_status    
                    parts[7] = current_datetime.strip()    
                    parts[8] = str(cubby_number) if cubby_number is not None else "0"  # Replace _0 with the cubby number or "0" if it's None    
                    updated_line = '_'.join(parts) + "\n"    
                    updated_lines.append(updated_line)    
                    found = True    
            else:    
                updated_lines.append(line)    
    
        if not found:    
            print("Scanned number not found")    
            return jsonify({"error": "Scanned number not found"}), 404    
    
        with open(file_path, 'w') as file:    
            file.writelines(updated_lines)    
    
    return jsonify({"message": "Status updated successfully"}), 200    


# UPDATE ALL ITEMS IN ORDER
def updateAllItemsStatus(order_number, new_status, filename, cubby_number=None):    
    file_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), '\\\\sharedrive', 'Batch.txt', 'status', filename)  
  
    if not os.path.exists(file_path):              
        return "File not found", 404  
  
    with open(file_path, 'r') as file:              
        lines = file.readlines()  
  
    updated_lines = []              
    current_datetime = datetime.now().strftime("%m-%d-%Y %H:%M")              
    found = False  
  
    for line in lines:    
        line_order_number, *_ = line.split("_")  
  
        if line_order_number == order_number:  
            if new_status == "Shipped":    
                found = True  # Mark as found, but don't add the line back to updated_lines    
            else:  
                parts = line.split('_')      
                parts[5] = new_status      
                parts[6] = current_datetime.strip()      
                parts[7] = str(cubby_number) if cubby_number is not None else "0"  # Replace _0 with the cubby number or "0" if it's None      
                updated_line = '_'.join(parts) + "\n"      
                updated_lines.append(updated_line)      
                found = True  
        else:    
            updated_lines.append(line)  
  
    if not found:              
        return jsonify({"error": "Scanned number not found"}), 404  
  
    with open(file_path, 'w') as file:              
        file.writelines(updated_lines)  
  
    return jsonify({"message": "Status updated successfully"}), 200  

# SWITCHES .TXT FILES
def get_txt_files(folder="status"):  
    if folder == "archive":  
        folder_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), '\\\\sharedrive', 'Batch.txt', 'archive')  
    else:  # default to "status" folder  
        folder_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), '\\\\sharedrive', 'Batch.txt', 'status')  
      
    txt_files = glob.glob(f"{folder_path}/*.txt")  
    return [os.path.basename(file) for file in txt_files]  
 

# CHECK STATUS
def getStatus(scannedNumber, fileName):  
    file_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), '\\\\sharedrive', 'Batch.txt', 'status', fileName);  
    if not os.path.exists(file_path):  
        return "File not found", 404  

    with open(file_path, 'r') as file:  
        lines = file.readlines()  
  
    status = "UNKNOWN"  
    for line in lines:  
        if line.startswith(scannedNumber + "_"):  
            if "Designed" in line:  
                status = "DESIGNED"  
            elif "Scanned-In" in line:  
                status = "SCANNED-IN" 
            elif "Printed" in line:  
                status = "PRINTED" 
            elif "Scanned-Out" in line:  
                status = "SCANNED-OUT" 
            elif "Cubby" in line:  
                status = "CUBBY" 
            elif "Shipped" in line:  
                status = "SHIPPED"       
            break  
  
    return status