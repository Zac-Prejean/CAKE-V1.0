import os
import re
from PIL import Image, ImageDraw, ImageFont  

script_dir = os.path.dirname(os.path.abspath(__file__))

# flip horazonal
def flip_mug_image(image, sku): 
    if re.match(r"JMUG11WB[A-Z0-9]*|ACRTOPRCT[A-Z0-9]*", sku):  
        image = image.transpose(method=Image.Transpose.FLIP_LEFT_RIGHT)  
    draw = ImageDraw.Draw(image)  
    return image, draw

# barcode  
IDAutomationHC39M_font_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'fonts', 'IDAutomationHC39M.ttf')  

def add_order_number_to_jmug(draw, sku, row, load_font):      
    if re.match(r"JMUG11WB[A-Z0-9]*", sku):      
        order_number = "*" + str(row['Order - Number']).strip('"') + "*"          
        processed_font_color = (0, 0, 0)  # font color (black)      
    
        num_chars = len(order_number)    
    
        if num_chars < 15:  
            font_size_order_number = 30
            font_order_number = load_font(IDAutomationHC39M_font_path, font_size_order_number) 
            draw.text((100, 790), order_number, fill=processed_font_color, font=font_order_number)  # position 
        else:   
            font_size_order_number = 20
            font_order_number = load_font(IDAutomationHC39M_font_path, font_size_order_number) 
            draw.text((80, 790), order_number, fill=processed_font_color, font=font_order_number)  # position 

def add_order_indicators(draw, sku, row, item_qty, order_quantities, order_skus):  
 
    if re.match(r"JMUG11WB[A-Z0-9]*", sku):  
 
        # EXPEDITED square    
        order_number = str(row['Order - Number']).strip('"')    
        expedited_order = order_number[-1].upper() == 'R' or 'EXP' in order_number.upper()    
          
        if not expedited_order:      
            EX_x = 12    
            EX_y = 783    
            EX_square_size = 55    
            draw.rectangle([(EX_x, EX_y), (EX_x + EX_square_size, EX_y + EX_square_size)], fill=(255, 255, 255))  
  
        # MULTI LINE square         
        order_number = str(row['Order - Number'])        
        order_skus_for_order_number = order_skus[order_number]      
      
        all_skus_start_with_jmug11 = True    
        for other_sku in order_skus_for_order_number:    
            if not other_sku.startswith("JMUG11"):    
                all_skus_start_with_jmug11 = False    
                break    
  
        if all_skus_start_with_jmug11:   
            ML_x = 511            
            ML_y = 845            
            ML_square_size = 55            
            draw.rectangle([(ML_x, ML_y), (ML_x + ML_square_size, ML_y + ML_square_size)], fill=(255, 255, 255))        
        else:    
            pass    
  
        # MULTI ORDER square    
        order_total_qty = order_quantities.get(order_number, 0)    
        multi_order = order_total_qty > 1      
      
        if not multi_order:         
            MO_x = 12      
            MO_y = 845      
            MO_square_size = 55      
            draw.rectangle([(MO_x, MO_y), (MO_x + MO_square_size, MO_y + MO_square_size)], fill=(255, 255, 255))   
                  
        # DUPLICATE ORDER square  
        duplicate_order = item_qty > 1  
  
        if not duplicate_order:
            DO_x = 511  
            DO_y = 783    
            DO_square_size = 55    
            draw.rectangle([(DO_x, DO_y), (DO_x + DO_square_size, DO_y + DO_square_size)], fill=(255, 255, 255))  
    else:  
        print(f"SKU not supported for order indicators: {sku}")  # Debug print  

sku_to_image = { 

    # customizable
    "JMUG11WBUVPPSLNTBBUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'customizable', 'blank_.png'),
    "JMUG11WBUVPPSICG1UVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'customizable', 'blank_.png'),    
    "JMUG11WBUVPPSNNCMUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'customizable', 'blank_.png'),
    "JMUG11WBUVPJMSAYOCMUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'customizable', 'UVPJMSAYOCMUVP.png'),
    "JMUG11WBUVPJMSAY1KMUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'customizable', 'UVPJMSAY1KMUVP.png'),
    "JMUG11WBUVPJMOVMUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'customizable', 'UVPJMOVMUVP.png'),
    "JMUG11WBUVPPSFUNCMUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'customizable', 'UVPPSFUNCMUVP.png'),
    "JMUG11WBUVPPSWIPEUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'customizable', 'UVPPSWIPEUVP.png'),
    "JMUG11WBUVPPSMUWRMUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'customizable', 'UVPPSMUWRMUVP.png'),
    "JMUG11WBUVPPSDUWRMUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'customizable', 'UVPPSDUWRMUVP.png'),
    "JMUG11WBUVPJMBTOIMUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'customizable', 'UVPJMBTOIMUVP.png'),
    "JMUG11WBSUBJMSUWOMSUB": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'customizable', 'SUBJMSUWOMSUB.png'),
    "JMUG11WBUVPPSSPERMMUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'customizable', 'UVPPSSPERMMUVP.png'),
    "JMUG11WBUVPPSBONDUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'customizable', 'UVPPSBONDUVP.png'),
    "JMUG11WBSUBUYTHTSUB": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'customizable', 'SUBUYTHTSUB.png'),
    "JMUG11WBUVPJMFMEMUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'customizable', 'UVPJMFMEMUVP.png'),
    "JMUG11WBUVPPSYBCMUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'customizable', 'UVPPSYBCMUVP.png'),
    "JMUG11WBUVPPSSBFRUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'customizable', 'UVPPSSBFRUVP.png'),
    "JMUG11WBUVPJMCCAS1UVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'customizable', 'blank_.png'),
    "JMUG11WBUVPJMCCAS2UVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'customizable', 'blank_.png'),
    "JMUG11WBUVPJMCCAS3UVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'customizable', 'blank_.png'),
    "JMUG11WBUVPJMCCAS4UVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'customizable', 'blank_.png'),
    "JMUG11WBUVPJMCCTNR1UVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'customizable', 'blank_.png'),
    "JMUG11WBUVPJMCCTNR2UVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'customizable', 'blank_.png'),
    "JMUG11WBUVPJMCCTNR3UVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'customizable', 'blank_.png'),
    "JMUG11WBUVPJMCCDS1UVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'customizable', 'blank_.png'),
    "JMUG11WBUVPJMCCDS2UVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'customizable', 'blank_.png'),
    "JMUG11WBUVPJMCCDS3UVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'customizable', 'blank_.png'),
    "JMUG11WBUVPPSBALLS2UVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'customizable', 'UVPPSBALLS2UVP.png'),
    "JMUG11WBUVPCCFREKEX1UVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'customizable', 'UVPCCFREKEX1UVP.png'),
    "JMUG11WBUVPPSTYBMUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'customizable', 'UVPPSTYBMUVP.png'),
    "JMUG11WBUVPPSSBNALUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'customizable', 'blank_.png'),
    "JMUG11WBUVPPSPFCMUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'customizable', 'UVPPSPFCMUVP.png'),
    "JMUG11WBUVPPSLAYBNSMUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'customizable', 'UVPPSLAYBNSMUVP.png'),
    "JMUG11WBUVPPSNORMUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'customizable', 'UVPPSNORMUVP.png'),
    "JMUG11WBUVPJMIFLYMUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'customizable', 'UVPJMIFLYMUVP.png'),
    "JMUG11WBUVPPSSCMUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'customizable', 'UVPPSSCMUVP.png'),
    "JMUG11WBUVPPSGDMNUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'customizable', 'UVPPSGDMNUVP.png'),
    "JMUG11WBUVPPSDLGFBMUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'customizable', 'UVPPSDLGFBMUVP.png'),
    "JMUG11WBUVPPSBOBWUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'customizable', 'UVPPSBOBWUVP.png'),
    "JMUG11WBUVPPSFARTUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'customizable', 'UVPPSFARTUVP.png'),
    "JMUG11WBUVPJMMCMWLYUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'customizable', 'UVPJMMCMWLYUVP.png'),
    "JMUG11WBUVPPSIMDAMUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'customizable', 'UVPPSIMDAMUVP.png'),
    "JMUG11WBUVPPSPSIBUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'customizable', 'UVPPSPSIBUVP.png'),
    "JMUG11WBUVPJMRTFTMUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'customizable', 'UVPJMRTFTMUVP.png'),
    "JMUG11WBUVPPSFAVEUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'customizable', 'UVPPSFAVEUVP.png'),
    "JMUG11WBUVPPSUBCNSBUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'customizable', 'UVPPSUBCNSBUVP.png'),
    "JMUG11WBUVPPSNCC1UVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'customizable', 'UVPPSNCC1UVP.png'),
    "JMUG11WBUVPPSTCMUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'customizable', 'UVPPSTCMUVP.png'),
    "JMUG11WBUVPPSCRAYMUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'customizable', 'UVPPSCRAYMUVP.png'),
    "JMUG11WBUVPPSFLONAMEUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'customizable', 'UVPPSFLONAMEUVP.png'),
    "JMUG11WBUVPPSBTEMUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'customizable', 'UVPPSBTEMUVP.png'),
    "JMUG11WBUVPPSBFCEUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'customizable', 'UVPPSBFCEUVP.png'),
    "JMUG11WBUVPJMFDCM7UVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'customizable', 'UVPJMFDCM7UVP.png'),
    "JMUG11WBUVPPSBMMMUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'customizable', 'UVPPSBMMMUVP.png'),

    # fav child
    "JMUG11WBUVPPSFAVCHUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'customizable', 'UVPPSFAVCHUVP.png'),
    "JMUG11WBUVPPS2FAVCHUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'customizable', 'UVPPS2FAVCHUVP.png'),
    "JMUG11WBUVPPS3FAVCHUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'customizable', 'UVPPS3FAVCHUVP.png'),
    "JMUG11WBUVPPS4FAVCHUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'customizable', 'UVPPS4FAVCHUVP.png'),

    # christmas
    "JMUG11WBUVPPSCMSMUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'customizable', 'UVPPSCMSMUVP.png'),
    "JMUG11WBUVPPSCMSRUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'customizable', 'UVPPSCMSRUVP.png'),
    "JMUG11WBUVPPSCMGRUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'customizable', 'UVPPSCMGRUVP.png'),
    "JMUG11WBUVPCCKHCSMUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'customizable', 'UVPCCKHCSMUVP.png'),

    # Little Miss
    "JMUG11WBUVPPSLILMSUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'customizable', 'UVPPSLILMSUVP.png'),
    "JMUG11WBUVPPSLILMGUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'customizable','UVPPSLILMGUVP.png'),
    "JMUG11WBUVPPSLILMPUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'customizable','UVPPSLILMPUVP.png'),
    
    # stable
    "JMUG11WBUVPCAITSUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'stable','UVPCAITSUVP.png'),
    "JMUG11WBUVPCCBESTTMNUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'stable', 'UVPCCBESTTMNUVP.png'),
    "JMUG11WBUVPCCCRYPUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'stable', 'UVPCCCRYPUVP.png'),
    "JMUG11WBUVPCCSCHITTMUGUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'stable','UVPCCSCHITTMUGUVP.png'),
    "JMUG11WBUVPCCUPMILFUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'stable', 'UVPCCUPMILFUVP.png'),
    "JMUG11WBUVPCCWEDCUPUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'stable', 'UVPCCWEDCUPUVP.png'),
    "JMUG11WBUVPCCWITCHUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'stable','UVPCCWITCHUVP.png'),
    "JMUG11WBUVPDHDED2ME1UVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'stable', 'UVPDHDED2ME1UVP.png'),   
    "JMUG11WBUVPHIKEUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'stable', 'UVPHIKEUVP.png'),
    "JMUG11WBUVPHOCUSMUGUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'stable','UVPHOCUSMUGUVP.png'),
    "JMUG11WBUVPJMBFNEUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'stable', 'UVPJMBFNEUVP.png'),
    "JMUG11WBUVPJMDCCUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'stable', 'UVPJMDCCUVP.png'),
    "JMUG11WBUVPJMDIRMEUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'stable', 'UVPJMDIRMEUVP.png'),  
    "JMUG11WBUVPJMDLSUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'stable','UVPJMDLSUVP.png'),
    "JMUG11WBUVPJMDWMMUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'stable', 'UVPJMDWMMUVP.png'),
    "JMUG11WBUVPJMIHTDMUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'stable', 'UVPJMIHTDMUVP.png'),
    "JMUG11WBUVPJMPCCUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'stable','UVPJMPCCUVP.png'),
    "JMUG11WBUVPJMSAWTUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'stable', 'UVPJMSAWTUVP.png'),
    "JMUG11WBUVPMONKEYSCCUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'stable', 'UVPMONKEYSCCUVP.png'),
    "JMUG11WBUVPPPSJEFFDMUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'stable','UVPPPSJEFFDMUVP.png'),
    "JMUG11WBUVPPSADHOUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'stable', 'UVPPSADHOUVP.png'),
    "JMUG11WBUVPPSASTRMUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'stable', 'UVPPSASTRMUVP.png'),
    "JMUG11WBUVPPSBFNDMUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'stable', 'UVPPSBFNDMUVP.png'),   
    "JMUG11WBUVPPSBFWOUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'stable', 'UVPPSBFWOUVP.png'),
    "JMUG11WBUVPPSROMEUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'stable', 'UVPPSROMEUVP.png'),
    "JMUG11WBUVPPSCATMUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'stable','UVPPSCATMUVP.png'),
    "JMUG11WBUVPPSCHIROUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'stable', 'UVPPSCHIROUVP.png'),
    "JMUG11WBUVPPSCUMUFUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'stable', 'UVPPSCUMUFUVP.png'),
    "JMUG11WBUVPPSDADABMUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'stable','UVPPSDADABMUVP.png'),
    "JMUG11WBUVPPSDFCMUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'stable', 'UVPPSDFCMUVP.png'),
    "JMUG11WBUVPPSDJLOUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'stable', 'UVPPSDJLOUVP.png'),
    "JMUG11WBUVPPSDMDWUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'stable','UVPPSDMDWUVP.png'),
    "JMUG11WBUVPPSDOCAUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'stable', 'UVPPSDOCAUVP.png'),
    "JMUG11WBUVPPSDTCNUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'stable', 'UVPPSDTCNUVP.png'),
    "JMUG11WBUVPPSDUMBUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'stable','UVPPSDUMBUVP.png'),
    "JMUG11WBUVPPSEPTUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'stable', 'UVPPSEPTUVP.png'),
    "JMUG11WBUVPPSFQOHRUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'stable', 'UVPPSFQOHRUVP.png'),
    "JMUG11WBUVPPSHUDBCUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'stable','UVPPSHUDBCUVP.png'),
    "JMUG11WBUVPPSHUDICKUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'stable', 'UVPPSHUDICKUVP.png'),
    "JMUG11WBUVPPSIBGMUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'stable', 'UVPPSIBGMUVP.png'),
    "JMUG11WBUVPPSIDRBHUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'stable','UVPPSIDRBHUVP.png'),
    "JMUG11WBUVPDHDED2ME1UVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'stable', 'UVPDHDED2ME1UVP.png'),   
    "JMUG11WBUVPHIKEUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'stable', 'UVPHIKEUVP.png'),
    "JMUG11WBUVPHOCUSMUGUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'stable','UVPHOCUSMUGUVP.png'),
    "JMUG11WBUVPPSIGBBJSUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'stable', 'UVPPSIGBBJSUVP.png'),
    "JMUG11WBUVPPSINAMUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'stable', 'UVPPSINAMUVP.png'),
    "JMUG11WBUVPPSJBANHUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'stable','UVPPSJBANHUVP.png'),
    "JMUG11WBUVPPSJCM1UVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'stable', 'UVPPSJCM1UVP.png'),
    "JMUG11WBUVPPSJOEBGUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'stable', 'UVPPSJOEBGUVP.png'),  
    "JMUG11WBUVPPSKIMJMUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'stable','UVPPSKIMJMUVP.png'),
    "JMUG11WBUVPPSLALPUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'stable', 'UVPPSLALPUVP.png'),
    "JMUG11WBUVPPSLAYGASMUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'stable', 'UVPPSLAYGASMUVP.png'),
    "JMUG11WBUVPUVPPSLVSBUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'stable', 'UVPPSLVSBUVP.png'),
    "JMUG11WBUVPPSMACASSMUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'stable','UVPPSMACASSMUVP.png'),
    "JMUG11WBUVPPSMMMBMUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'stable', 'UVPPSMMMBMUVP.png'),
    "JMUG11WBUVPPSMOMBAUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'stable', 'UVPPSMOMBAUVP.png'),
    "JMUG11WBUVPPSNBAHUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'stable','UVPPSNBAHUVP.png'),
    "JMUG11WBUVPPSNCATUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'stable', 'UVPPSNCATUVP.png'),   
    "JMUG11WBUVPPSOKILUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'stable', 'UVPPSOKILUVP.png'), 
    "JMUG11WBUVPPSONEDEGREEUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'stable','UVPPSONEDEGREEUVP.png'),
    "JMUG11WBUVPPSOWACUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'stable', 'UVPPSOWACUVP.png'),
    "JMUG11WBUVPPSPFDKUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'stable', 'UVPPSPFDKUVP.png'),
    "JMUG11WBUVPPSPPLYUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'stable','UVPPSPPLYUVP.png'),
    "JMUG11WBUVPPSPRSWDLUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'stable', 'UVPPSPRSWDLUVP.png'),
    "JMUG11WBUVPPSPRSWDMUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'stable', 'UVPPSPRSWDMUVP.png'),
    "JMUG11WBUVPPSRTTTSMUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'stable','UVPPSRTTTSMUVP.png'),
    "JMUG11WBUVPPSSHITTERSUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'stable', 'UVPPSSHITTERSUVP.png'),
    "JMUG11WBUVPPSSLPCMUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'stable', 'UVPPSSLPCMUVP.png'),
    "JMUG11WBUVPPSSMUGUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'stable','UVPPSSMUGUVP.png'),
    "JMUG11WBUVPPSSTFUUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'stable', 'UVPPSSTFUUVP.png'),
    "JMUG11WBUVPPSSWALLOWUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'stable', 'UVPPSSWALLOWUVP.png'),
    "JMUG11WBUVPPSTDLCMUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'stable','UVPPSTDLCMUVP.png'),
    "JMUG11WBUVPPSTHMDCUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'stable', 'UVPPSTHMDCUVP.png'),
    "JMUG11WBUVPPSTOB1UVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'stable', 'UVPPSTOB1UVP.png'),
    "JMUG11WBUVPPSTOD1UVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'stable','UVPPSTOD1UVP.png'),
    "JMUG11WBUVPPSTOPBMUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'stable', 'UVPPSTOPBMUVP.png'),
    "JMUG11WBUVPPSTWAFUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'stable', 'UVPPSTWAFUVP.png'),   
    "JMUG11WBUVPPSUHOHUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'stable','UVPPSUHOHUVP.png'),
    "JMUG11WBUVPPSVAGMUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'stable', 'UVPPSVAGMUVP.png'),   
    "JMUG11WBUVPPSWGFMUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'stable', 'UVPPSWGFMUVP.png'),   
    "JMUG11WBUVPPSYFACMUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'stable','UVPPSYFACMUVP.png'),
    "JMUG11WBUVPPSYINAPUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'stable', 'UVPPSYINAPUVP.png'),
    "JMUG11WBUVPRACAIMUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'stable', 'UVPRACAIMUVP.png'),
    "JMUG11WBUVPRAPMAGUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'stable','UVPRAPMAGUVP.png'),
    "JMUG11WBUVPRATODPUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'stable', 'UVPRATODPUVP.png'),
    "JMUG11WBUVPRMCMDND5UVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'stable', 'UVPRMCMDND5UVP.png'),
    "JMUG11WBUVPRMCMDND6UVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'stable','UVPRMCMDND6UVP.png'),
    "JMUG11WBUVPROFSUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'stable', 'UVPROFSUVP.png'),
    "JMUG11WBUVPttsmmuUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'stable', 'UVPttsmmuUVP.png'),
    "JMUG11WBUVPPSSWTUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'stable', 'UVPPSSWTUVP.png'),
    "JMUG11WBSUBBOSSUB": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'stable', 'SUBBOSSUB.png'),
    "JMUG11WBUVPJMBFMEUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'stable','UVPJMBFMEUVP.png'),
    "JMUG11WBUVPPSNCATUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'stable', 'UVPPSNCATUVP.png'),
    "JMUG11WBUVPPSOFFSUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'stable', 'UVPPSOFFSUVP.png'),
    "JMUG11WBUVPPSPFDKUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'stable', 'UVPPSPFDKUVP.png'),
    "JMUG11WBUVPJMSHITTERUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'stable', 'UVPJMSHITTERUVP.png'),
    "JMUG11WBUVPPSINAMUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'stable', 'UVPPSINAMUVP.png'),
    "JMUG11WBUVPJMSJSSMUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'stable', 'UVPJMSJSSMUVP.png'),
    "JMUG11WBUVPPSTHCTWUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'stable', 'UVPPSTHCTWUVP.png'),

}

sku_to_font = {

    # customizable
    'JMUG11WBUVPPSLNTBBUVP': os.path.join(script_dir, 'fonts', 'TeXGyre-Termes-Bold.ttf'),
    'JMUG11WBUVPPSICG1UVP': os.path.join(script_dir, 'fonts', 'TeXGyre-Termes-Bold.ttf'),
    'JMUG11WBUVPPSNNCMUVP': os.path.join(script_dir, 'Fonts', 'LibreBaskerville.ttf'),
    'JMUG11WBUVPJMSAYOCMUVP': os.path.join(script_dir, 'fonts', 'AmaticSC-Bold.ttf'),
    'JMUG11WBUVPJMOVMUVP': os.path.join(script_dir, 'fonts', 'MoonTime-Regular.ttf'),
    'JMUG11WBUVPPSFUNCMUVP': os.path.join(script_dir, 'fonts', 'AmaticSC-Bold.ttf'),
    'JMUG11WBUVPJMSAY1KMUVP': os.path.join(script_dir, 'fonts', 'AmaticSC-Bold.ttf'),
    'JMUG11WBUVPPSWIPEUVP': os.path.join(script_dir, 'fonts', 'AmaticSC-Bold.ttf'),
    'JMUG11WBUVPPSMUWRMUVP': os.path.join(script_dir, 'fonts', 'AmaticSC-Bold.ttf'),
    'JMUG11WBUVPPSDUWRMUVP': os.path.join(script_dir, 'fonts', 'AmaticSC-Bold.ttf'),
    'JMUG11WBUVPJMBTOIMUVP': os.path.join(script_dir, 'fonts', 'AmaticSC-Bold.ttf'),
    'JMUG11WBSUBJMSUWOMSUB': os.path.join(script_dir, 'fonts', 'AmaticSC-Bold.ttf'),
    'JMUG11WBUVPPSSPERMMUVP': os.path.join(script_dir, 'fonts', 'AmaticSC-Bold.ttf'), 
    'JMUG11WBUVPPSBONDUVP': os.path.join(script_dir, 'fonts', 'AmaticSC-Bold.ttf'),
    'JMUG11WBSUBUYTHTSUB': os.path.join(script_dir, 'fonts', 'Shorelines Script Bold.ttf'),
    'JMUG11WBUVPJMFMEMUVP': os.path.join(script_dir, 'fonts', 'I Love Glitter.ttf'),
    'JMUG11WBUVPPSYBCMUVP': os.path.join(script_dir, 'fonts', 'AmaticSC-Bold.ttf'),
    'JMUG11WBUVPPSSBFRUVP': os.path.join(script_dir, 'fonts', 'Gabriel_Weiss_Friends.ttf'),
    'JMUG11WBUVPJMCCAS1UVP': os.path.join(script_dir, 'fonts', 'AmaticSC-Regular.ttf'),
    'JMUG11WBUVPJMCCAS2UVP': os.path.join(script_dir, 'fonts', 'AmaticSC-Regular.ttf'),
    'JMUG11WBUVPJMCCAS3UVP': os.path.join(script_dir, 'fonts', 'AmaticSC-Regular.ttf'),
    'JMUG11WBUVPJMCCAS4UVP': os.path.join(script_dir, 'fonts', 'AmaticSC-Regular.ttf'),
    'JMUG11WBUVPJMCCTNR1UVP': os.path.join(script_dir, 'fonts', 'Times New Roman-Regular.ttf'),
    'JMUG11WBUVPJMCCTNR2UVP': os.path.join(script_dir, 'fonts', 'Times New Roman-Regular.ttf'),
    'JMUG11WBUVPJMCCTNR3UVP': os.path.join(script_dir, 'fonts', 'Times New Roman-Regular.ttf'),
    'JMUG11WBUVPJMCCDS1UVP': os.path.join(script_dir, 'fonts', 'DancingScript-Bold.ttf'),
    'JMUG11WBUVPJMCCDS2UVP': os.path.join(script_dir, 'fonts', 'DancingScript-Bold.ttf'),
    'JMUG11WBUVPJMCCDS3UVP': os.path.join(script_dir, 'fonts', 'DancingScript-Bold.ttf'),
    'JMUG11WBUVPPSBALLS2UVP': os.path.join(script_dir, 'fonts', 'Louis George Cafe.ttf'),
    'JMUG11WBUVPCCFREKEX1UVP': os.path.join(script_dir, 'fonts', 'Shorelines Script Bold.ttf'),
    'JMUG11WBUVPPSTYBMUVP': os.path.join(script_dir, 'fonts', 'BebasNeue-Regular.ttf'),
    'JMUG11WBUVPPSSBNALUVP': os.path.join(script_dir, 'fonts', 'TeXGyre-Termes-Bold.ttf'),
    'JMUG11WBUVPPSPFCMUVP': os.path.join(script_dir, 'fonts', 'AmaticSC-Regular.ttf'),
    'JMUG11WBUVPPSLAYBNSMUVP': os.path.join(script_dir, 'fonts', 'BrittanySignature.ttf'),
    'JMUG11WBUVPPSNORMUVP': os.path.join(script_dir, 'fonts', 'BrittanySignature.ttf'),
    'JMUG11WBUVPJMIFLYMUVP': os.path.join(script_dir, 'fonts', 'BrittanySignature.ttf'),
    'JMUG11WBUVPPSSCMUVP': os.path.join(script_dir, 'fonts', 'AmaticSC-Bold.ttf'),
    'JMUG11WBUVPPSGDMNUVP': os.path.join(script_dir, 'fonts', 'AmaticSC-Bold.ttf'),
    'JMUG11WBUVPPSDLGFBMUVP': os.path.join(script_dir, 'fonts', 'AmaticSC-Bold.ttf'),
    'JMUG11WBUVPPSBOBWUVP': os.path.join(script_dir, 'fonts', 'BrittanySignature.ttf'),
    'JMUG11WBUVPPSFARTUVP': os.path.join(script_dir, 'fonts', 'BrittanySignature.ttf'),
    'JMUG11WBUVPJMMCMWLYUVP': os.path.join(script_dir, 'fonts', 'I Love Glitter red_heart.ttf'),
    'JMUG11WBUVPPSIMDAMUVP': os.path.join(script_dir, 'fonts', 'BrittanySignature.ttf'),
    'JMUG11WBUVPPSPSIBUVP': os.path.join(script_dir, 'fonts', 'AmaticSC-Bold.ttf'),
    'JMUG11WBUVPJMRTFTMUVP': os.path.join(script_dir, 'fonts', 'AmaticSC-Bold.ttf'),
    'JMUG11WBUVPPSFAVEUVP': os.path.join(script_dir, 'fonts', 'AmaticSC-Bold.ttf'),
    'JMUG11WBUVPPSUBCNSBUVP': os.path.join(script_dir, 'fonts', 'AmaticSC-Bold.ttf'),
    'JMUG11WBUVPPSNCC1UVP': os.path.join(script_dir, 'fonts', 'BrittanySignature.ttf'),
    'JMUG11WBUVPPSTCMUVP': os.path.join(script_dir, 'fonts', 'BrittanySignature.ttf'),    
    'JMUG11WBUVPPSCRAYMUVP': os.path.join(script_dir, 'fonts', 'BrittanySignature.ttf'),
    'JMUG11WBUVPPSFLONAMEUVP': os.path.join(script_dir, 'fonts', 'PinyonScript-Regular.ttf'),
    'JMUG11WBUVPPSBTEMUVP': os.path.join(script_dir, 'fonts', 'BebasNeue-Regular.ttf'),
    'JMUG11WBUVPPSBFCEUVP': os.path.join(script_dir, 'fonts', 'AmaticSC-Bold.ttf'),
    'JMUG11WBUVPJMFDCM7UVP': os.path.join(script_dir, 'fonts', 'AmaticSC-Bold.ttf'),
    'JMUG11WBUVPPSBMMMUVP': os.path.join(script_dir, 'fonts', 'AmaticSC-Bold.ttf'),

    # fav child
    "JMUG11WBUVPPSFAVCHUVP": os.path.join(script_dir, 'fonts', 'AmaticSC-Regular.ttf'),
    "JMUG11WBUVPPS2FAVCHUVP": os.path.join(script_dir, 'fonts', 'AmaticSC-Regular.ttf'),
    "JMUG11WBUVPPS3FAVCHUVP": os.path.join(script_dir, 'fonts', 'AmaticSC-Regular.ttf'),
    "JMUG11WBUVPPS4FAVCHUVP": os.path.join(script_dir, 'fonts', 'AmaticSC-Regular.ttf'),

    
    # christmas
    'JMUG11WBUVPPSCMSMUVP': os.path.join(script_dir, 'fonts', 'Farmer Market Regular.ttf'),
    'JMUG11WBUVPPSCMSRUVP': os.path.join(script_dir, 'fonts', 'Farmer Market Regular.ttf'),
    'JMUG11WBUVPPSCMGRUVP': os.path.join(script_dir, 'fonts', 'Farmer Market Regular.ttf'),
    'JMUG11WBUVPCCKHCSMUVP': os.path.join(script_dir, 'fonts', 'Blueberry.ttf'),

    # Little Miss
    "JMUG11WBUVPPSLILMSUVP": os.path.join(script_dir, 'fonts', 'BebasNeue-Regular.ttf'),
    "JMUG11WBUVPPSLILMGUVP": os.path.join(script_dir, 'fonts', 'BebasNeue-Regular.ttf'),
    "JMUG11WBUVPPSLILMPUVP": os.path.join(script_dir, 'fonts', 'BebasNeue-Regular.ttf'),

}

sku_to_second_line_font = { 

    # customizable
    'JMUG11WBUVPPSLNTBBUVP': os.path.join(script_dir, 'fonts', 'BrittanySignature.ttf'),
    'JMUG11WBUVPPSICG1UVP': os.path.join(script_dir, 'fonts', 'AmaticSC-Bold.ttf'),
    'JMUG11WBUVPPSNNCMUVP': os.path.join(script_dir, 'fonts', 'BrittanySignature.ttf'),
    'JMUG11WBUVPPSTYBMUVP': os.path.join(script_dir, 'fonts', 'BebasNeue-Regular.ttf'),
    'JMUG11WBUVPPSSBNALUVP': os.path.join(script_dir, 'fonts', 'BrittanySignature.ttf'),
    'JMUG11WBUVPJMRTFTMUVP': os.path.join(script_dir, 'fonts', 'BebasNeue-Regular.ttf'),
    'JMUG11WBUVPPSTCMUVP': os.path.join(script_dir, 'fonts', 'BebasNeue-Regular.ttf'),
    'JMUG11WBUVPPSCRAYMUVP': os.path.join(script_dir, 'fonts', 'BebasNeue-Regular.ttf'),
}

sku_to_third_line_font = { 

    # customizable
    'JMUG11WBUVPPSNNCMUVP': os.path.join(script_dir, 'fonts', 'LibreBaskerville.ttf'),
    
}

sku_to_fontsize_placement = {  # (font-size, x, y)  

    # customizable
    'JMUG11WBUVPPSLNTBBUVP': {     
         1: (600, 50),
    },
    'JMUG11WBUVPPSICG1UVP': {     
         1: (600, 50),
    },
    'JMUG11WBUVPPSNNCMUVP': {     
         1: (500, 0),
    },
    'JMUG11WBUVPJMSAYOCMUVP': {     
         1: (90, 330, 590),  2: (90, 330, 590), 3: (90, 330, 590),  4: (90, 330, 590),  5: (90, 330, 590),  
         6: (90, 330, 590),  7: (90, 330, 590),  8: (90, 330, 590),  9: (90, 330, 590), 10: (80, 330, 590),  
        11: (80, 330, 590), 12: (80, 330, 590), 13: (80, 330, 590), 14: (60, 330, 580), 15: (60, 330, 580), 
        16: (60, 330, 580), 17: (60, 330, 580), 18: (40, 330, 570), 19: (40, 330, 570), 20: (40, 330, 570),
    },
    'JMUG11WBUVPJMSAY1KMUVP': {     
         1: (90, 330, 590),  2: (90, 330, 590), 3: (90, 330, 590),  4: (90, 330, 590),  5: (90, 330, 590),  
         6: (90, 330, 590),  7: (90, 330, 590),  8: (90, 330, 590),  9: (90, 330, 590), 10: (80, 330, 590),  
        11: (80, 330, 590), 12: (80, 330, 590), 13: (80, 330, 590), 14: (60, 330, 580), 15: (60, 330, 580), 
        16: (60, 330, 580), 17: (60, 330, 580), 18: (40, 330, 570), 19: (40, 330, 570), 20: (40, 330, 570),
    },
    'JMUG11WBUVPJMOVMUVP': {     
         1: (90, 280, 560),  2: (90, 280, 560), 3: (90, 280, 560),  4: (90, 280, 560),  5: (90, 280, 560),  
         6: (90, 280, 560),  7: (90, 280, 560),  8: (90, 280, 560),  9: (90, 280, 560), 10: (80, 280, 560),  
        11: (80, 280, 560), 12: (80, 280, 560), 13: (80, 280, 560), 14: (60, 280, 560), 15: (60, 280, 560), 
        16: (60, 280, 560), 17: (60, 280, 560), 18: (40, 280, 560), 19: (40, 280, 560), 20: (40, 280, 560),
    },
    'JMUG11WBUVPPSFUNCMUVP': {     
         1: (100, 280, 510),  2: (100, 280, 510), 3: (100, 280, 510),  4: (100, 280, 510),  5: (100, 280, 510),  
         6: (100, 280, 510),  7: (100, 280, 510),  8: (100, 280, 510),  9: (100, 280, 510), 10: (90, 280, 510),  
        11: (90, 280, 510), 12: (90, 280, 510), 13: (90, 280, 510), 14: (70, 280, 500), 15: (70, 280, 500), 
        16: (70, 280, 500), 17: (70, 280, 500), 18: (50, 280, 490), 19: (50, 280, 490), 20: (50, 280, 490),
    },
    'JMUG11WBUVPPSWIPEUVP': {     
         1: (90, 330, 590),  2: (90, 330, 590), 3: (90, 330, 590),  4: (90, 330, 590),  5: (90, 330, 590),  
         6: (90, 330, 590),  7: (90, 330, 590),  8: (90, 330, 590),  9: (90, 330, 590), 10: (80, 330, 590),  
        11: (80, 330, 590), 12: (80, 330, 590), 13: (80, 330, 590), 14: (60, 330, 580), 15: (60, 330, 580), 
        16: (60, 330, 580), 17: (60, 330, 580), 18: (40, 330, 570), 19: (40, 330, 570), 20: (40, 330, 570),
    },
    'JMUG11WBUVPPSMUWRMUVP': {     
         1: (90, 330, 590),  2: (90, 330, 590), 3: (90, 330, 590),  4: (90, 330, 590),  5: (90, 330, 590),  
         6: (90, 330, 590),  7: (90, 330, 590),  8: (90, 330, 590),  9: (90, 330, 590), 10: (80, 330, 590),  
        11: (80, 330, 590), 12: (80, 330, 590), 13: (80, 330, 590), 14: (60, 330, 580), 15: (60, 330, 580), 
        16: (60, 330, 580), 17: (60, 330, 580), 18: (40, 330, 570), 19: (40, 330, 570), 20: (40, 330, 570),
    },
    'JMUG11WBUVPPSDUWRMUVP': {     
         1: (90, 330, 590),  2: (90, 330, 590), 3: (90, 330, 590),  4: (90, 330, 590),  5: (90, 330, 590),  
         6: (90, 330, 590),  7: (90, 330, 590),  8: (90, 330, 590),  9: (90, 330, 590), 10: (80, 330, 590),  
        11: (80, 330, 590), 12: (80, 330, 590), 13: (80, 330, 590), 14: (60, 330, 580), 15: (60, 330, 580), 
        16: (60, 330, 580), 17: (60, 330, 580), 18: (40, 330, 570), 19: (40, 330, 570), 20: (40, 330, 570),
    },
    'JMUG11WBUVPJMBTOIMUVP': {     
         1: (90, 330, 590),  2: (90, 330, 590), 3: (90, 330, 590),  4: (90, 330, 590),  5: (90, 330, 590),  
         6: (90, 330, 590),  7: (90, 330, 590),  8: (90, 330, 590),  9: (90, 330, 590), 10: (80, 330, 590),  
        11: (80, 330, 590), 12: (80, 330, 590), 13: (80, 330, 590), 14: (60, 330, 580), 15: (60, 330, 580), 
        16: (60, 330, 580), 17: (60, 330, 580), 18: (40, 330, 570), 19: (40, 330, 570), 20: (40, 330, 570),
    },
    'JMUG11WBSUBJMSUWOMSUB': {     
         1: (90, 330, 590),  2: (90, 330, 590), 3: (90, 330, 590),  4: (90, 330, 590),  5: (90, 330, 590),  
         6: (90, 330, 590),  7: (90, 330, 590),  8: (90, 330, 590),  9: (90, 330, 590), 10: (80, 330, 590),  
        11: (80, 330, 590), 12: (80, 330, 590), 13: (80, 330, 590), 14: (60, 330, 580), 15: (60, 330, 580), 
        16: (60, 330, 580), 17: (60, 330, 580), 18: (40, 330, 570), 19: (40, 330, 570), 20: (40, 330, 570),
    },
    'JMUG11WBUVPPSSPERMMUVP': {     
         1: (90, 330, 590),  2: (90, 330, 590), 3: (90, 330, 590),  4: (90, 330, 590),  5: (90, 330, 590),  
         6: (90, 330, 590),  7: (90, 330, 590),  8: (90, 330, 590),  9: (90, 330, 590), 10: (80, 330, 590),  
        11: (80, 330, 590), 12: (80, 330, 590), 13: (80, 330, 590), 14: (60, 330, 580), 15: (60, 330, 580), 
        16: (60, 330, 580), 17: (60, 330, 580), 18: (40, 330, 570), 19: (40, 330, 570), 20: (40, 330, 570),
    },
    'JMUG11WBUVPPSBONDUVP': {     
         1: (90, 330, 590),  2: (90, 330, 590), 3: (90, 330, 590),  4: (90, 330, 590),  5: (90, 330, 590),  
         6: (90, 330, 590),  7: (90, 330, 590),  8: (90, 330, 590),  9: (90, 330, 590), 10: (80, 330, 590),  
        11: (80, 330, 590), 12: (80, 330, 590), 13: (80, 330, 590), 14: (60, 330, 580), 15: (60, 330, 580), 
        16: (60, 330, 580), 17: (60, 330, 580), 18: (40, 330, 570), 19: (40, 330, 570), 20: (40, 330, 570),
    },
    'JMUG11WBSUBUYTHTSUB': {     
         1: (60, 520),  2: (60, 520),  3: (60, 520),  4: (60, 520),  5: (60, 520),  
         6: (60, 520),  7: (60, 520),  8: (60, 520),  9: (60, 520), 10: (60, 520),  
        11: (60, 520), 12: (60, 520), 13: (60, 520), 14: (50, 530), 15: (50, 530), 
        16: (50, 530), 17: (50, 530), 18: (50, 530), 19: (40, 540), 20: (40, 540),
    },
    'JMUG11WBUVPJMFMEMUVP': {     
         1: (100, 200, 570),  2: (100, 200, 570),  3: (100, 200, 570),  4: (100, 200, 570),  5: (100, 200, 570),  
         6: (100, 150, 570),  7: (100, 150, 570),  8: (100, 150, 570),  9: (100, 150, 570), 10: (100, 150, 570),  
        11: (100, 100, 570), 12: (100, 100, 570), 13: (100, 100, 570), 14: (90, 100, 580), 15: (90, 100, 580), 
        16: (90, 50, 580), 17: (90, 50, 580), 18: (90, 50, 580), 19: (80, 50, 590), 20: (80, 50, 590),
    },
    'JMUG11WBUVPPSYBCMUVP': {     
         1: (180, 480),  2: (180, 480),  3: (180, 480),  4: (180, 480),  5: (180, 480),  
         6: (180, 480),  7: (180, 480),  8: (150, 500),  9: (150, 500), 10: (150, 500),  
        11: (130, 520), 12: (130, 520), 13: (130, 520), 14: (100, 530), 15: (100, 530), 
        16: (100, 530), 17: (90, 530),  18: (90, 530),  19: (80, 530),  20: (80, 530),
        21: (70, 530),  22: (70, 530),  23: (70, 530),  24: (60, 540),  25: (60, 540),
    },
    'JMUG11WBUVPPSSBFRUVP': {     
         1: (85, 330),  2: (85, 330),  3: (85, 330),  4: (85, 330),  5: (85, 330),  
         6: (85, 330),  7: (85, 330),  8: (85, 330),  9: (85, 330), 10: (85, 330),  
        11: (85, 330), 12: (85, 330), 13: (85, 330), 14: (85, 330), 15: (85, 330), 
        16: (70, 340), 17: (70, 340), 18: (70, 340), 19: (70, 340), 20: (70, 340),
        21: (60, 350), 22: (60, 350), 23: (60, 350), 24: (50, 360), 25: (50, 360),
    },
    'JMUG11WBUVPJMCCAS1UVP': {   
         1: (300, 250),  2: (280, 250),  3: (280, 250),  4: (260, 250),  5: (260, 250),  
         6: (260, 250),  7: (240, 250),  8: (220, 250),  9: (200, 260), 10: (180, 260),       
        11: (150, 270), 12: (140, 270), 13: (130, 280), 14: (120, 300), 15: (110, 320), 
        16: (110, 320), 17: (100, 330), 18: (100, 340), 19: (90, 350),  20: (80, 360),
    },
    'JMUG11WBUVPJMCCAS2UVP': {     
         1: (300, 150),  2: (300, 150),  3: (280, 150),  4: (260, 150),  5: (260, 150),  
         6: (260, 150),  7: (240, 150),  8: (220, 150),  9: (200, 160), 10: (180, 160),       
        11: (150, 160), 12: (140, 160), 13: (130, 170), 14: (120, 170), 15: (110, 170), 
        16: (110, 170), 17: (100, 170), 18: (100, 170), 19: (90, 170),  20: (80, 170),
        21: (80, 180),  22: (80, 180),  23: (80, 180),  24: (80, 180),  25: (80, 180), 
        26: (70, 180),  27: (70, 180),  28: (60, 180),  29: (55, 180),  30: (50, 180), 
        31: (50, 180),  32: (40, 190),  33: (40, 190),  34: (30, 190),  35: (30, 190),
    },
    'JMUG11WBUVPJMCCAS3UVP': {     
         1: (300, 50),  2: (300, 50),  3: (280, 50),  4: (260, 50),  5: (260, 50),  
         6: (260, 50),  7: (240, 50),  8: (220, 50),  9: (200, 60), 10: (180, 60),       
        11: (150, 60), 12: (140, 60), 13: (130, 70), 14: (120, 70), 15: (110, 70), 
        16: (110, 70), 17: (100, 70), 18: (100, 70), 19: (90, 70),  20: (80, 70),
        21: (80, 80),  22: (80, 80),  23: (80, 80),  24: (80, 80),  25: (80, 80), 
        26: (70, 80),  27: (70, 80),  28: (60, 80),  29: (55, 80),  30: (50, 80), 
        31: (50, 80),  32: (40, 90),  33: (40, 90),  34: (30, 90),  35: (30, 90),
    },
    'JMUG11WBUVPJMCCAS4UVP': {     
         1: (300, 50),  2: (300, 50),  3: (280, 50),  4: (260, 50),  5: (260, 50),  
         6: (260, 50),  7: (240, 50),  8: (220, 50),  9: (200, 60), 10: (180, 60),       
        11: (150, 60), 12: (140, 60), 13: (130, 70), 14: (120, 70), 15: (110, 70), 
        16: (110, 70), 17: (100, 70), 18: (100, 70), 19: (90, 70),  20: (80, 70),
        21: (80, 80),  22: (80, 80),  23: (80, 80),  24: (80, 80),  25: (80, 80), 
        26: (70, 80),  27: (70, 80),  28: (60, 80),  29: (55, 80),  30: (50, 80), 
        31: (50, 80),  32: (40, 90),  33: (40, 90),  34: (30, 90),  35: (30, 90),
    },
    'JMUG11WBUVPJMCCTNR1UVP': {
         1: (150, 250),   2: (150, 250),   3: (150, 250),   4: (150, 250),   5: (150, 250),  
         6: (150, 250),   7: (140, 255),   8: (140, 255),   9: (130, 260),  10: (130, 260),       
        11: (120, 260), 12: (110, 260), 13: (100, 270), 14: (100, 270), 15: (90, 270), 
        16: (80, 280), 17: (80, 280), 18: (70, 285), 19: (70, 285), 20: (60, 290),
        21: (60, 290), 22: (60, 290), 23: (50, 295), 24: (50, 295), 25: (50, 295), 
        26: (50, 295), 27: (50, 295), 28: (40, 300), 29: (40, 300), 30: (40, 300), 
        31: (40, 300), 32: (40, 300), 33: (40, 300), 34: (40, 300), 35: (40, 300),
    },
    'JMUG11WBUVPJMCCDS1UVP': { 
         1: (150, 250),   2: (150, 250),   3: (150, 250),   4: (150, 250),   5: (150, 250),  
         6: (150, 250),   7: (140, 255),   8: (140, 255),   9: (130, 260),  10: (130, 260),       
        11: (120, 260), 12: (110, 260), 13: (100, 270), 14: (100, 270), 15: (90, 270), 
        16: (80, 280), 17: (80, 280), 18: (70, 285), 19: (70, 285), 20: (60, 290),
        21: (60, 290), 22: (60, 290), 23: (50, 295), 24: (50, 295), 25: (50, 295), 
        26: (50, 295), 27: (50, 295), 28: (40, 300), 29: (40, 300), 30: (40, 300), 
        31: (40, 300), 32: (40, 300), 33: (40, 300), 34: (40, 300), 35: (40, 300),
    },
    'JMUG11WBUVPJMCCTNR2UVP': {     
         1: (150, 150),   2: (150, 150),   3: (150, 150),   4: (150, 150),   5: (150, 150),  
         6: (150, 150),   7: (150, 150),   8: (150, 150),   9: (130, 160),  10: (130, 160),       
        11: (130, 160), 12: (130, 160), 13: (110, 170), 14: (110, 170), 15: (110, 170), 
        16: (110, 170), 17: (100, 170), 18: (100, 170), 19: (100, 170), 20: (100, 170),
        21: (80, 180), 22: (80, 180), 23: (80, 180), 24: (80, 180), 25: (80, 180), 
        26: (70, 180), 27: (70, 180), 28: (60, 180), 29: (55, 180), 30: (50, 180), 
        31: (50, 180), 32: (40, 190), 33: (40, 190), 34: (30, 190), 35: (30, 190),
    },
    'JMUG11WBUVPJMCCTNR3UVP': {
         1: (150, 50),   2: (150, 50),   3: (150, 50),   4: (150, 50),   5: (150, 50),  
         6: (150, 50),   7: (150, 50),   8: (150, 50),   9: (130, 60),  10: (130, 60),       
        11: (130, 60), 12: (130, 60), 13: (110, 70), 14: (110, 70), 15: (110, 70), 
        16: (110, 70), 17: (100, 70), 18: (100, 70), 19: (100, 70), 20: (100, 70),
        21: (80, 80), 22: (80, 80), 23: (80, 80), 24: (80, 80), 25: (80, 80), 
        26: (70, 80), 27: (70, 80), 28: (60, 80), 29: (55, 80), 30: (50, 80), 
        31: (50, 80), 32: (40, 90), 33: (40, 90), 34: (30, 90), 35: (30, 90),
    },
    'JMUG11WBUVPJMCCDS1UVP': { 
         1: (150, 250),   2: (150, 250),   3: (150, 250),   4: (150, 250),   5: (150, 250),  
         6: (150, 250),   7: (140, 255),   8: (140, 255),   9: (130, 260),  10: (130, 260),       
        11: (120, 260), 12: (110, 260), 13: (100, 270), 14: (100, 270), 15: (90, 270), 
        16: (80, 280), 17: (80, 280), 18: (70, 285), 19: (70, 285), 20: (60, 290),
        21: (60, 290), 22: (60, 290), 23: (50, 295), 24: (50, 295), 25: (50, 295), 
        26: (50, 295), 27: (50, 295), 28: (40, 300), 29: (40, 300), 30: (40, 300), 
        31: (40, 300), 32: (40, 300), 33: (40, 300), 34: (40, 300), 35: (40, 300),
    },
    'JMUG11WBUVPJMCCDS2UVP': {     
         1: (150, 150),   2: (150, 150),   3: (150, 150),   4: (150, 150),   5: (150, 150),  
         6: (150, 150),   7: (150, 150),   8: (150, 150),   9: (130, 160),  10: (130, 160),       
        11: (130, 160), 12: (130, 160), 13: (110, 170), 14: (110, 170), 15: (110, 170), 
        16: (110, 170), 17: (100, 170), 18: (100, 170), 19: (100, 170), 20: (100, 170),
        21: (80, 180), 22: (80, 180), 23: (80, 180), 24: (80, 180), 25: (80, 180), 
        26: (70, 180), 27: (70, 180), 28: (60, 180), 29: (55, 180), 30: (50, 180), 
        31: (50, 180), 32: (40, 190), 33: (40, 190), 34: (30, 190), 35: (30, 190),
    },
    'JMUG11WBUVPJMCCDS3UVP': {
         1: (150, 50),   2: (150, 50),   3: (150, 50),   4: (150, 50),   5: (150, 50),  
         6: (150, 50),   7: (150, 50),   8: (150, 50),   9: (130, 60),  10: (130, 60),       
        11: (130, 60), 12: (130, 60), 13: (110, 70), 14: (110, 70), 15: (110, 70), 
        16: (110, 70), 17: (100, 70), 18: (100, 70), 19: (100, 70), 20: (100, 70),
        21: (80, 80), 22: (80, 80), 23: (80, 80), 24: (80, 80), 25: (80, 80), 
        26: (70, 80), 27: (70, 80), 28: (60, 80), 29: (55, 80), 30: (50, 80), 
        31: (50, 80), 32: (40, 90), 33: (40, 90), 34: (30, 90), 35: (30, 90),
    },
    'JMUG11WBUVPPSBALLS2UVP': {     
         1: (70, 600),  2: (70, 600),  3: (70, 600),  4: (70, 600),  5: (70, 600),  
         6: (70, 600),  7: (70, 600),  8: (70, 600),  9: (70, 600), 10: (70, 600),  
        11: (70, 600), 12: (70, 600), 13: (70, 600), 14: (70, 600), 15: (70, 600), 
        16: (55, 610), 17: (55, 610), 18: (55, 610), 19: (55, 610), 20: (55, 610),
        21: (45, 620), 22: (45, 620), 23: (45, 620), 24: (35, 630), 25: (35, 630),
    },
    'JMUG11WBUVPCCFREKEX1UVP': {     
         1: (60, 550),  2: (60, 550),  3: (60, 550),  4: (80, 550),  5: (60, 550),  
         6: (60, 550),  7: (60, 550),  8: (60, 550),  9: (60, 550), 10: (60, 550),  
        11: (60, 550), 12: (60, 550), 13: (60, 550), 14: (50, 560), 15: (50, 560), 
        16: (50, 560), 17: (50, 560), 18: (50, 560), 19: (40, 570), 20: (40, 570),
    },
    'JMUG11WBUVPPSTYBMUVP': {     
         1: (50, 300, 320),  2: (50, 300, 320),  3: (50, 300, 320),  4: (50, 300, 320),  5: (50, 300, 320),  
         6: (50, 300, 320),  7: (40, 300, 320),  8: (40, 300, 320),  9: (30, 300, 330), 10: (30, 300, 320),  
        11: (25, 300, 330), 12: (25, 300, 330), 13: (25, 300, 330), 14: (20, 300, 335), 15: (20, 300, 325), 
    },
    'JMUG11WBUVPPSSBNALUVP': {     
         1: (400, 50),
    },
    'JMUG11WBUVPPSPFCMUVP': {     
         1: (90, 610),  2: (90, 610), 3: (90, 610),  4: (90, 610),  5: (90, 610),  
         6: (90, 610),  7: (90, 610),  8: (90, 610),  9: (90, 610), 10: (80, 610),  
        11: (80, 610), 12: (80, 610), 13: (80, 610), 14: (60, 600), 15: (60, 600), 
        16: (60, 600), 17: (60, 600), 18: (40, 600), 19: (60, 600), 20: (60, 600),
        21: (40, 600), 22: (40, 600), 23: (40, 600), 24: (40, 600), 25: (40, 600),
    },
    'JMUG11WBUVPPSLAYBNSMUVP': {
         1: (90, 550),  2: (90, 550), 3: (90, 550),  4: (90, 550),  5: (90, 550),  
         6: (90, 550),  7: (90, 550),  8: (90, 550),  9: (90, 550), 10: (70, 550),  
        11: (70, 550), 12: (70, 550), 13: (70, 550), 14: (70, 560), 15: (70, 560), 
        16: (70, 560), 17: (70, 560), 18: (70, 560), 19: (70, 560), 20: (50, 560),
        21: (50, 560), 22: (50, 560), 23: (50, 560), 24: (40, 560), 25: (40, 560),
    },
    'JMUG11WBUVPPSNORMUVP': {     
         1: (80, 330, 590),  2: (80, 330, 590), 3: (80, 330, 590),  4: (80, 330, 590),  5: (80, 330, 590),  
         6: (80, 330, 590),  7: (80, 330, 590),  8: (80, 330, 590),  9: (80, 330, 590), 10: (70, 330, 590),  
        11: (70, 330, 590), 12: (70, 330, 590), 13: (70, 330, 590), 14: (50, 330, 580), 15: (50, 330, 580), 
        16: (50, 330, 580), 17: (50, 330, 580), 18: (30, 330, 570), 19: (30, 330, 570), 20: (30, 330, 570),
    },
    'JMUG11WBUVPJMIFLYMUVP': {
         1: (70, 590),  2: (70, 590), 3: (70, 590),  4: (70, 590),  5: (70, 590),  
         6: (70, 590),  7: (70, 590),  8: (70, 590),  9: (70, 590), 10: (70, 590),  
        11: (70, 590), 12: (70, 590), 13: (60, 590), 14: (60, 600), 15: (60, 600), 
        16: (60, 600), 17: (60, 600), 18: (60, 600), 19: (60, 600), 20: (40, 600),
        21: (40, 600), 22: (40, 600), 23: (40, 600), 24: (30, 600), 25: (30, 600),
    },
    'JMUG11WBUVPPSSCMUVP': {     
         1: (90, 590),  2: (90, 590), 3: (90, 590),  4: (90, 590),  5: (90, 590),  
         6: (90, 590),  7: (90, 590),  8: (90, 590),  9: (90, 590), 10: (80, 590),  
        11: (80, 590), 12: (80, 590), 13: (80, 590), 14: (60, 580), 15: (60, 580), 
        16: (60, 580), 17: (60, 580), 18: (40, 570), 19: (40, 570), 20: (40, 570),
    },
    'JMUG11WBUVPPSGDMNUVP': {
         1: (90, 590),  2: (90, 590), 3: (90, 590),  4: (90, 590),  5: (90, 590),  
         6: (90, 590),  7: (90, 590),  8: (90, 590),  9: (90, 590), 10: (90, 590),  
        11: (90, 590), 12: (90, 590), 13: (70, 590), 14: (70, 600), 15: (70, 600), 
        16: (70, 600), 17: (70, 600), 18: (70, 600), 19: (70, 600), 20: (50, 600),
        21: (50, 600), 22: (50, 600), 23: (50, 600), 24: (40, 600), 25: (40, 600),
    },
    'JMUG11WBUVPPSDLGFBMUVP': {     
         1: (90, 330, 590),  2: (90, 330, 590), 3: (90, 330, 590),  4: (90, 330, 590),  5: (90, 330, 590),  
         6: (90, 330, 590),  7: (90, 330, 590),  8: (90, 330, 590),  9: (90, 330, 590), 10: (80, 330, 590),  
        11: (80, 330, 590), 12: (80, 330, 590), 13: (80, 330, 590), 14: (60, 330, 580), 15: (60, 330, 580), 
        16: (60, 330, 580), 17: (60, 330, 580), 18: (40, 330, 570), 19: (40, 330, 570), 20: (40, 330, 570),
    },
    'JMUG11WBUVPPSBOBWUVP': {     
         1: (90, 330, 590),  2: (90, 330, 590), 3: (90, 330, 590),  4: (90, 330, 590),  5: (90, 330, 590),  
         6: (90, 330, 590),  7: (90, 330, 590),  8: (90, 330, 590),  9: (90, 330, 590), 10: (80, 330, 590),  
        11: (80, 330, 590), 12: (80, 330, 590), 13: (80, 330, 590), 14: (60, 330, 580), 15: (60, 330, 580), 
        16: (60, 330, 580), 17: (60, 330, 580), 18: (40, 330, 570), 19: (40, 330, 570), 20: (40, 330, 570),
    },
    'JMUG11WBUVPPSFARTUVP': {
         1: (60, 590),  2: (60, 590),  3: (60, 590),  4: (60, 590),  5: (60, 590),  
         6: (60, 590),  7: (60, 590),  8: (60, 590),  9: (60, 590), 10: (60, 590),  
        11: (60, 590), 12: (60, 590), 13: (50, 590), 14: (50, 600), 15: (50, 600), 
        16: (50, 600), 17: (50, 600), 18: (50, 600), 19: (50, 600), 20: (30, 600),
        21: (30, 600), 22: (30, 600), 23: (30, 600), 24: (20, 600), 25: (20, 600),
    },
    'JMUG11WBUVPPSFAVEUVP': {
         1: (180, 1, 40),   2: (180, 1, 40),   3: (180, 1, 40),   4: (180, 1, 40),   5: (180, 1, 40),  
         6: (180, 1, 40),   7: (180, 1, 40),   8: (180, 1, 40),   9: (180, 1, 40),  10: (180, 1, 40),   
        11: (180, 1, 40),  12: (180, 1, 40),  13: (180, 1, 40),  14: (180, 1, 40),  15: (180, 1, 40),  
        16: (180, 1, 40),  17: (180, 1, 40),  18: (180, 1, 40),  19: (180, 1, 40),  20: (180, 1, 40), 
        21: (180, 1, 40),  22: (180, 1, 40),  23: (180, 1, 40),  24: (180, 1, 40),  25: (180, 1, 40), 
    },
    'JMUG11WBUVPPSUBCNSBUVP': {
         1: (120, 355),  2: (120, 355),  3: (120, 355),  4: (120, 355),  5: (120, 355),  
         6: (120, 355),  7: (120, 355),  8: (120, 355),  9: (120, 355), 10: (120, 355),  
        11: (120, 355), 12: (120, 355), 13: (120, 355), 14: (120, 355), 15: (120, 355), 
        16: (120, 355), 17: (120, 355), 18: (120, 355), 19: (120, 355), 20: (120, 355),
        21: (120, 355), 22: (120, 355), 23: (120, 355), 24: (120, 355), 25: (120, 355),
    },
    'JMUG11WBUVPPSNCC1UVP': {
         1: (110, 220),  2: (110, 220), 3: (110, 220),  4: (110, 220),  5: (110, 220),  
         6: (110, 220),  7: (110, 220),  8: (110, 220),  9: (100, 220), 10: (100, 220),  
        11: (100, 220), 12: (90, 220), 13: (90, 220), 14: (90, 220), 15: (90, 220), 
        16: (80, 230), 17: (80, 230), 18: (70, 230), 19: (70, 230), 20: (60, 240),
        21: (60, 240), 22: (60, 240), 23: (60, 240), 24: (40, 240), 25: (40, 240),
    },
    'JMUG11WBUVPPSTCMUVP': {
         1: (110, 100),  2: (110, 100), 3: (110, 100),  4: (110, 100),  5: (110, 100),  
         6: (110, 100),  7: (110, 100),  8: (110, 100),  9: (100, 100), 10: (100, 100),  
        11: (100, 100), 12: (90, 100), 13: (90, 100), 14: (90, 100), 15: (90, 100), 
        16: (80, 110), 17: (80, 110), 18: (70, 110), 19: (70, 110), 20: (60, 120),
        21: (60, 120), 22: (60, 120), 23: (60, 120), 24: (40, 120), 25: (40, 120),
    },
    'JMUG11WBUVPPSCRAYMUVP': {
         1: (110, 100),  2: (110, 100), 3: (110, 100),  4: (110, 100),  5: (110, 100),  
         6: (110, 100),  7: (110, 100),  8: (110, 100),  9: (100, 100), 10: (100, 100),  
        11: (100, 100), 12: (90, 100), 13: (90, 100), 14: (90, 100), 15: (90, 100), 
        16: (80, 110), 17: (80, 110), 18: (70, 110), 19: (70, 110), 20: (60, 120),
        21: (60, 120), 22: (60, 120), 23: (60, 120), 24: (40, 120), 25: (40, 120),
    },
    'JMUG11WBUVPPSFLONAMEUVP': {
         1: (130, 200),  2: (130, 200), 3: (130, 200),  4: (130, 200),  5: (130, 200),  
         6: (130, 200),  7: (130, 200),  8: (130, 200),  9: (120, 200), 10: (120, 200),  
        11: (120, 200), 12: (110, 200), 13: (110, 200), 14: (110, 200), 15: (110, 200), 
        16: (100, 210), 17: (100, 210), 18: (90, 210), 19: (90, 210), 20: (80, 220),
        21: (80, 220), 22: (80, 220), 23: (80, 220), 24: (60, 220), 25: (60, 220),
    },
    'JMUG11WBUVPPSBTEMUVP': {
         1: (110, 520),  2: (110, 520),  3: (110, 520), 4: (110, 520),  5: (110, 520),  
         6: (110, 520),  7: (110, 520),  8: (110, 520), 9: (100, 520), 10: (100, 520),  
        11: (100, 520), 12: (90, 520),  13: (90, 520), 14: (90, 520),  15: (90, 520), 
        16: (80, 520),  17: (80, 520),  18: (70, 520), 19: (70, 520),  20: (60, 520),
        21: (60, 520),  22: (60, 520),  23: (60, 520), 24: (40, 520),  25: (40, 520),
    },
    'JMUG11WBUVPPSBFCEUVP': {
         1: (150, 340),  2: (150, 340),  3: (150, 340),  4: (150, 340),  5: (150, 340),  
         6: (150, 340),  7: (150, 340),  8: (150, 340),  9: (140, 340), 10: (140, 340),  
        11: (140, 340), 12: (130, 340), 13: (130, 340), 14: (130, 340), 15: (130, 340), 
        16: (120, 350), 17: (120, 350), 18: (110, 350), 19: (110, 350), 20: (100, 360),
        21: (100, 360), 22: (100, 360), 23: (100, 360), 24: (80, 360),  25: (80, 360),
    },

    # fav child
    'JMUG11WBUVPPSFAVCHUVP': {     
         1: (175, 110),  2: (175, 110),  3: (175, 110),  4: (175, 110),  5: (175, 110),  
         6: (175, 110),  7: (175, 110),  8: (175, 110),  9: (175, 110), 10: (155, 120),  
        11: (155, 120), 12: (125, 140), 13: (125, 140), 14: (100, 150), 15: (100, 150), 
    },
    'JMUG11WBUVPPS2FAVCHUVP': { 
         1: (150, 70),  2: (150, 70), 3: (150, 70), 4: (150, 70),  5: (150, 70),  
         6: (150, 70),  7: (150, 70), 8: (150, 70), 9: (150, 70), 10: (140, 80),  
        11: (130, 80), 12: (130, 80), 13: (100, 100), 14: (90, 110),  15: (90, 110), 
    },
    'JMUG11WBUVPPS3FAVCHUVP': {     
         1: (130, 60),  2: (130, 60),  3: (130, 60),  4: (130, 60),  5: (130, 60),  
         6: (130, 60),  7: (130, 60),  8: (130, 60),  9: (130, 60), 10: (130, 60),  
        11: (120, 60), 12: (120, 60), 13: (120, 60), 14: (120, 60), 15: (120, 60), 
    },
    'JMUG11WBUVPPS4FAVCHUVP': {     
         1: (100, 80), 2: (100, 80), 3: (100, 80), 4: (100, 80),  5: (100, 80),  
         6: (100, 80), 7: (100, 80), 8: (100, 80), 9: (100, 80), 10: (100, 80),  
        11: (90, 80), 12: (90, 80), 13: (90, 80), 14: (80, 85),  15: (80, 85), 
    },
    'JMUG11WBUVPJMFDCM7UVP': {     
         1: (90, 200, 595),  2: (90, 200, 595), 3: (90, 200, 595),  4: (90, 200, 595),  5: (90, 200, 595),  
         6: (90, 200, 595),  7: (90, 200, 595),  8: (90, 200, 595),  9: (90, 200, 595), 10: (80, 200, 595),  
        11: (80, 200, 595), 12: (80, 200, 595), 13: (80, 200, 595), 14: (70, 165, 545), 15: (70, 185, 605), 
        16: (65, 185, 605), 17: (65, 185, 605), 18: (65, 185, 605), 19: (60, 185, 605), 20: (60, 185, 605),
    },
    'JMUG11WBUVPPSBMMMUVP': {     
         1: (90, 200, 590),  2: (90, 200, 590), 3: (90, 200, 590),  4: (90, 200, 590),  5: (90, 200, 590),  
         6: (90, 200, 590),  7: (90, 200, 590),  8: (90, 200, 590),  9: (90, 200, 590), 10: (80, 200, 590),  
        11: (80, 200, 590), 12: (80, 200, 590), 13: (80, 200, 590), 14: (70, 185, 600), 15: (70, 185, 600), 
        16: (65, 185, 600), 17: (65, 185, 600), 18: (65, 185, 600), 19: (60, 185, 600), 20: (60, 185, 600),
    },


    # christmas
    'JMUG11WBUVPPSCMSMUVP': {     
         1: (150, 540),  2: (150, 540),  3: (150, 540),  4: (150, 540),  5: (150, 540),  
         6: (150, 540),  7: (150, 540),  8: (150, 540),  9: (150, 540), 10: (150, 540),  
        11: (150, 540), 12: (130, 540), 13: (130, 540), 14: (110, 540), 15: (110, 540), 
        16: (90, 560),  17: (90, 560),  18: (90, 560),  19: (80, 560),  20: (80, 560),
    },
    'JMUG11WBUVPPSCMSRUVP': {     
         1: (150, 540),  2: (150, 540),  3: (150, 540),  4: (150, 540),  5: (150, 540),  
         6: (150, 540),  7: (150, 540),  8: (150, 540),  9: (150, 540), 10: (150, 540),  
        11: (150, 540), 12: (130, 540), 13: (130, 540), 14: (110, 540), 15: (110, 540), 
        16: (90, 560),  17: (90, 560),  18: (90, 560),  19: (80, 560),  20: (80, 560),
    },
    'JMUG11WBUVPPSCMGRUVP': {     
         1: (150, 540),  2: (150, 540),  3: (150, 540),  4: (150, 540),  5: (150, 540),  
         6: (150, 540),  7: (150, 540),  8: (150, 540),  9: (150, 540), 10: (150, 540),  
        11: (150, 540), 12: (130, 540), 13: (130, 540), 14: (110, 540), 15: (110, 540), 
        16: (90, 560),  17: (90, 560),  18: (90, 560),  19: (80, 560),  20: (80, 560),
    },
    'JMUG11WBUVPCCKHCSMUVP': {     
         1: (130, 500),  2: (130, 500),  3: (130, 500),  4: (130, 500),  5: (130, 500),  
         6: (130, 500),  7: (130, 500),  8: (130, 500),  9: (130, 500), 10: (130, 500),  
        11: (130, 500), 12: (110, 500), 13: (110, 500), 14: (90, 500), 15: (90, 500), 
        16: (70, 520),  17: (70, 520),  18: (70, 520),  19: (60, 520),  20: (60, 520),
    },

    # Little Miss
    'JMUG11WBUVPPSLILMGUVP': {     
         1: (130, 200),  2: (130, 200),  3: (130, 200),  4: (130, 200),  5: (130, 200),  
         6: (130, 200),  7: (130, 200),  8: (130, 200),  9: (130, 200), 10: (130, 200),  
        11: (130, 200), 12: (110, 200), 13: (110, 200), 14: (90, 200), 15: (90, 200), 
        16: (70, 220),  17: (70, 220),  18: (70, 220),  19: (60, 220),  20: (60, 220),
    },
    'JMUG11WBUVPPSLILMPUVP': {     
         1: (130, 200),  2: (130, 200),  3: (130, 200),  4: (130, 200),  5: (130, 200),  
         6: (130, 200),  7: (130, 200),  8: (130, 200),  9: (130, 200), 10: (130, 200),  
        11: (130, 200), 12: (110, 200), 13: (110, 200), 14: (90, 200), 15: (90, 200), 
        16: (70, 220),  17: (70, 220),  18: (70, 220),  19: (60, 220),  20: (60, 220),
    },
    'JMUG11WBUVPPSLILMSUVP': {     
         1: (130, 200),  2: (130, 200),  3: (130, 200),  4: (130, 200),  5: (130, 200),  
         6: (130, 200),  7: (130, 200),  8: (130, 200),  9: (130, 200), 10: (130, 200),  
        11: (130, 200), 12: (110, 200), 13: (110, 200), 14: (90, 200), 15: (90, 200), 
        16: (70, 220),  17: (70, 220),  18: (70, 220),  19: (60, 220),  20: (60, 220),
    },
    'JMUG11WBUVPJMMCMWLYUVP': {     
         1: (70, 295),  2: (70, 295),  3: (70, 295),  4: (70, 295),  5: (70, 295),  
         6: (70, 295),  7: (70, 295),  8: (70, 295),  9: (70, 295), 10: (70, 295),  
        11: (70, 295), 12: (70, 295), 13: (70, 295), 14: (70, 295), 15: (70, 295), 
        16: (70, 295), 17: (70, 295), 18: (70, 295), 19: (70, 295), 20: (70, 295),
        21: (60, 305), 22: (60, 305), 23: (60, 305), 24: (60, 305), 25: (60, 305),  
        26: (60, 305), 27: (60, 305), 28: (60, 305), 29: (60, 305), 30: (60, 305),  
        31: (60, 305), 32: (60, 305), 33: (60, 305), 34: (60, 305), 35: (60, 305), 
        36: (40, 315), 37: (40, 315), 38: (40, 315), 39: (40, 315), 40: (40, 315),
        41: (30, 315), 42: (30, 315), 43: (30, 315), 44: (30, 315), 45: (30, 315),  
        46: (30, 315), 47: (30, 315), 48: (30, 315), 49: (30, 315), 50: (30, 315),
    },
    'JMUG11WBUVPPSIMDAMUVP': {
         1: (110, 380),  2: (110, 380), 3: (110, 380),  4: (110, 380),  5: (110, 380),  
         6: (110, 380),  7: (110, 380),  8: (110, 380),  9: (110, 380), 10: (110, 380),  
        11: (110, 380), 12: (110, 380), 13: (100, 380), 14: (100, 420), 15: (100, 420), 
        16: (100, 420), 17: (100, 420), 18: (100, 420), 19: (100, 420), 20: (90, 420),
        21: (90, 420), 22: (90, 420), 23: (90, 420), 24: (70, 420), 25: (70, 420),
    },
    'JMUG11WBUVPPSPSIBUVP': {
         1: (130, 250, 400),  2: (130, 250, 400), 3: (130, 250, 400),  4: (130, 250, 400),  5: (130, 250, 400), 
         6: (130, 250, 400),  7: (130, 250, 400),  8: (130, 250, 400),  9: (130, 250, 400), 10: (130, 250, 400),  
        11: (110, 250, 410), 12: (110, 250, 410), 13: (110, 250, 410), 14: (110, 250, 410), 15: (110, 250, 410), 
        16: (100, 250, 420), 17: (100, 250, 420), 18: (100, 250, 420), 19: (90, 250, 420), 20: (90, 250, 420),
    },
    'JMUG11WBUVPJMRTFTMUVP': {
         1: (65, 475),  2: (65, 475), 3: (65, 475),  4: (65, 475),  5: (65, 475), 
         6: (65, 475),  7: (65, 475),  8: (65, 475),  9: (65, 475), 10: (65, 475),  
        11: (65, 475), 12: (65, 475), 13: (65, 475), 14: (65, 475), 15: (65, 475), 
        16: (65, 475), 17: (65, 475), 18: (65, 475), 19: (65, 475), 20: (55, 475),
        21: (55, 475), 22: (55, 475), 23: (55, 475), 24: (45, 475), 25: (45, 475), 
        26: (45, 475), 27: (45, 475), 28: (45, 475), 29: (45, 475), 30: (45, 475),  
        31: (40, 475), 32: (40, 475), 33: (40, 475), 34: (40, 475), 35: (40, 475), 

    },
}

sku_to_second_fontsize_placement = {  # (font-size, x, y)
    
    # customizable
    'JMUG11WBUVPPSLNTBBUVP': {     
         1: (200, 200),  2: (200, 200),  3: (200, 200),  4: (200, 200),  5: (200, 200),  
         6: (200, 200),  7: (200, 200),  8: (200, 200),  9: (200, 200), 10: (180, 210),  
        11: (180, 210), 12: (150, 230), 13: (150, 230), 14: (120, 250), 15: (120, 250), 
        16: (120, 250), 17: (100, 270), 18: (100, 270), 19: (80, 300),  20: (80, 300),
    },
    'JMUG11WBUVPPSICG1UVP': {     
         1: (200, 200),  2: (200, 200),  3: (200, 200),  4: (200, 200),  5: (200, 200),  
         6: (200, 200),  7: (200, 200),  8: (200, 200),  9: (200, 200), 10: (180, 210),  
        11: (150, 230), 12: (150, 230), 13: (120, 250), 14: (120, 250), 15: (120, 250), 
        16: (120, 250), 17: (100, 270), 18: (80, 300), 19: (80, 300),  20: (80, 300),
    },
    'JMUG11WBUVPPSNNCMUVP': {     
         1: (200, 150),  2: (200, 150),  3: (200, 150),  4: (200, 150),  5: (200, 150),  
         6: (200, 150),  7: (200, 150),  8: (200, 150),  9: (200, 150), 10: (180, 160),  
        11: (180, 160), 12: (150, 180), 13: (150, 180), 14: (120, 200), 15: (120, 200), 
        16: (120, 200), 17: (100, 220), 18: (100, 220), 19: (80, 250),  20: (80, 250),
    },
    'JMUG11WBUVPPSSBFRUVP': {     
         1: (85, 455),  2: (85, 455),  3: (85, 455),  4: (85, 455),  5: (85, 455),  
         6: (85, 455),  7: (85, 455),  8: (85, 455),  9: (85, 455), 10: (85, 455),  
        11: (85, 455), 12: (85, 455), 13: (85, 455), 14: (85, 455), 15: (85, 455), 
        16: (70, 465), 17: (70, 465), 18: (70, 465), 19: (70, 465), 20: (70, 465),
        21: (60, 475), 22: (60, 475), 23: (60, 475), 24: (50, 485), 25: (50, 485),
    },

    'JMUG11WBUVPJMCCAS2UVP': {     
         1: (300, 350),  2: (300, 350),  3: (280, 350),  4: (260, 350),  5: (260, 350),  
         6: (260, 350),  7: (240, 350),  8: (220, 350),  9: (200, 360), 10: (180, 360),       
        11: (150, 360), 12: (140, 360), 13: (130, 370), 14: (120, 370), 15: (110, 370), 
        16: (110, 370), 17: (100, 370), 18: (100, 370), 19: (90, 370),  20: (80, 370),
        21: (80, 380),  22: (80, 380),  23: (80, 380),  24: (80, 380),  25: (80, 380), 
        26: (70, 380),  27: (70, 380),  28: (60, 380),  29: (55, 380),  30: (50, 380), 
        31: (50, 380),  32: (40, 390),  33: (40, 390),  34: (30, 390),  35: (30, 390),
    },
    'JMUG11WBUVPJMCCAS3UVP': {     
         1: (300, 250),  2: (300, 250),  3: (280, 250),  4: (260, 250),  5: (260, 250),  
         6: (260, 250),  7: (240, 250),  8: (220, 250),  9: (200, 260), 10: (180, 260),       
        11: (150, 260), 12: (140, 260), 13: (130, 270), 14: (120, 270), 15: (110, 270), 
        16: (110, 270), 17: (100, 270), 18: (100, 270), 19: (90, 270),  20: (80, 270),
        21: (80, 280),  22: (80, 280),  23: (80, 280),  24: (80, 280),  25: (80, 280), 
        26: (70, 280),  27: (70, 280),  28: (60, 280),  29: (55, 280),  30: (50, 280), 
        31: (50, 280),  32: (40, 290),  33: (40, 290),  34: (30, 290),  35: (30, 290),
    },
    'JMUG11WBUVPJMCCAS4UVP': {     
         1: (300, 200),  2: (300, 200),  3: (280, 200),  4: (260, 200),  5: (260, 200),  
         6: (260, 200),  7: (240, 200),  8: (220, 200),  9: (200, 210), 10: (180, 210),       
        11: (150, 210), 12: (140, 210), 13: (130, 220), 14: (120, 220), 15: (110, 220), 
        16: (110, 220), 17: (100, 220), 18: (100, 220), 19: (90, 220),  20: (80, 220),
        21: (80, 230),  22: (80, 230),  23: (80, 230),  24: (80, 230),  25: (80, 230), 
        26: (70, 230),  27: (70, 230),  28: (60, 230),  29: (55, 230),  30: (50, 230), 
        31: (50, 230),  32: (40, 240),  33: (40, 240),  34: (30, 240),  35: (30, 240),
    },
    'JMUG11WBUVPJMCCTNR2UVP': {     
         1: (150, 350), 2: (150, 350), 3: (150, 350), 4: (150, 350),  5: (150, 350),  
         6: (150, 350), 7: (150, 350), 8: (150, 350), 9: (130, 360), 10: (130, 360),       
        11: (130, 360), 12: (130, 360), 13: (110, 370), 14: (110, 370), 15: (110, 370), 
        16: (110, 370), 17: (100, 370), 18: (100, 370), 19: (100, 370), 20: (100, 370),
        21: (80, 380), 22: (80, 380), 23: (80, 380), 24: (80, 380), 25: (80, 380), 
        26: (70, 380), 27: (70, 380), 28: (60, 380), 29: (55, 380), 30: (50, 380), 
        31: (50, 380), 32: (40, 390), 33: (40, 390), 34: (30, 390), 35: (30, 390),
    },
    'JMUG11WBUVPJMCCTNR3UVP': {     
         1: (150, 250),   2: (150, 250),   3: (150, 250),   4: (150, 250),   5: (150, 250),  
         6: (150, 250),   7: (150, 250),   8: (150, 250),   9: (130, 260),  10: (130, 260),       
        11: (130, 260), 12: (130, 260), 13: (110, 270), 14: (110, 270), 15: (110, 270), 
        16: (110, 270), 17: (100, 270), 18: (100, 270), 19: (100, 270), 20: (100, 270),
        21: (80, 280), 22: (80, 280), 23: (80, 280), 24: (80, 280), 25: (80, 280), 
        26: (70, 280), 27: (70, 280), 28: (60, 280), 29: (55, 280), 30: (50, 280), 
        31: (50, 280), 32: (40, 290), 33: (40, 290), 34: (30, 290), 35: (30, 290),
    },
    'JMUG11WBUVPJMCCDS2UVP': {     
         1: (150, 350), 2: (150, 350), 3: (150, 350), 4: (150, 350),  5: (150, 350),  
         6: (150, 350), 7: (150, 350), 8: (150, 350), 9: (130, 360), 10: (130, 360),       
        11: (130, 360), 12: (130, 360), 13: (110, 370), 14: (110, 370), 15: (110, 370), 
        16: (110, 370), 17: (100, 370), 18: (100, 370), 19: (100, 370), 20: (100, 370),
        21: (80, 380), 22: (80, 380), 23: (80, 380), 24: (80, 380), 25: (80, 380), 
        26: (70, 380), 27: (70, 380), 28: (60, 380), 29: (55, 380), 30: (50, 380), 
        31: (50, 380), 32: (40, 390), 33: (40, 390), 34: (30, 390), 35: (30, 390),
    },
    'JMUG11WBUVPJMCCDS3UVP': {     
         1: (150, 250),   2: (150, 250),   3: (150, 250),   4: (150, 250),   5: (150, 250),  
         6: (150, 250),   7: (150, 250),   8: (150, 250),   9: (130, 260),  10: (130, 260),       
        11: (130, 260), 12: (130, 260), 13: (110, 270), 14: (110, 270), 15: (110, 270), 
        16: (110, 270), 17: (100, 270), 18: (100, 270), 19: (100, 270), 20: (100, 270),
        21: (80, 280), 22: (80, 280), 23: (80, 280), 24: (80, 280), 25: (80, 280), 
        26: (70, 280), 27: (70, 280), 28: (60, 280), 29: (55, 280), 30: (50, 280), 
        31: (50, 280), 32: (40, 290), 33: (40, 290), 34: (30, 290), 35: (30, 290),
    },
    'JMUG11WBUVPPSTYBMUVP': {     
         1: (50, 450, 400),  2: (50, 450, 400),  3: (50, 450, 400),  4: (50, 450, 400),  5: (50, 450, 400),  
         6: (50, 450, 400),  7: (40, 450, 400),  8: (40, 450, 400),  9: (30, 450, 410), 10: (30, 450, 410),  
        11: (25, 450, 410), 12: (25, 450, 410), 13: (25, 450, 410), 14: (20, 450, 415), 15: (20, 450, 415), 
    },
    'JMUG11WBUVPPSSBNALUVP': {     
         1: (160, 400),  2: (160, 400),  3: (160, 400),  4: (160, 400),  5: (160, 400),  
         6: (160, 400),  7: (160, 400),  8: (160, 400),  9: (160, 400), 10: (150, 410),  
        11: (150, 410), 12: (120, 430), 13: (120, 430), 14: (90, 450), 15: (90, 450), 
        16: (90, 450), 17: (70, 470),  18: (70, 470),  19: (50, 500),  20: (50, 500),
    },
    'JMUG11WBUVPJMRTFTMUVP': {
         1: (45, 610),  2: (45, 610), 3: (45, 610),  4: (45, 610),  5: (45, 610), 
         6: (45, 610),  7: (45, 610),  8: (45, 610),  9: (45, 610), 10: (45, 610),  
        11: (45, 610), 12: (45, 610), 13: (45, 610), 14: (45, 610), 15: (45, 610), 
        16: (45, 610), 17: (45, 610), 18: (45, 610), 19: (45, 610), 20: (35, 610),
        21: (35, 610), 22: (35, 610), 23: (35, 610), 24: (25, 610), 25: (25, 610), 
        26: (25, 610), 27: (25, 610), 28: (25, 610), 29: (25, 610), 30: (25, 610),  
        31: (20, 610), 32: (20, 610), 33: (20, 610), 34: (20, 610), 35: (20, 610),
    },
    'JMUG11WBUVPPSTCMUVP': {
         1: (110, 425),  2: (110, 425), 3: (110, 425),  4: (110, 425),  5: (110, 425),  
         6: (110, 425),  7: (110, 425),  8: (110, 425),  9: (110, 425), 10: (110, 425),  
        11: (110, 425), 12: (110, 425), 13: (100, 425), 14: (100, 425), 15: (100, 425), 
        16: (100, 425), 17: (100, 425), 18: (100, 425), 19: (100, 425), 20: (90, 435),
        21: (90, 435), 22: (90, 435), 23: (90, 435), 24: (70, 445), 25: (70, 445),
    },
    'JMUG11WBUVPPSCRAYMUVP': {
         1: (110, 425),  2: (110, 425), 3: (110, 425),  4: (110, 425),  5: (110, 425),  
         6: (110, 425),  7: (110, 425),  8: (110, 425),  9: (110, 425), 10: (110, 425),  
        11: (110, 425), 12: (110, 425), 13: (100, 425), 14: (100, 425), 15: (100, 425), 
        16: (100, 425), 17: (100, 425), 18: (100, 425), 19: (100, 425), 20: (90, 435),
        21: (90, 435), 22: (90, 435), 23: (90, 435), 24: (70, 445), 25: (70, 445),
    },

    # fav child
    'JMUG11WBUVPPS2FAVCHUVP': {     
         1: (150, 210),  2: (150, 210), 3: (150, 210), 4: (150, 210),  5: (150, 210),  
         6: (150, 210),  7: (150, 210), 8: (150, 210), 9: (150, 210), 10: (140, 220),  
        11: (130, 220), 12: (130, 240), 13: (100, 240), 14: (90, 260),  15: (90, 260), 
    },
    'JMUG11WBUVPPS3FAVCHUVP': {     
         1: (130, 180),  2: (130, 180),  3: (130, 180),  4: (130, 180),  5: (130, 180),  
         6: (130, 180),  7: (130, 180),  8: (130, 180),  9: (130, 180), 10: (130, 180),  
        11: (120, 180), 12: (120, 180), 13: (120, 180), 14: (120, 180), 15: (120, 180), 
    },
    'JMUG11WBUVPPS4FAVCHUVP': {     
         1: (110, 160), 2: (110, 160), 3: (110, 160), 4: (110, 160),  5: (110, 160),  
         6: (110, 160), 7: (110, 160), 8: (110, 160), 9: (110, 160), 10: (110, 160),  
        11: (100, 150), 12: (100, 150), 13: (100, 150), 14: (90, 155),  15: (90, 155), 
    },
}

sku_to_third_fontsize_placement = {  # (font-size, x, y)
    
    # customizable
    'JMUG11WBUVPPSNNCMUVP': {     
         1: (100, 200),  2: (100, 500),  3: (100, 200),  4: (100, 500),  5: (100, 200),  
         6: (100, 200),  7: (100, 200),  8: (100, 200),  9: (100, 200), 10: (80, 210),  
        11: (80, 210), 12: (50, 230), 13: (50, 230), 14: (20, 250), 15: (20, 250), 
        16: (20, 250), 17: (20, 270), 18: (20, 270), 19: (20, 300),  20: (20, 300),
    },
    'JMUG11WBUVPPSSBFRUVP': {     
         1: (85, 580),  2: (85, 580),  3: (85, 580),  4: (85, 580),  5: (85, 580),  
         6: (85, 580),  7: (85, 580),  8: (85, 580),  9: (85, 580), 10: (85, 580),  
        11: (85, 580), 12: (85, 580), 13: (85, 580), 14: (85, 580), 15: (85, 580), 
        16: (70, 590), 17: (70, 590), 18: (70, 590), 19: (70, 590), 20: (70, 590),
        21: (60, 600), 22: (60, 600), 23: (60, 600), 24: (50, 610), 25: (50, 610),
    },
    'JMUG11WBUVPJMCCAS3UVP': {     
         1: (300, 450),  2: (300, 450),  3: (280, 450),  4: (260, 450),  5: (260, 450),  
         6: (260, 450),  7: (240, 450),  8: (220, 450),  9: (200, 460), 10: (180, 460),       
        11: (150, 460), 12: (140, 460), 13: (130, 470), 14: (120, 470), 15: (110, 470), 
        16: (110, 470), 17: (100, 470), 18: (100, 470), 19: (90, 470),  20: (80, 470),
        21: (80, 480),  22: (80, 480),  23: (80, 480),  24: (80, 480),  25: (80, 480), 
        26: (70, 480),  27: (70, 480),  28: (60, 480),  29: (55, 480),  30: (50, 480), 
        31: (50, 480),  32: (40, 490),  33: (40, 490),  34: (30, 490),  35: (30, 490),
    },
    'JMUG11WBUVPJMCCAS4UVP': {     
         1: (300, 350),  2: (300, 350),  3: (280, 350),  4: (260, 350),  5: (260, 350),  
         6: (260, 350),  7: (240, 350),  8: (220, 350),  9: (200, 360), 10: (180, 360),       
        11: (150, 360), 12: (140, 360), 13: (130, 370), 14: (120, 370), 15: (110, 370), 
        16: (110, 370), 17: (100, 370), 18: (100, 370), 19: (90, 370),  20: (80, 370),
        21: (80, 380),  22: (80, 380),  23: (80, 380),  24: (80, 380),  25: (80, 380), 
        26: (70, 380),  27: (70, 380),  28: (60, 380),  29: (55, 380),  30: (50, 380), 
        31: (50, 380),  32: (40, 390),  33: (40, 390),  34: (30, 390),  35: (30, 390),
    },
    'JMUG11WBUVPJMCCTNR3UVP': {     
         1: (150, 450),   2: (150, 450),   3: (150, 450),   4: (150, 450),   5: (150, 450),  
         6: (150, 450),   7: (150, 450),   8: (150, 450),   9: (130, 460),  10: (130, 460),       
        11: (130, 460), 12: (130, 460), 13: (110, 470), 14: (110, 470), 15: (110, 470), 
        16: (110, 470), 17: (100, 470), 18: (100, 470), 19: (100, 470), 20: (100, 470),
        21: (80, 480), 22: (80, 480), 23: (80, 480), 24: (80, 480), 25: (80, 480), 
        26: (70, 480), 27: (70, 480), 28: (60, 480), 29: (55, 480), 30: (50, 480), 
        31: (50, 480), 32: (40, 490), 33: (40, 490), 34: (30, 490), 35: (30, 490),
    },
        
    # fav child
    'JMUG11WBUVPPS3FAVCHUVP': {     
         1: (130, 300),  2: (130, 300),  3: (130, 300),  4: (130, 300),  5: (130, 300),  
         6: (130, 300),  7: (130, 300),  8: (130, 300),  9: (130, 300), 10: (130, 300),  
        11: (120, 300), 12: (120, 300), 13: (120, 300), 14: (120, 300), 15: (120, 300),
    },
    'JMUG11WBUVPPS4FAVCHUVP': {     
         1: (110, 250), 2: (110, 250), 3: (110, 250), 4: (110, 250),  5: (110, 250),  
         6: (110, 250), 7: (110, 250), 8: (110, 250), 9: (110, 250), 10: (110, 250),  
        11: (100, 240), 12: (100, 240), 13: (100, 240), 14: (90, 245),  15: (90, 245), 
    },
}

sku_to_four_fontsize_placement = {  # (font-size, x, y)
    'JMUG11WBUVPPS4FAVCHUVP': {     
         1: (110, None, 350), 2: (110, None, 350), 3: (110, None, 350), 4: (110, None, 350),  5: (110, None, 350),  
         6: (110, None, 350), 7: (110, None, 350), 8: (110, None, 350), 9: (110, None, 350), 10: (110, None, 350),   
        11: (100, None, 340), 12: (100, None, 340), 13: (100, None, 340), 14: (90, None, 335),  15: (90, None, 335),  
    },
    'JMUG11WBUVPJMCCAS4UVP': {     
         1: (30, None, 500),   2: (300, None, 500),  3: (280, None, 500),  4: (260, None, 500),  5: (260, None, 500),  
         6: (260, None, 500),  7: (240, None, 500),  8: (220, None, 500),  9: (200, None, 510), 10: (180, None, 510),       
        11: (150, None, 510), 12: (140, None, 510), 13: (130, None, 520), 14: (120, None, 520), 15: (110, None, 520), 
        16: (110, None, 520), 17: (100, None, 520), 18: (100, None, 520), 19: (90, None, 520),  20: (80, None, 520),
        21: (80, None, 530),  22: (80, None, 530),  23: (80, None, 530),  24: (80, None, 530),  25: (80, None, 530), 
        26: (70, None, 530),  27: (70, None, 530),  28: (60, None, 530),  29: (55, None, 530),  30: (50, None, 530), 
        31: (50, None, 530),  32: (40, None, 540),  33: (40, None, 540),  34: (30, None, 540),  35: (30, None, 540),
    },
}