import os
import re

script_dir = os.path.dirname(os.path.abspath(__file__))  
background_image_path = os.path.join(script_dir, 'background', 'tumblers', 'UVPPSSCCPTUVP.png')  

sku_to_image = {

    # SCRIPT
    'UVPUYPTBFUVP': os.path.join(script_dir, 'background', 'Tumblers', '_blank.png'),
    'UVPPSACRYLMIUVP': os.path.join(script_dir, 'background', 'Tumblers', '_blank.png'),
    'UVPPSSCCPTUVP': os.path.join(script_dir, 'background', 'Tumblers', 'UVPPSSCCPTUVP.png'),
    'UVPPSPICBFUVP': os.path.join(script_dir, 'background', 'Tumblers', 'UVPPSPICBFUVP.png'),
    'UVPUYSDD2UVP': os.path.join(script_dir, 'background', 'Tumblers', 'UVPUYSDD2UVP.png'),
    'UVPRADENTUVP': os.path.join(script_dir, 'background', 'Tumblers', 'UVPRADENTUVP.png'),
    'UVPPSGKNTPUVP': os.path.join(script_dir, 'background', 'Tumblers', '_blank.png'),
    'UVPPSGKNTSUVP': os.path.join(script_dir, 'background', 'Tumblers', '_blank.png'),
    'UVPANWTTUVP': os.path.join(script_dir, 'background', 'Tumblers', '_blank.png'),
    'UVPCCBFTUVP': os.path.join(script_dir, 'background', 'Tumblers', '_blank.png'),

    # PIC
    'UVPANWHTUVP': os.path.join(script_dir, 'background', 'Tumblers', 'UVPANWHTUVP.png'),
    'UVPPSTBUVP': os.path.join(script_dir, 'background', 'Tumblers', '_blank.png'),
    'UVPPSKFGPUVP': os.path.join(script_dir, 'background', 'Tumblers', 'UVPPSKFGPUVP.png'),
    'UVPPSKFGWUVP': os.path.join(script_dir, 'background', 'Tumblers', 'UVPPSKFGWUVP.png'),

    # DENTAL
    'UVPPSDENTTELUVP': os.path.join(script_dir, 'background', 'Tumblers', 'UVPPSDENTTELUVP.png'),
    'UVPPSDENTBLKUVP': os.path.join(script_dir, 'background', 'Tumblers', 'UVPPSDENTTELUVP.png'),
    'UVPPSDENTPNKUVP': os.path.join(script_dir, 'background', 'Tumblers', 'UVPPSDENTTELUVP.png'),

    # TEACHERS   
    'UVPUYSTD1UVP': os.path.join(script_dir, 'background', 'Tumblers', 'UVPUYSTD1UVP.png'),  
    'UVPUYSTD2UVP': os.path.join(script_dir, 'background', 'Tumblers', 'UVPUYSTD2UVP.png'),    
    'UVPUYSTD3UVP': os.path.join(script_dir, 'background', 'Tumblers', 'UVPUYSTD3UVP.png'),  
    'UVPUYSTD4UVP': os.path.join(script_dir, 'background', 'Tumblers', 'UVPUYSTD4UVP.png'),
    'UVPUYSTD5UVP': os.path.join(script_dir, 'background', 'Tumblers', 'UVPUYSTD5UVP.png'),  
    'UVPUYSTD6UVP': os.path.join(script_dir, 'background', 'Tumblers', 'UVPUYSTD6UVP.png'),  
    'UVPUYSTD7UVP': os.path.join(script_dir, 'background', 'Tumblers', 'UVPUYSTD7UVP.png'),

    'UVPPSAPPTUVP': os.path.join(script_dir, 'background', 'Tumblers', 'UVPPSAPPTUVP.png'),
    'UVPPSABCTUVP': os.path.join(script_dir, 'background', 'Tumblers', 'UVPPSABCTUVP.png'),
    'UVPPSPENTUVP': os.path.join(script_dir, 'background', 'Tumblers', 'UVPPSPENTUVP.png'),
    'UVPPSBUSTUVP': os.path.join(script_dir, 'background', 'Tumblers', 'UVPPSBUSTUVP.png'),
    
    # KIDS TUM
    'UVPJMKTDSUVP': os.path.join(script_dir, 'background', 'Tumblers', 'UVPJMKTDSUVP.png'),
    'UVPJMKTMTUVP': os.path.join(script_dir, 'background', 'Tumblers', 'UVPJMKTMTUVP.png'),
    'UVPJMKTPCUVP': os.path.join(script_dir, 'background', 'Tumblers', 'UVPJMKTPCUVP.png'),
    'UVPJMKTUCUVP': os.path.join(script_dir, 'background', 'Tumblers', 'UVPJMKTUCUVP.png'),

    'UVPPSKIDTBUVP': os.path.join(script_dir, 'background', 'Tumblers', '_blank.png'),  
    'UVPPSKIDTWUVP': os.path.join(script_dir, 'background', 'Tumblers', '_blank.png'),
    'UVPPSKIDTPUVP': os.path.join(script_dir, 'background', 'Tumblers', '_blank.png'),

    # BLACK / WHITE
    'UVPPSB16BUVP': os.path.join(script_dir, 'background', 'Tumblers', '_blank.png'),
    'UVPPSB16WUVP': os.path.join(script_dir, 'background', 'Tumblers', '_blank.png'),
    'UVPPSTTUMBUVP': os.path.join(script_dir, 'background', 'Tumblers', 'UVPPSTTUMWUVP.png'),
    'UVPPSTTUMWUVP': os.path.join(script_dir, 'background', 'Tumblers', 'UVPPSTTUMWUVP.png'),
    'UVPPSPHRMBUVP': os.path.join(script_dir, 'background', 'Tumblers', 'UVPPSPHRMBUVP.png'),
    'UVPPSPHRMWUVP': os.path.join(script_dir, 'background', 'Tumblers', 'UVPPSPHRMWUVP.png'),
    'UVPPSSTILGBHUVP': os.path.join(script_dir, 'background', 'Tumblers', '_blank.png'),
    'UVPPSSTILGWHUVP': os.path.join(script_dir, 'background', 'Tumblers', '_blank.png'),
    'UVPJMSLCLBUVP': os.path.join(script_dir, 'background', 'Tumblers', '_blank.png'),
    'UVPJMSLCLWUVP': os.path.join(script_dir, 'background', 'Tumblers', '_blank.png'),
    'UVPPSNUBRBUVP': os.path.join(script_dir, 'background', 'Tumblers', 'UVPPSNUBRBUVP.png'),
    'UVPPSNUBRWUVP': os.path.join(script_dir, 'background', 'Tumblers', 'UVPPSNUBRWUVP.png'),
    'UVPJMHDBSUVP': os.path.join(script_dir, 'background', 'Tumblers', 'UVPJMHDBSUVP.png'),
    'UVPJMHDWSUVP': os.path.join(script_dir, 'background', 'Tumblers', 'UVPJMHDWSUVP.png'),
    'UVPJMHDBPUVP': os.path.join(script_dir, 'background', 'Tumblers', 'UVPJMHDBSUVP.png'),
    'UVPJMHDWPUVP': os.path.join(script_dir, 'background', 'Tumblers', 'UVPJMHDWSUVP.png'),

    # HORAZONAL
    'UVPPSEITTTSBUVP': os.path.join(script_dir, 'background', 'Tumblers', 'UVPPSEITTTSBUVP.png'),
    'UVPPSEITTTSWUVP': os.path.join(script_dir, 'background', 'Tumblers', 'UVPPSEITTTSWUVP.png'),
    'UVPPSTTPTBUVP': os.path.join(script_dir, 'background', 'Tumblers', 'UVPPSTTPTBUVP.png'),
    'UVPPSTTPTWUVP': os.path.join(script_dir, 'background', 'Tumblers', 'UVPPSTTPTWUVP.png'),
    'UVPPSTTPTABUVP': os.path.join(script_dir, 'background', 'Tumblers', 'UVPPSTTPTABUVP.png'),
    'UVPPSTTPTAWUVP': os.path.join(script_dir, 'background', 'Tumblers', 'UVPPSTTPTAWUVP.png'),
    'UVPPSTTOTBUVP': os.path.join(script_dir, 'background', 'Tumblers', 'UVPPSTTOTBUVP.png'),
    'UVPPSTTOTWUVP': os.path.join(script_dir, 'background', 'Tumblers', 'UVPPSTTOTWUVP.png'),
    'UVPPSTTOTABUVP': os.path.join(script_dir, 'background', 'Tumblers', 'UVPPSTTOTABUVP.png'),
    'UVPPSTTOTAWUVP': os.path.join(script_dir, 'background', 'Tumblers', 'UVPPSTTOTAWUVP.png'),
    'UVPPSSLPTBUVP': os.path.join(script_dir, 'background', 'Tumblers', 'UVPPSSLPTBUVP.png'),
    'UVPPSSLPTWUVP': os.path.join(script_dir, 'background', 'Tumblers', 'UVPPSSLPTWUVP.png'),
    'UVPPSOPTTBUVP': os.path.join(script_dir, 'background', 'Tumblers', 'UVPPSOPTTBUVP.png'),
    'UVPPSOPTTWUVP': os.path.join(script_dir, 'background', 'Tumblers', 'UVPPSOPTTWUVP.png'),

    # TWO LINE
    'UVPPSVETTBUVP': os.path.join(script_dir, 'background', 'Tumblers', 'UVPPSVETTBUVP.png'),
    'UVPPSVETTWUVP': os.path.join(script_dir, 'background', 'Tumblers', 'UVPPSVETTWUVP.png'),
    'UVPCCGTUMBUVP': os.path.join(script_dir, 'background', 'Tumblers', '_blank.png'),
    'UVPCCGTUMWUVP': os.path.join(script_dir, 'background', 'Tumblers', '_blank.png'),
    'UVPJMMAMATBUVP': os.path.join(script_dir, 'background', 'Tumblers', '_blank.png'),
    'UVPJMMAMATWUVP': os.path.join(script_dir, 'background', 'Tumblers', '_blank.png'),
    'UVPPSAUNTTBUVP': os.path.join(script_dir, 'background', 'Tumblers', '_blank.png'),
    'UVPPSAUNTTWUVP': os.path.join(script_dir, 'background', 'Tumblers', '_blank.png'),

    # HALLOWEEN
    'UVPPSHSTGUVP': os.path.join(script_dir, 'background', 'Tumblers', 'UVPPSHSTGUVP.png'),
    'UVPPSHSTWUVP': os.path.join(script_dir, 'background', 'Tumblers', 'UVPPSHSTWUVP.png'),
    'UVPPSHSTPUVP': os.path.join(script_dir, 'background', 'Tumblers', 'UVPPSHSTPUVP.png'),
    'UVPPSHSTHUVP': os.path.join(script_dir, 'background', 'Tumblers', 'UVPPSHSTHUVP.png'),

    # SUMMER
    'UVPPSBASTUVP-FLAMINGO': os.path.join(script_dir, 'background', 'Tumblers', 'FLAMINGO.png'),  
    'UVPPSBASTUVP-PALM_TREE': os.path.join(script_dir, 'background', 'Tumblers', 'PALM_TREE.png'),  
    'UVPPSBASTUVP-STAR_FISH': os.path.join(script_dir, 'background', 'Tumblers', 'STAR_FISH.png'),  
    'UVPPSBASTUVP-PINEAPPLE': os.path.join(script_dir, 'background', 'Tumblers', 'PINEAPPLE.png'),
    'UVPPSBASTUVP': os.path.join(script_dir, 'background', 'Tumblers', 'UVPPSBASTUVP.png'),

    # GLASSCANS
    'GLSCAN16OZF1JAN': os.path.join(script_dir, 'background', 'glasscan', 'JANUARY.png'),
    'GLSCAN16OZF1FEB': os.path.join(script_dir, 'background', 'glasscan', 'FEBRUARY.png'),
    'GLSCAN16OZF1MAR': os.path.join(script_dir, 'background', 'glasscan', 'MARCH.png'),
    'GLSCAN16OZF1APR': os.path.join(script_dir, 'background', 'glasscan', 'APRIL.png'),
    'GLSCAN16OZF1MAY': os.path.join(script_dir, 'background', 'glasscan', 'MAY.png'),
    'GLSCAN16OZF1JUN': os.path.join(script_dir, 'background', 'glasscan', 'JUNE.png'),
    'GLSCAN16OZF1JUL': os.path.join(script_dir, 'background', 'glasscan', 'JULY.png'),
    'GLSCAN16OZF1AUG': os.path.join(script_dir, 'background', 'glasscan', 'AUGUST.png'),
    'GLSCAN16OZF1SEP': os.path.join(script_dir, 'background', 'glasscan', 'SEPTEMBER.png'),
    'GLSCAN16OZF1OCT': os.path.join(script_dir, 'background', 'glasscan', 'OCTOBER.png'),
    'GLSCAN16OZF1NOV': os.path.join(script_dir, 'background', 'glasscan', 'NOVEMBER.png'),
    'GLSCAN16OZF1DEC': os.path.join(script_dir, 'background', 'glasscan', 'DECEMBER.png'),
}


sku_to_font = {

    # SCRIPT
    'UVPUYPTBFUVP': os.path.join(script_dir, 'Fonts', 'BrittanySignature.ttf'),
    'UVPPSACRYLMIUVP': os.path.join(script_dir, 'Fonts', 'BrittanySignature.ttf'), 
    'UVPPSSCCPTUVP': os.path.join(script_dir, 'Fonts', 'BrittanySignature.ttf'),
    'UVPPSPICBFUVP': os.path.join(script_dir, 'Fonts', 'BrittanySignature.ttf'),
    'UVPUYSDD2UVP': os.path.join(script_dir, 'Fonts', 'BrittanySignature.ttf'),
    'UVPRADENTUVP': os.path.join(script_dir, 'Fonts', 'Brooke Smith Script.ttf'),
    'UVPPSGKNTPUVP': os.path.join(script_dir, 'Fonts', 'Versailles LT Regular.ttf'),
    'UVPPSGKNTSUVP': os.path.join(script_dir, 'Fonts', 'DancingScript-Bold.ttf'),
    'UVPANWTTUVP': os.path.join(script_dir, 'Fonts', 'Rumba.ttf'),
    'UVPCCBFTUVP': os.path.join(script_dir, 'Fonts', 'BrittanySignature.ttf'),

    # PIC
    'UVPANWHTUVP': os.path.join(script_dir, 'Fonts', 'Rumba.ttf'),
    'UVPPSTBUVP': os.path.join(script_dir, 'Fonts', 'Breathing Regular.ttf'),
    'UVPPSKFGPUVP': os.path.join(script_dir, 'Fonts', 'AmaticSC-Regular.ttf'),
    'UVPPSKFGWUVP': os.path.join(script_dir, 'Fonts', 'AmaticSC-Regular.ttf'),

    # DENTAL
    'UVPPSDENTTELUVP': os.path.join(script_dir, 'Fonts', 'BrittanySignature.ttf'),
    'UVPPSDENTBLKUVP': os.path.join(script_dir, 'Fonts', 'BrittanySignature.ttf'),
    'UVPPSDENTPNKUVP': os.path.join(script_dir, 'Fonts', 'BrittanySignature.ttf'),

     # TEACHERS    
    'UVPUYSTD1UVP': os.path.join(script_dir, 'Fonts', 'Apricots.ttf'),  
    'UVPUYSTD2UVP': os.path.join(script_dir, 'Fonts', 'Apricots.ttf'),  
    'UVPUYSTD3UVP': os.path.join(script_dir, 'Fonts', 'Apricots.ttf'),  
    'UVPUYSTD4UVP': os.path.join(script_dir, 'Fonts', 'Apricots.ttf'),
    'UVPUYSTD5UVP': os.path.join(script_dir, 'Fonts', 'Apricots.ttf'),
    'UVPUYSTD6UVP': os.path.join(script_dir, 'Fonts', 'Apricots.ttf'),  
    'UVPUYSTD7UVP': os.path.join(script_dir, 'Fonts', 'Apricots.ttf'),

    'UVPPSAPPTUVP': os.path.join(script_dir, 'Fonts', 'BrittanySignature.ttf'),
    'UVPPSABCTUVP': os.path.join(script_dir, 'Fonts', 'BrittanySignature.ttf'),
    'UVPPSPENTUVP': os.path.join(script_dir, 'Fonts', 'BrittanySignature.ttf'),
    'UVPPSBUSTUVP': os.path.join(script_dir, 'Fonts', 'BrittanySignature.ttf'),

    # KIDS TUM
    'UVPJMKTDSUVP': os.path.join(script_dir, 'Fonts', 'AmaticSC-Regular.ttf'),
    'UVPJMKTMTUVP': os.path.join(script_dir, 'Fonts', 'AmaticSC-Regular.ttf'),
    'UVPJMKTPCUVP': os.path.join(script_dir, 'Fonts', 'DancingScript-Bold.ttf'),
    'UVPJMKTUCUVP': os.path.join(script_dir, 'Fonts', 'DancingScript-Bold.ttf'),

    'UVPPSKIDTBUVP': os.path.join(script_dir, 'Fonts', 'AmaticSC-Regular.ttf'),
    'UVPPSKIDTWUVP': os.path.join(script_dir, 'Fonts', 'AmaticSC-Regular.ttf'),
    'UVPPSKIDTPUVP': os.path.join(script_dir, 'Fonts', 'AmaticSC-Regular.ttf'),

    # BLACK / WHITE
    'UVPPSB16BUVP': os.path.join(script_dir, 'Fonts', 'BrittanySignature.ttf'),
    'UVPPSB16WUVP': os.path.join(script_dir, 'Fonts', 'BrittanySignature.ttf'),
    'UVPPSTTUMBUVP': os.path.join(script_dir, 'Fonts', 'I Love Glitter.ttf'),
    'UVPPSTTUMWUVP': os.path.join(script_dir, 'Fonts', 'I Love Glitter.ttf'),
    'UVPPSPHRMBUVP': os.path.join(script_dir, 'Fonts', 'BrittanySignature.ttf'),
    'UVPPSPHRMWUVP': os.path.join(script_dir, 'Fonts', 'BrittanySignature.ttf'),
    'UVPPSSTILGBHUVP': os.path.join(script_dir, 'Fonts', 'I Love Glitter.ttf'),
    'UVPPSSTILGWHUVP': os.path.join(script_dir, 'Fonts', 'I Love Glitter.ttf'),
    'UVPJMSLCLBUVP': os.path.join(script_dir, 'Fonts', 'Shorelines Script Bold.ttf'),
    'UVPJMSLCLWUVP': os.path.join(script_dir, 'Fonts', 'Shorelines Script Bold.ttf'),
    'UVPPSNUBRBUVP': os.path.join(script_dir, 'Fonts', 'BrittanySignature.ttf'),
    'UVPPSNUBRWUVP': os.path.join(script_dir, 'Fonts', 'BrittanySignature.ttf'),
    'UVPJMHDBSUVP': os.path.join(script_dir, 'Fonts', 'BrittanySignature.ttf'),
    'UVPJMHDWSUVP': os.path.join(script_dir, 'Fonts', 'BrittanySignature.ttf'),
    'UVPJMHDBPUVP': os.path.join(script_dir, 'Fonts', 'BebasNeue-Regular.ttf'),
    'UVPJMHDWPUVP': os.path.join(script_dir, 'Fonts', 'BebasNeue-Regular.ttf'),

    # HORAZONAL
    'UVPPSEITTTSBUVP': os.path.join(script_dir, 'Fonts', 'BrittanySignature.ttf'),
    'UVPPSEITTTSWUVP': os.path.join(script_dir, 'Fonts', 'BrittanySignature.ttf'),
    'UVPPSTTPTBUVP': os.path.join(script_dir, 'Fonts', 'BrittanySignature.ttf'),
    'UVPPSTTPTWUVP': os.path.join(script_dir, 'Fonts', 'BrittanySignature.ttf'),
    'UVPPSTTPTABUVP': os.path.join(script_dir, 'Fonts', 'BrittanySignature.ttf'),
    'UVPPSTTPTAWUVP': os.path.join(script_dir, 'Fonts', 'BrittanySignature.ttf'),
    'UVPPSTTOTBUVP': os.path.join(script_dir, 'Fonts', 'BrittanySignature.ttf'),
    'UVPPSTTOTWUVP': os.path.join(script_dir, 'Fonts', 'BrittanySignature.ttf'),
    'UVPPSTTOTABUVP': os.path.join(script_dir, 'Fonts', 'BrittanySignature.ttf'),
    'UVPPSTTOTAWUVP': os.path.join(script_dir, 'Fonts', 'BrittanySignature.ttf'),
    'UVPPSSLPTBUVP': os.path.join(script_dir, 'Fonts', 'BrittanySignature.ttf'),
    'UVPPSSLPTWUVP': os.path.join(script_dir, 'Fonts', 'BrittanySignature.ttf'),
    'UVPPSOPTTBUVP': os.path.join(script_dir, 'Fonts', 'BrittanySignature.ttf'),
    'UVPPSOPTTWUVP': os.path.join(script_dir, 'Fonts', 'BrittanySignature.ttf'),

    # TWO LINE
    'UVPPSVETTBUVP': os.path.join(script_dir, 'Fonts', 'BrittanySignature.ttf'),
    'UVPPSVETTWUVP': os.path.join(script_dir, 'Fonts', 'BrittanySignature.ttf'),
    'UVPCCGTUMBUVP': os.path.join(script_dir, 'Fonts', 'Radley-Regular.ttf'),
    'UVPCCGTUMWUVP': os.path.join(script_dir, 'Fonts', 'Radley-Regular.ttf'),
    'UVPJMMAMATBUVP': os.path.join(script_dir, 'Fonts', 'AmaticSC-Regular.ttf'),
    'UVPJMMAMATWUVP': os.path.join(script_dir, 'Fonts', 'AmaticSC-Regular.ttf'),
    'UVPPSAUNTTBUVP': os.path.join(script_dir, 'Fonts', 'BrimNarrow-Combined.ttf'),
    'UVPPSAUNTTWUVP': os.path.join(script_dir, 'Fonts', 'BrimNarrow-Combined.ttf'),

    # HALLOWEEN
    'UVPPSHSTGUVP': os.path.join(script_dir, 'Fonts', 'Charu_Chandan_BloodDrip-Regular.ttf'),
    'UVPPSHSTWUVP': os.path.join(script_dir, 'Fonts', 'Charu_Chandan_BloodDrip-Regular.ttf'),
    'UVPPSHSTPUVP': os.path.join(script_dir, 'Fonts', 'Charu_Chandan_BloodDrip-Regular.ttf'),
    'UVPPSHSTHUVP': os.path.join(script_dir, 'Fonts', 'Charu_Chandan_BloodDrip-Regular.ttf'),

    # SUMMER
    'UVPPSBASTUVP': os.path.join(script_dir, 'Fonts', 'AboutLove.ttf'),
    
    # GLASSCANS
    'GLSCAN16OZF1JAN': os.path.join(script_dir, 'Fonts', 'NellaSue.ttf'),
    'GLSCAN16OZF1FEB': os.path.join(script_dir, 'Fonts', 'NellaSue.ttf'),
    'GLSCAN16OZF1MAR': os.path.join(script_dir, 'Fonts', 'NellaSue.ttf'),
    'GLSCAN16OZF1APR': os.path.join(script_dir, 'Fonts', 'NellaSue.ttf'),
    'GLSCAN16OZF1MAY': os.path.join(script_dir, 'Fonts', 'NellaSue.ttf'),
    'GLSCAN16OZF1JUN': os.path.join(script_dir, 'Fonts', 'NellaSue.ttf'),
    'GLSCAN16OZF1JUL': os.path.join(script_dir, 'Fonts', 'NellaSue.ttf'),
    'GLSCAN16OZF1AUG': os.path.join(script_dir, 'Fonts', 'NellaSue.ttf'),
    'GLSCAN16OZF1SEP': os.path.join(script_dir, 'Fonts', 'NellaSue.ttf'),
    'GLSCAN16OZF1OCT': os.path.join(script_dir, 'Fonts', 'NellaSue.ttf'),
    'GLSCAN16OZF1NOV': os.path.join(script_dir, 'Fonts', 'NellaSue.ttf'),
    'GLSCAN16OZF1DEC': os.path.join(script_dir, 'Fonts', 'NellaSue.ttf'),
}

sku_to_second_line_font = { 
    'UVPPSGKNTPUVP': os.path.join(script_dir, 'Fonts', 'Calibri-Heart.ttf'),
    'UVPPSGKNTSUVP': os.path.join(script_dir, 'Fonts', 'Calibri-Heart.ttf'),
    'UVPANWTTUVP': os.path.join(script_dir, 'Fonts', 'DB Sans Regular.ttf'),

    # TWO LINE
    'UVPPSVETTBUVP': os.path.join(script_dir, 'Fonts', 'BebasNeue-Regular.ttf'),
    'UVPPSVETTWUVP': os.path.join(script_dir, 'Fonts', 'BebasNeue-Regular.ttf'),
    'UVPCCGTUMBUVP': os.path.join(script_dir, 'Fonts', 'I Love Glitter.ttf'),
    'UVPCCGTUMWUVP': os.path.join(script_dir, 'Fonts', 'I Love Glitter.ttf'),
    'UVPJMMAMATBUVP': os.path.join(script_dir, 'Fonts', 'I Love Glitter.ttf'),
    'UVPJMMAMATWUVP': os.path.join(script_dir, 'Fonts', 'I Love Glitter.ttf'),
    'UVPPSAUNTTBUVP': os.path.join(script_dir, 'Fonts', 'I Love Glitter.ttf'),
    'UVPPSAUNTTWUVP': os.path.join(script_dir, 'Fonts', 'I Love Glitter.ttf'),

}

skip_line = {  
    "line1": {  
    "physical therapist": [  
        "UVPPSTTPTBUVP", "UVPPSTTPTWUVP",  
    ],  
    "physical therapist assistant": [  
        "UVPPSTTPTABUVP", "UVPPSTTPTAWUVP",  
    ],  
    "occupational therapist": [  
        "UVPPSTTOTBUVP", "UVPPSTTOTWUVP",  
    ],  
    "occupational therapist assistant": [  
        "UVPPSTTOTABUVP", "UVPPSTTOTAWUVP",  
    ],  
    "speech-language pathologist": [  
        "UVPPSSLPTBUVP", "UVPPSSLPTWUVP",  
    ],  
    },  
    "line2": {  
    },
    "line3": {  
    },
    "line4": {  
    }, 
}
  
sku_to_fontsize_placement = {  # (font-size, x, y)  


    # SCRIPT
    'UVPUYPTBFUVP': {     
         1: (700, 500),  2: (700, 500),  3: (700, 500),  4: (700, 500),  5: (700, 500),  
         6: (700, 500),  7: (700, 500),  8: (700, 500),  9: (700, 500), 10: (700, 500),  
        11: (500, 600), 12: (500, 600), 13: (500, 600), 14: (500, 600), 15: (500, 600), 
        16: (500, 600), 17: (500, 600), 18: (500, 600), 19: (500, 600), 20: (500, 600),
        21: (400, 700), 22: (400, 700), 23: (400, 700), 24: (400, 700), 25: (400, 700), 
        26: (400, 700), 27: (400, 700), 28: (400, 700), 29: (400, 700), 30: (400, 700),
    },
    'UVPPSACRYLMIUVP': {     
         1: (700, 500),  2: (700, 500),  3: (700, 500),  4: (700, 500),  5: (700, 500),  
         6: (700, 500),  7: (700, 500),  8: (700, 500),  9: (700, 500), 10: (700, 500),  
        11: (500, 600), 12: (500, 600), 13: (500, 600), 14: (500, 600), 15: (500, 600), 
        16: (500, 600), 17: (500, 600), 18: (500, 600), 19: (500, 600), 20: (500, 600),
        21: (400, 700), 22: (400, 700), 23: (400, 700), 24: (400, 700), 25: (400, 700), 
        26: (400, 700), 27: (400, 700), 28: (400, 700), 29: (400, 700), 30: (400, 700),
    },
    'UVPPSSCCPTUVP': {     
         1: (600, 500),  2: (600, 500),  3: (600, 500),  4: (600, 500),  5: (600, 500),  
         6: (600, 500),  7: (600, 500),  8: (600, 500),  9: (600, 500), 10: (600, 500),  
        11: (500, 600), 12: (500, 600), 13: (500, 600), 14: (500, 600), 15: (500, 600), 
        16: (500, 600), 17: (500, 600), 18: (500, 600), 19: (500, 600), 20: (500, 600),
        21: (400, 700), 22: (400, 700), 23: (400, 700), 24: (400, 700), 25: (400, 700), 
        26: (400, 700), 27: (400, 700), 28: (400, 700), 29: (400, 700), 30: (400, 700),
    },
    'UVPPSPICBFUVP': {       
         1: (425, 1300, 500),  2: (425, 1300, 500),  3: (425, 1300, 500),  4: (425, 1300, 500),  5: (425, 1300, 500),   
         6: (425, 1300, 500),  7: (425, 1300, 500),  8: (425, 1300, 500),  9: (425, 1300, 500), 10: (425, 1300, 500), 
        11: (350, 1300, 600), 12: (350, 1300, 600), 13: (350, 1300, 600), 14: (350, 1300, 600), 15: (350, 1300, 600), 
        16: (350, 1300, 600), 17: (350, 1300, 600), 18: (325, 1300, 600), 19: (325, 1300, 600), 20: (325, 1300, 600),
    },
    'UVPUYSDD2UVP': {     
         1: (400, 1000),  2: (400, 1000),  3: (400, 1000),  4: (400, 1000),  5: (400, 1000),  
         6: (400, 1000),  7: (400, 1100),  8: (400, 1100),  9: (400, 1100), 10: (300, 1200),  
        11: (300, 1200), 12: (300, 1200), 13: (300, 1200), 14: (300, 1200), 15: (250, 1250), 
        16: (250, 1250), 17: (200, 1300), 18: (200, 1300), 19: (150, 1300), 20: (150, 1300),
    },
    'UVPRADENTUVP': {     
         1: (700, 500),  2: (700, 500),  3: (700, 500),  4: (700, 500),  5: (700, 500),  
         6: (700, 500),  7: (700, 500),  8: (700, 500),  9: (700, 500), 10: (700, 500),  
        11: (500, 600), 12: (500, 600), 13: (500, 600), 14: (500, 600), 15: (500, 600), 
        16: (500, 600), 17: (500, 600), 18: (500, 600), 19: (500, 600), 20: (500, 600),
        21: (400, 700), 22: (400, 700), 23: (400, 700), 24: (400, 700), 25: (400, 700), 
        26: (400, 700), 27: (400, 700), 28: (400, 700), 29: (400, 700), 30: (400, 700),
    },
    'UVPPSGKNTPUVP': {     
         1: (800, 300),  2: (800, 300),  3: (800, 300),  4: (800, 300),  5: (800, 300),  
         6: (800, 300),  7: (700, 400),  8: (700, 400),  9: (700, 400), 10: (600, 450),  
        11: (600, 450), 12: (500, 500), 13: (500, 500), 14: (450, 550), 15: (450, 550), 
        16: (400, 550), 17: (350, 600), 18: (350, 600), 19: (300, 650), 20: (300, 650),
    },
    'UVPPSGKNTSUVP': {     
         1: (800, 300),  2: (800, 300),  3: (800, 300),  4: (800, 300),  5: (800, 300),  
         6: (800, 300),  7: (700, 400),  8: (700, 400),  9: (700, 400), 10: (600, 450),  
        11: (600, 450), 12: (500, 500), 13: (500, 500), 14: (450, 550), 15: (450, 550), 
        16: (400, 550), 17: (350, 600), 18: (350, 600), 19: (300, 650), 20: (300, 650),
    },
    'UVPANWTTUVP': {     
         1: (850, 300),  2: (850, 300),  3: (850, 300),  4: (850, 300),  5: (850, 300),  
         6: (850, 300),  7: (750, 400),  8: (750, 400),  9: (750, 400), 10: (650, 450),  
        11: (650, 450), 12: (550, 500), 13: (550, 500), 14: (500, 550), 15: (500, 550), 
        16: (450, 550), 17: (400, 600), 18: (400, 600), 19: (350, 650), 20: (350, 650),
    },
    'UVPCCBFTUVP': {     
         1: (700, 500),  2: (700, 500),  3: (700, 500),  4: (700, 500),  5: (700, 500),  
         6: (700, 500),  7: (700, 500),  8: (700, 500),  9: (700, 500), 10: (700, 500),  
        11: (500, 600), 12: (500, 600), 13: (500, 600), 14: (500, 600), 15: (500, 600), 
        16: (500, 600), 17: (500, 600), 18: (500, 600), 19: (500, 600), 20: (500, 600),
        21: (400, 700), 22: (400, 700), 23: (400, 700), 24: (400, 700), 25: (400, 700), 
        26: (400, 700), 27: (400, 700), 28: (400, 700), 29: (400, 700), 30: (400, 700),
    },

    # PIC
    'UVPANWHTUVP': {     
         1: (800, 400), 2: (800, 400), 3: (800, 400), 4: (800, 400), 5: (800, 400),  
         6: (800, 400), 7: (800, 400), 8: (800, 300, 400),  9: (800, 300, 400), 10: (800, 300, 400),  
        11: (800, 200, 400), 12: (800, 200, 400), 13: (800, 200, 400), 14: (800, 200, 400), 15: (800, 200, 400), 
        16: (800, 100, 400), 17: (800, 100, 400), 18: (800, 100, 400), 19: (800, 100, 400), 20: (800, 100, 400),
    },
    'UVPPSTBUVP': {     
         1: (800, 100), 2: (800, 100), 3: (800, 100), 4: (800, 100), 5: (800, 100),  
         6: (800, 100), 7: (600, 200), 8: (600, 200),  9: (600, 200), 10: (600, 200),  
        11: (400, 300), 12: (400, 300), 13: (400, 300), 14: (400, 300), 15: (300, 400), 
        16: (300, 400), 17: (300, 400), 18: (250, 400), 19: (250, 400), 20: (250, 400),
    },
    'UVPPSKFGPUVP': {     
         1: (800, 300), 2: (800, 300), 3: (800, 300), 4: (800, 300), 5: (800, 300),  
         6: (800, 300), 7: (800, 300), 8: (800, 300, 300),  9: (800, 300, 300), 10: (800, 300, 300),  
        11: (800, 200, 300), 12: (700, 200, 400), 13: (700, 200, 400), 14: (600, 200, 500), 15: (600, 200, 500), 
        16: (600, 100, 500), 17: (500, 100, 500), 18: (500, 100, 500), 19: (400, 100, 600), 20: (400, 100, 600),
    },
    'UVPPSKFGWUVP': {     
         1: (800, 300), 2: (800, 300), 3: (800, 300), 4: (800, 300), 5: (800, 300),  
         6: (800, 300), 7: (800, 300), 8: (800, 300, 300),  9: (800, 300, 300), 10: (800, 300, 300),  
        11: (800, 200, 300), 12: (700, 200, 400), 13: (700, 200, 400), 14: (600, 200, 500), 15: (600, 200, 500), 
        16: (600, 100, 500), 17: (500, 100, 500), 18: (500, 100, 500), 19: (400, 100, 600), 20: (400, 100, 600),
    },

    # DENTAL
    'UVPPSDENTTELUVP': {     
         1: (700, 400), 2: (700, 400), 3: (700, 400), 4: (700, 400), 5: (700, 400),  
         6: (700, 400), 7: (700, 400), 8: (700, 400), 9: (700, 400), 10: (600, 400),  
        11: (500, 200, 500), 12: (500, 200, 500), 13: (500, 200, 500), 14: (500, 200, 500), 15: (500, 200, 500), 
        16: (400, 100, 600), 17: (400, 100, 600), 18: (400, 100, 600), 19: (400, 100, 600), 20: (400, 100, 600),
    },
    'UVPPSDENTBLKUVP': {     
         1: (700, 400), 2: (700, 400), 3: (700, 400), 4: (700, 400), 5: (700, 400),  
         6: (700, 400), 7: (700, 400), 8: (700, 400), 9: (700, 400), 10: (600, 400),  
        11: (500, 200, 500), 12: (500, 200, 500), 13: (500, 200, 500), 14: (500, 200, 500), 15: (500, 200, 500), 
        16: (400, 100, 600), 17: (400, 100, 600), 18: (400, 100, 600), 19: (400, 100, 600), 20: (400, 100, 600),
    },
    'UVPPSDENTPNKUVP': {     
         1: (700, 400), 2: (700, 400), 3: (700, 400), 4: (700, 400), 5: (700, 400),  
         6: (700, 400), 7: (700, 400), 8: (700, 400), 9: (700, 400), 10: (600, 400),  
        11: (500, 200, 500), 12: (500, 200, 500), 13: (500, 200, 500), 14: (500, 200, 500), 15: (500, 200, 500), 
        16: (400, 100, 600), 17: (400, 100, 600), 18: (400, 100, 600), 19: (400, 100, 600), 20: (400, 100, 600),
    },

    # TEACHERS  
    'UVPUYSTD1UVP': {     
        1: (650, 500), 2: (650, 500), 3: (650, 500), 4: (650, 500), 5: (650, 500),  
        6: (650, 500), 7: (650, 500), 8: (650, 500), 9: (650, 500), 10: (650, 500),  
       11: (650, 400, 500), 12: (600, 200, 500), 13: (500, 400, 600), 14: (500, 300, 600), 15: (500, 200, 600), 
       16: (500, 100, 600), 17: (400, 200, 650), 18: (400, 200, 650), 19: (400, 650), 20: (400, 650),
    }, 
    'UVPUYSTD2UVP': {     
        1: (650, 500), 2: (650, 500), 3: (650, 500), 4: (650, 500), 5: (650, 500),  
        6: (650, 500), 7: (650, 500), 8: (650, 800, 500), 9: (650, 750, 500), 10: (650, 700, 500),  
       11: (650, 550, 500), 12: (600, 400, 500), 13: (500, 550, 600), 14: (500, 600, 600), 15: (500, 350, 600), 
       16: (500, 200, 600), 17: (400, 500, 650), 18: (400, 500, 650), 19: (400, 650), 20: (400, 650),
    },   
    'UVPUYSTD3UVP': {     
        1: (650, 500), 2: (650, 500), 3: (650, 500), 4: (650, 500), 5: (650, 500),  
        6: (650, 500), 7: (650, 500), 8: (650, 500), 9: (650, 500), 10: (650, 500),  
       11: (650, 400, 500), 12: (600, 200, 500), 13: (500, 400, 600), 14: (500, 300, 600), 15: (500, 200, 600), 
       16: (500, 100, 600), 17: (400, 200, 650), 18: (400, 200, 650), 19: (400, 650), 20: (400, 650),
    },  
    'UVPUYSTD4UVP': {     
        1: (650, 500), 2: (650, 500), 3: (650, 500), 4: (650, 500), 5: (650, 500),  
        6: (650, 500), 7: (650, 500), 8: (650, 500), 9: (650, 500), 10: (650, 500),  
       11: (650, 400, 500), 12: (600, 200, 500), 13: (500, 400, 600), 14: (500, 300, 600), 15: (500, 200, 600), 
       16: (500, 100, 600), 17: (400, 200, 650), 18: (400, 200, 650), 19: (400, 650), 20: (400, 650),
    }, 
    'UVPUYSTD5UVP': {     
        1: (650, 500), 2: (650, 500), 3: (650, 500), 4: (650, 500), 5: (650, 500),  
        6: (650, 500), 7: (650, 500), 8: (650, 500), 9: (650, 500), 10: (650, 500),  
       11: (650, 400, 500), 12: (600, 200, 500), 13: (500, 400, 600), 14: (500, 300, 600), 15: (500, 200, 600), 
       16: (500, 100, 600), 17: (400, 200, 650), 18: (400, 200, 650), 19: (400, 650), 20: (400, 650),
    }, 
    'UVPUYSTD6UVP': {     
        1: (650, 500), 2: (650, 500), 3: (650, 500), 4: (650, 500), 5: (650, 500),  
        6: (650, 500), 7: (650, 500), 8: (650, 800, 500), 9: (650, 750, 500), 10: (650, 700, 500),  
       11: (650, 550, 500), 12: (600, 400, 500), 13: (500, 550, 600), 14: (500, 600, 600), 15: (500, 350, 600), 
       16: (500, 200, 600), 17: (400, 500, 650), 18: (400, 500, 650), 19: (400, 650), 20: (400, 650),
    },  
    'UVPUYSTD7UVP': {     
        1: (650, 500), 2: (650, 500), 3: (650, 500), 4: (650, 500), 5: (650, 500),  
        6: (650, 500), 7: (650, 500), 8: (650, 500), 9: (650, 500), 10: (650, 500),  
       11: (650, 400, 500), 12: (600, 200, 500), 13: (500, 400, 600), 14: (500, 300, 600), 15: (500, 200, 600), 
       16: (500, 100, 600), 17: (400, 200, 650), 18: (400, 200, 650), 19: (400, 650), 20: (400, 650),
    }, 

    'UVPPSAPPTUVP': {     
         1: (500, 500),  2: (500, 500),  3: (500, 500),  4: (500, 500),  5: (500, 500),  
         6: (500, 500),  7: (500, 500),  8: (500, 500),  9: (500, 500), 10: (500, 500),  
        11: (500, 500), 12: (500, 500), 13: (500, 500), 14: (500, 500), 15: (450, 550), 
        16: (400, 600), 17: (400, 600), 18: (400, 600), 19: (350, 700), 20: (350, 700),
    },
    'UVPPSABCTUVP': {     
         1: (500, 500),  2: (500, 500),  3: (500, 500),  4: (500, 500),  5: (500, 500),  
         6: (500, 500),  7: (500, 500),  8: (500, 500),  9: (500, 500), 10: (500, 500),  
        11: (500, 500), 12: (500, 500), 13: (500, 500), 14: (500, 500), 15: (450, 550), 
        16: (400, 600), 17: (400, 600), 18: (400, 600), 19: (350, 700), 20: (350, 700),
    },
    'UVPPSPENTUVP': {     
         1: (500, 500),  2: (500, 500),  3: (500, 500),  4: (500, 500),  5: (500, 500),  
         6: (500, 500),  7: (500, 500),  8: (500, 500),  9: (500, 500), 10: (500, 500),  
        11: (500, 500), 12: (500, 500), 13: (500, 500), 14: (500, 500), 15: (450, 550), 
        16: (400, 600), 17: (400, 600), 18: (400, 600), 19: (350, 700), 20: (350, 700),
    },
    'UVPPSBUSTUVP': {     
         1: (500, 500),  2: (500, 500),  3: (500, 500),  4: (500, 500),  5: (500, 500),  
         6: (500, 500),  7: (500, 500),  8: (500, 500),  9: (500, 500), 10: (500, 500),  
        11: (500, 500), 12: (500, 500), 13: (500, 500), 14: (500, 500), 15: (450, 550), 
        16: (400, 600), 17: (400, 600), 18: (400, 600), 19: (350, 700), 20: (350, 700),
    },

    # KIDS TUM
    'UVPJMKTDSUVP': {     
         1: (800, 300), 2: (800, 300), 3: (800, 300), 4: (800, 900, 300), 5: (800, 700, 300),  
         6: (800, 500, 300),  7: (800, 300, 300),  8: (700, 100, 400),  9: (700, 100, 400), 10: (600, 200, 450),  
        11: (600, 100, 450), 12: (500, 200, 500), 13: (500, 100, 500), 14: (450, 200, 550), 15: (450, 100, 550), 
        16: (400, 200, 550), 17: (350, 100, 600), 18: (350, 100, 600), 19: (300, 100, 650), 20: (300, 100, 650),
    },
    'UVPJMKTMTUVP': {     
         1: (800, 300), 2: (800, 300), 3: (800, 300), 4: (800, 900, 300), 5: (800, 700, 300),  
         6: (800, 500, 300),  7: (800, 300, 300),  8: (700, 100, 400),  9: (700, 100, 400), 10: (600, 200, 450),  
        11: (600, 100, 450), 12: (500, 200, 500), 13: (500, 100, 500), 14: (450, 200, 550), 15: (450, 100, 550), 
        16: (400, 200, 550), 17: (350, 100, 600), 18: (350, 100, 600), 19: (300, 100, 650), 20: (300, 100, 650),
    },
    'UVPJMKTPCUVP': {     
         1: (700, 400), 2: (700, 400), 3: (700, 900, 400), 4: (700, 800, 400), 5: (700, 400, 400),  
         6: (700, 300, 400),  7: (700, 100, 400),  8: (600, 100, 500),  9: (600, 100, 500), 10: (500, 200, 550),  
        11: (500, 100, 550), 12: (400, 200, 600), 13: (400, 100, 600), 14: (350, 200, 650), 15: (350, 100, 650), 
        16: (300, 200, 700), 17: (300, 100, 700), 18: (300, 100, 700), 19: (250, 100, 750), 20: (250, 100, 750),
    },
    'UVPJMKTUCUVP': {     
         1: (700, 400), 2: (700, 400), 3: (700, 900, 400), 4: (700, 800, 400), 5: (700, 400, 400),  
         6: (700, 300, 400),  7: (700, 100, 400),  8: (600, 100, 500),  9: (600, 100, 500), 10: (500, 200, 550),  
        11: (500, 100, 550), 12: (400, 200, 600), 13: (400, 100, 600), 14: (350, 200, 650), 15: (350, 100, 650), 
        16: (300, 200, 700), 17: (300, 100, 700), 18: (300, 100, 700), 19: (250, 100, 750), 20: (250, 100, 750),
    },

    'UVPPSKIDTBUVP': {     
         1: (1400, -100), 2: (1400, -100), 3: (1400, -100), 4: (1400, -100), 5: (1400, -100),  
         6: (1400, -100), 7: (1300, -50),  8: (1100, 100),  9: (1100, 100), 10: (1100, 100),  
        11: (900, 200),  12: (850, 250),  13: (800, 300),  14: (800, 300),  15: (600, 500), 
        16: (600, 500),  17: (600, 500),  18: (550, 550),  19: (500, 600),  20: (500, 600),
    },
    'UVPPSKIDTWUVP': {     
         1: (1400, -100), 2: (1400, -100), 3: (1400, -100), 4: (1400, -100), 5: (1400, -100),  
         6: (1400, -100), 7: (1300, -50),  8: (1100, 100),  9: (1100, 100), 10: (1100, 100),  
        11: (900, 200),  12: (850, 250),  13: (800, 300),  14: (800, 300),  15: (600, 500), 
        16: (600, 500),  17: (600, 500),  18: (550, 550),  19: (500, 600),  20: (500, 600),
    },
    'UVPPSKIDTPUVP': {     
         1: (1400, -100), 2: (1400, -100), 3: (1400, -100), 4: (1400, -100), 5: (1400, -100),  
         6: (1400, -100), 7: (1300, -50),  8: (1100, 100),  9: (1100, 100), 10: (1100, 100),  
        11: (900, 200),  12: (850, 250),  13: (800, 300),  14: (800, 300),  15: (600, 500), 
        16: (600, 500),  17: (600, 500),  18: (550, 550),  19: (500, 600),  20: (500, 600),
    },

    # BLACK / WHITE
    'UVPPSB16BUVP': {     
         1: (700, 200, 300),  2: (700, 200, 300),  3: (700, 200, 300),  4: (700, 200, 300),  5: (700, 200, 300),  
         6: (700, 200, 300),  7: (700, 200, 300),  8: (700, 200, 300),  9: (700, 200, 300), 10: (700, 200, 300),  
        11: (600, 200, 400), 12: (550, 200, 450), 13: (500, 200, 500), 14: (500, 200, 500), 15: (400, 200, 600), 
        16: (400, 200, 600), 17: (400, 200, 600), 18: (400, 200, 600), 19: (300, 200, 700), 20: (300, 200, 700),
    },
    'UVPPSB16WUVP': {     
         1: (700, 200, 300),  2: (700, 200, 300),  3: (700, 200, 300),  4: (700, 200, 300),  5: (700, 200, 300),  
         6: (700, 200, 300),  7: (700, 200, 300),  8: (700, 200, 300),  9: (700, 200, 300), 10: (700, 200, 300),  
        11: (600, 200, 400), 12: (550, 200, 450), 13: (500, 200, 500), 14: (500, 200, 500), 15: (400, 200, 600), 
        16: (400, 200, 600), 17: (400, 200, 600), 18: (400, 200, 600), 19: (300, 200, 700), 20: (300, 200, 700),
    },
    'UVPPSTTUMBUVP': {     
         1: (200, 875),  2: (200, 875),  3: (200, 875),  4: (200, 875),  5: (200, 875),  
         6: (200, 875),  7: (200, 875),  8: (200, 875),  9: (200, 875), 10: (200, 875),  
        11: (200, 875), 12: (200, 875), 13: (200, 875), 14: (200, 875), 15: (200, 875), 
        16: (200, 875), 17: (200, 875), 18: (200, 875), 19: (200, 875), 20: (200, 875),
        21: (200, 875), 22: (200, 875), 23: (200, 875), 24: (200, 875), 25: (200, 875), 
    },
    'UVPPSTTUMWUVP': {     
         1: (200, 875),  2: (200, 875),  3: (200, 875),  4: (200, 875),  5: (200, 875),  
         6: (200, 875),  7: (200, 875),  8: (200, 875),  9: (200, 875), 10: (200, 875),  
        11: (200, 875), 12: (200, 875), 13: (200, 875), 14: (200, 875), 15: (200, 875), 
        16: (200, 875), 17: (200, 875), 18: (200, 875), 19: (200, 875), 20: (200, 875),
        21: (200, 875), 22: (200, 875), 23: (200, 875), 24: (200, 875), 25: (200, 875), 
    },
    'UVPPSPHRMBUVP': {     
         1: (700, 1000, 300),  2: (700, 1000, 300),  3: (700, 1000, 300),  4: (700, 1000, 300),  5: (700, 1000, 300),  
         6: (700, 1000, 300),  7: (700, 1000, 300),  8: (600, 1000, 400),  9: (600, 1000, 400), 10: (600, 1000, 400),  
        11: (500, 1000, 450), 12: (400, 1000, 500), 13: (400, 1000, 500), 14: (400, 1000, 500), 15: (300, 1000, 600), 
        16: (300, 1000, 600), 17: (300, 1000, 600), 18: (300, 1000, 600), 19: (250, 1000, 700), 20: (250, 1000, 700),
    },
    'UVPPSPHRMWUVP': {     
         1: (700, 1000, 300),  2: (700, 1000, 300),  3: (700, 1000, 300),  4: (700, 1000, 300),  5: (700, 1000, 300),  
         6: (700, 1000, 300),  7: (700, 1000, 300),  8: (600, 1000, 400),  9: (600, 1000, 400), 10: (600, 1000, 400),  
        11: (500, 1000, 450), 12: (400, 1000, 500), 13: (400, 1000, 500), 14: (400, 1000, 500), 15: (300, 1000, 600), 
        16: (300, 1000, 600), 17: (300, 1000, 600), 18: (300, 1000, 600), 19: (250, 1000, 700), 20: (250, 1000, 700),
    },
    'UVPPSSTILGBHUVP': {     
         1: (700, 100, 400),  2: (700, 100, 400),  3: (700, 100, 400),  4: (700, 100, 400),  5: (700, 100, 400),  
         6: (700, 100, 400),  7: (600, 100, 500),  8: (600, 100, 500),  9: (600, 100, 500), 10: (500, 100, 600),  
        11: (500, 100, 600), 12: (400, 100, 700), 13: (400, 100, 700), 14: (400, 100, 700), 15: (400, 100, 700), 
        16: (350, 100, 750), 17: (350, 100, 750), 18: (350, 100, 750), 19: (300, 100, 800), 20: (300, 100, 800),
        21: (300, 100, 800), 22: (200, 100, 900), 23: (200, 100, 900), 24: (200, 100, 900), 25: (200, 100, 900),
    },
    'UVPPSSTILGWHUVP': {     
         1: (700, 100, 400),  2: (700, 100, 400),  3: (700, 100, 400),  4: (700, 100, 400),  5: (700, 100, 400),  
         6: (700, 100, 400),  7: (600, 100, 500),  8: (600, 100, 500),  9: (600, 100, 500), 10: (500, 100, 600),  
        11: (500, 100, 600), 12: (400, 100, 700), 13: (400, 100, 700), 14: (400, 100, 700), 15: (400, 100, 700), 
        16: (350, 100, 750), 17: (350, 100, 750), 18: (350, 100, 750), 19: (300, 100, 800), 20: (300, 100, 800),
        21: (300, 100, 800), 22: (200, 100, 900), 23: (200, 100, 900), 24: (200, 100, 900), 25: (200, 100, 900),
    },
    'UVPJMSLCLBUVP': {     
         1: (400, 400),  2: (400, 400),  3: (400, 400),  4: (400, 400),  5: (400, 400),  
         6: (400, 400),  7: (300, 500),  8: (300, 500),  9: (300, 500), 10: (300, 600),  
        11: (300, 600), 12: (250, 700), 13: (250, 700), 14: (250, 700), 15: (250, 700), 
        16: (250, 750), 17: (250, 750), 18: (250, 750), 19: (200, 800), 20: (200, 800),
        21: (200, 800), 22: (200, 900), 23: (200, 900), 24: (200, 900), 25: (200, 900),
    },
    'UVPJMSLCLWUVP': {     
         1: (400, 400),  2: (400, 400),  3: (400, 400),  4: (400, 400),  5: (400, 400),  
         6: (400, 400),  7: (300, 500),  8: (300, 500),  9: (300, 500), 10: (300, 600),  
        11: (300, 600), 12: (250, 700), 13: (250, 700), 14: (250, 700), 15: (250, 700), 
        16: (250, 750), 17: (250, 750), 18: (250, 750), 19: (200, 800), 20: (200, 800),
        21: (200, 800), 22: (200, 900), 23: (200, 900), 24: (200, 900), 25: (200, 900),
    },
    'UVPPSNUBRBUVP': {       
         1: (425, 1300, 500),  2: (425, 1300, 500),  3: (425, 1300, 500),  4: (425, 1300, 500),  5: (425, 1300, 500),   
         6: (425, 1300, 500),  7: (425, 1300, 500),  8: (425, 1300, 500),  9: (425, 1300, 500), 10: (425, 1300, 500), 
        11: (350, 1300, 600), 12: (350, 1300, 600), 13: (350, 1300, 600), 14: (350, 1300, 600), 15: (350, 1300, 600), 
        16: (350, 1300, 600), 17: (350, 1300, 600), 18: (325, 1300, 600), 19: (325, 1300, 600), 20: (325, 1300, 600),
    },
    'UVPPSNUBRWUVP': {       
         1: (425, 1300, 500),  2: (425, 1300, 500),  3: (425, 1300, 500),  4: (425, 1300, 500),  5: (425, 1300, 500),   
         6: (425, 1300, 500),  7: (425, 1300, 500),  8: (425, 1300, 500),  9: (425, 1300, 500), 10: (425, 1300, 500), 
        11: (350, 1300, 600), 12: (350, 1300, 600), 13: (350, 1300, 600), 14: (350, 1300, 600), 15: (350, 1300, 600), 
        16: (350, 1300, 600), 17: (350, 1300, 600), 18: (325, 1300, 600), 19: (325, 1300, 600), 20: (325, 1300, 600),
    },
    'UVPJMHDBSUVP': {       
         1: (425, 1200, 500),  2: (425, 1200, 500),  3: (425, 1200, 500),  4: (425, 1200, 500),  5: (425, 1200, 500),   
         6: (425, 1200, 500),  7: (425, 1200, 500),  8: (425, 1200, 500),  9: (425, 1200, 500), 10: (425, 1200, 500), 
        11: (325, 1200, 600), 12: (325, 1200, 600), 13: (325, 1200, 600), 14: (325, 1200, 600), 15: (325, 1200, 600), 
        16: (325, 1200, 600), 17: (325, 1200, 600), 18: (325, 1200, 600), 19: (325, 1200, 600), 20: (500, 1200, 600),
    },
    'UVPJMHDWSUVP': {       
         1: (425, 1200, 500),  2: (425, 1200, 500),  3: (425, 1200, 500),  4: (425, 1200, 500),  5: (425, 1200, 500),   
         6: (425, 1200, 500),  7: (425, 1200, 500),  8: (425, 1200, 500),  9: (425, 1200, 500), 10: (425, 1200, 500), 
        11: (325, 1200, 600), 12: (325, 1200, 600), 13: (325, 1200, 600), 14: (325, 1200, 600), 15: (325, 1200, 600), 
        16: (325, 1200, 600), 17: (325, 1200, 600), 18: (325, 1200, 600), 19: (325, 1200, 600), 20: (500, 1200, 600),
    },
    'UVPJMHDBPUVP': {       
         1: (425, 1200, 500),  2: (425, 1200, 500),  3: (425, 1200, 500),  4: (425, 1200, 500),  5: (425, 1200, 500),   
         6: (425, 1200, 500),  7: (425, 1200, 500),  8: (425, 1200, 500),  9: (425, 1200, 500), 10: (425, 1200, 500), 
        11: (325, 1200, 600), 12: (325, 1200, 600), 13: (325, 1200, 600), 14: (325, 1200, 600), 15: (325, 1200, 600), 
        16: (325, 1200, 600), 17: (325, 1200, 600), 18: (325, 1200, 600), 19: (325, 1200, 600), 20: (500, 1200, 600),
    },
    'UVPJMHDWPUVP': {       
         1: (425, 1200, 500),  2: (425, 1200, 500),  3: (425, 1200, 500),  4: (425, 1200, 500),  5: (425, 1200, 500),   
         6: (425, 1200, 500),  7: (425, 1200, 500),  8: (425, 1200, 500),  9: (425, 1200, 500), 10: (425, 1200, 500), 
        11: (325, 1200, 600), 12: (325, 1200, 600), 13: (325, 1200, 600), 14: (325, 1200, 600), 15: (325, 1200, 600), 
        16: (325, 1200, 600), 17: (325, 1200, 600), 18: (325, 1200, 600), 19: (325, 1200, 600), 20: (500, 1200, 600),
    },

    # HORAZONAL
    'UVPPSEITTTSBUVP': {     
         1: (400, 1300),  2: (400, 1300),  3: (400, 1300),  4: (400, 1300),  5: (400, 1300),  
         6: (400, 1300),  7: (400, 1300),  8: (400, 1300),  9: (400, 1300), 10: (300, 1300),  
        11: (300, 1300), 12: (300, 1300), 13: (300, 1300), 14: (300, 1300), 15: (300, 1300), 
        16: (250, 1300), 17: (250, 1300), 18: (200, 1300), 19: (150, 1300), 20: (150, 1300),
    },
    'UVPPSEITTTSWUVP': {     
         1: (400, 1300),  2: (400, 1300),  3: (400, 1300),  4: (400, 1300),  5: (400, 1300),  
         6: (400, 1300),  7: (400, 1300),  8: (400, 1300),  9: (400, 1300), 10: (300, 1300),  
        11: (300, 1300), 12: (300, 1300), 13: (300, 1300), 14: (300, 1300), 15: (250, 1300), 
        16: (250, 1300), 17: (200, 1300), 18: (200, 1300), 19: (150, 1300), 20: (150, 1300),
    },
    'UVPPSTTPTBUVP': {     
         1: (400, 1300),  2: (400, 1300),  3: (400, 1300),  4: (400, 1300),  5: (400, 1300),  
         6: (400, 1300),  7: (400, 1300),  8: (400, 1300),  9: (400, 1300), 10: (300, 1300),  
        11: (300, 1300), 12: (300, 1300), 13: (300, 1300), 14: (300, 1300), 15: (250, 1300), 
        16: (250, 1300), 17: (200, 1300), 18: (200, 1300), 19: (150, 1300), 20: (150, 1300),
    },
    'UVPPSTTPTWUVP': {     
         1: (400, 1300),  2: (400, 1300),  3: (400, 1300),  4: (400, 1300),  5: (400, 1300),  
         6: (400, 1300),  7: (400, 1300),  8: (400, 1300),  9: (400, 1300), 10: (300, 1300),  
        11: (300, 1300), 12: (300, 1300), 13: (300, 1300), 14: (300, 1300), 15: (250, 1300), 
        16: (250, 1300), 17: (200, 1300), 18: (200, 1300), 19: (150, 1300), 20: (150, 1300),
    },
    'UVPPSTTPTABUVP':{     
         1: (400, 1300),  2: (400, 1300),  3: (400, 1300),  4: (400, 1300),  5: (400, 1300),  
         6: (400, 1300),  7: (400, 1300),  8: (400, 1300),  9: (400, 1300), 10: (300, 1300),  
        11: (300, 1300), 12: (300, 1300), 13: (300, 1300), 14: (300, 1300), 15: (250, 1300), 
        16: (250, 1300), 17: (200, 1300), 18: (200, 1300), 19: (150, 1300), 20: (150, 1300),
    },
    'UVPPSTTPTAWUVP': {     
         1: (400, 1300),  2: (400, 1300),  3: (400, 1300),  4: (400, 1300),  5: (400, 1300),  
         6: (400, 1300),  7: (400, 1300),  8: (400, 1300),  9: (400, 1300), 10: (300, 1300),  
        11: (300, 1300), 12: (300, 1300), 13: (300, 1300), 14: (300, 1300), 15: (250, 1300), 
        16: (250, 1300), 17: (200, 1300), 18: (200, 1300), 19: (150, 1300), 20: (150, 1300),
    },
    'UVPPSTTOTBUVP': {     
         1: (400, 1300),  2: (400, 1300),  3: (400, 1300),  4: (400, 1300),  5: (400, 1300),  
         6: (400, 1300),  7: (400, 1300),  8: (400, 1300),  9: (300, 1300), 10: (300, 1300),  
        11: (300, 1300), 12: (300, 1300), 13: (300, 1300), 14: (300, 1300), 15: (250, 1300), 
        16: (250, 1300), 17: (200, 1300), 18: (200, 1300), 19: (150, 1300), 20: (150, 1300),
    },
    'UVPPSTTOTWUVP': {     
         1: (400, 1300),  2: (400, 1300),  3: (400, 1300),  4: (400, 1300),  5: (400, 1300),  
         6: (400, 1300),  7: (400, 1300),  8: (400, 1300),  9: (400, 1300), 10: (300, 1300),  
        11: (300, 1300), 12: (300, 1300), 13: (300, 1300), 14: (300, 1300), 15: (250, 1300), 
        16: (250, 1300), 17: (200, 1300), 18: (200, 1300), 19: (150, 1300), 20: (150, 1300),
    },
    'UVPPSTTOTABUVP': {     
         1: (400, 1300),  2: (400, 1300),  3: (400, 1300),  4: (400, 1300),  5: (400, 1300),  
         6: (400, 1300),  7: (400, 1300),  8: (400, 1300),  9: (400, 1300), 10: (300, 1300),  
        11: (300, 1300), 12: (300, 1300), 13: (300, 1300), 14: (300, 1300), 15: (250, 1300), 
        16: (250, 1300), 17: (200, 1300), 18: (200, 1300), 19: (150, 1300), 20: (150, 1300),
    },
    'UVPPSTTOTAWUVP': {     
         1: (400, 1300),  2: (400, 1300),  3: (400, 1300),  4: (400, 1300),  5: (400, 1300),  
         6: (400, 1300),  7: (400, 1300),  8: (400, 1300),  9: (400, 1300), 10: (300, 1300),  
        11: (300, 1300), 12: (300, 1300), 13: (300, 1300), 14: (300, 1300), 15: (250, 1300), 
        16: (250, 1300), 17: (200, 1300), 18: (200, 1300), 19: (150, 1300), 20: (150, 1300),
    },
    'UVPPSSLPTBUVP': {     
         1: (400, 1300),  2: (400, 1300),  3: (400, 1300),  4: (400, 1300),  5: (400, 1300),  
         6: (400, 1300),  7: (400, 1300),  8: (400, 1300),  9: (400, 1300), 10: (300, 1300),  
        11: (300, 1300), 12: (300, 1300), 13: (300, 1300), 14: (300, 1300), 15: (250, 1300), 
        16: (250, 1300), 17: (200, 1300), 18: (200, 1300), 19: (150, 1300), 20: (150, 1300),
    },
    'UVPPSSLPTWUVP': {     
         1: (400, 1300),  2: (400, 1300),  3: (400, 1300),  4: (400, 1300),  5: (400, 1300),  
         6: (400, 1300),  7: (400, 1300),  8: (400, 1300),  9: (400, 1300), 10: (300, 1300),  
        11: (300, 1300), 12: (300, 1300), 13: (300, 1300), 14: (300, 1300), 15: (250, 1300), 
        16: (250, 1300), 17: (200, 1300), 18: (200, 1300), 19: (150, 1300), 20: (150, 1300),
    },
    'UVPPSOPTTBUVP': {     
         1: (400, 2500),  2: (400, 2500),  3: (400, 2500),  4: (400, 2500),  5: (400, 2500),  
         6: (400, 2500),  7: (400, 2500),  8: (400, 2500),  9: (400, 2500), 10: (300, 2500),  
        11: (300, 2500), 12: (300, 2500), 13: (300, 2500), 14: (300, 2500), 15: (250, 2500), 
        16: (250, 2500), 17: (200, 2500), 18: (200, 2500), 19: (150, 2500), 20: (150, 2500),
    },
    'UVPPSOPTTWUVP': {     
         1: (400, 2500),  2: (400, 2500),  3: (400, 2500),  4: (400, 2500),  5: (400, 2500),  
         6: (400, 2500),  7: (400, 2500),  8: (400, 2500),  9: (400, 2500), 10: (300, 2500),  
        11: (300, 2500), 12: (300, 2500), 13: (300, 2500), 14: (300, 2500), 15: (250, 2500), 
        16: (250, 2500), 17: (200, 2500), 18: (200, 2500), 19: (150, 2500), 20: (150, 2500),
    },

    # TWO LINE
    'UVPPSVETTBUVP': {     
         1: (400, 1300),  2: (400, 1300),  3: (400, 1300),  4: (400, 1300),  5: (400, 1300),  
         6: (400, 1300),  7: (400, 1300),  8: (400, 1300),  9: (400, 1300), 10: (300, 1300),  
        11: (300, 1300), 12: (300, 1300), 13: (300, 1300), 14: (300, 1300), 15: (250, 1300), 
        16: (250, 1300), 17: (200, 1300), 18: (200, 1300), 19: (150, 1300), 20: (150, 1300),
    },
    'UVPPSVETTWUVP': {     
         1: (400, 1300),  2: (400, 1300),  3: (400, 1300),  4: (400, 1300),  5: (400, 1300),  
         6: (400, 1300),  7: (400, 1300),  8: (400, 1300),  9: (400, 1300), 10: (300, 1300),  
        11: (300, 1300), 12: (300, 1300), 13: (300, 1300), 14: (300, 1300), 15: (250, 1300), 
        16: (250, 1300), 17: (200, 1300), 18: (200, 1300), 19: (150, 1300), 20: (150, 1300),
    },
    'UVPCCGTUMBUVP': {     
         1: (800, 300),  2: (800, 300),  3: (800, 300),  4: (800, 300),  5: (800, 300),  
         6: (800, 300),  7: (700, 400),  8: (700, 400),  9: (700, 400), 10: (600, 450),  
        11: (600, 450), 12: (500, 500), 13: (500, 500), 14: (450, 550), 15: (450, 550), 
        16: (400, 550), 17: (350, 600), 18: (350, 600), 19: (300, 650), 20: (300, 650),
    },
    'UVPCCGTUMWUVP': {     
         1: (800, 300),  2: (800, 300),  3: (800, 300),  4: (800, 300),  5: (800, 300),  
         6: (800, 300),  7: (700, 400),  8: (700, 400),  9: (700, 400), 10: (600, 450),  
        11: (600, 450), 12: (500, 500), 13: (500, 500), 14: (450, 550), 15: (450, 550), 
        16: (400, 550), 17: (350, 600), 18: (350, 600), 19: (300, 650), 20: (300, 650),
    },
    'UVPJMMAMATBUVP': {     
         1: (800, 300),  2: (800, 300),  3: (800, 300),  4: (800, 300),  5: (800, 300),  
         6: (800, 300),  7: (800, 300),  8: (700, 400),  9: (700, 400), 10: (600, 450),  
        11: (600, 450), 12: (500, 500), 13: (500, 500), 14: (450, 550), 15: (450, 550), 
        16: (400, 550), 17: (350, 600), 18: (350, 600), 19: (300, 650), 20: (300, 650),
    },
    'UVPJMMAMATWUVP': {     
         1: (800, 300),  2: (800, 300),  3: (800, 300),  4: (800, 300),  5: (800, 300),  
         6: (800, 300),  7: (800, 300),  8: (700, 400),  9: (700, 400), 10: (600, 450),  
        11: (600, 450), 12: (500, 500), 13: (500, 500), 14: (450, 550), 15: (450, 550), 
        16: (400, 550), 17: (350, 600), 18: (350, 600), 19: (300, 650), 20: (300, 650),
    },
    'UVPPSAUNTTBUVP': {     
         1: (800, 300),  2: (800, 300),  3: (800, 300),  4: (800, 300),  5: (700, 400),  
         6: (700, 400),  7: (500, 500),  8: (500, 500),  9: (500, 500), 10: (450, 550),  
        11: (450, 550), 12: (400, 600), 13: (350, 650), 14: (300, 650), 15: (300, 650), 
        16: (300, 650), 17: (250, 700), 18: (250, 700), 19: (200, 750), 20: (200, 750),
    },
    'UVPPSAUNTTWUVP': {     
         1: (800, 300),  2: (800, 300),  3: (800, 300),  4: (800, 300),  5: (700, 400),  
         6: (700, 400),  7: (500, 500),  8: (500, 500),  9: (500, 500), 10: (450, 550),  
        11: (450, 550), 12: (400, 600), 13: (350, 650), 14: (300, 650), 15: (300, 650), 
        16: (300, 650), 17: (250, 700), 18: (250, 700), 19: (200, 750), 20: (200, 750),
    },

    # HALLOWEEN
    'UVPPSHSTGUVP': {     
         1: (800, 500, 600),  2: (800, 400, 600),  3: (800, 300, 600),  4: (800, 300, 600),  5: (700, 300, 600),  
         6: (700, 300, 600),  7: (600, 100, 600),  8: (600, 100, 600),  9: (500, 150, 600), 10: (500, 100, 600),  
        11: (400, 200, 700), 12: (400, 100, 700), 13: (400, 100, 700), 14: (400, 100, 700), 15: (400, 100, 700),
        16: (400, 100, 700), 17: (300, 100, 800), 18: (300, 100, 800), 19: (300, 100, 800), 20: (300, 100, 800),
    },
    'UVPPSHSTWUVP': {     
         1: (800, 500, 600),  2: (800, 400, 600),  3: (800, 300, 600),  4: (800, 300, 600),  5: (700, 300, 600),  
         6: (700, 300, 600),  7: (600, 100, 600),  8: (600, 100, 600),  9: (500, 150, 600), 10: (500, 100, 600),  
        11: (400, 200, 700), 12: (400, 100, 700), 13: (400, 100, 700), 14: (400, 100, 700), 15: (400, 100, 700),
        16: (400, 100, 700), 17: (300, 100, 800), 18: (300, 100, 800), 19: (300, 100, 800), 20: (300, 100, 800),
    },
    'UVPPSHSTPUVP': {     
         1: (800, 500, 600),  2: (800, 400, 600),  3: (800, 300, 600),  4: (800, 300, 600),  5: (700, 300, 600),  
         6: (700, 300, 600),  7: (600, 100, 600),  8: (600, 100, 600),  9: (500, 150, 600), 10: (500, 100, 600),  
        11: (400, 200, 700), 12: (400, 100, 700), 13: (400, 100, 700), 14: (400, 100, 700), 15: (400, 100, 700),
        16: (400, 100, 700), 17: (300, 100, 800), 18: (300, 100, 800), 19: (300, 100, 800), 20: (300, 100, 800),
    },
    'UVPPSHSTHUVP': {     
         1: (800, 500, 600),  2: (800, 400, 600),  3: (800, 300, 600),  4: (800, 300, 600),  5: (700, 300, 600),  
         6: (700, 300, 600),  7: (600, 100, 600),  8: (600, 100, 600),  9: (500, 150, 600), 10: (500, 100, 600),  
        11: (400, 200, 700), 12: (400, 100, 700), 13: (400, 100, 700), 14: (400, 100, 700), 15: (400, 100, 700),
        16: (400, 100, 700), 17: (300, 100, 800), 18: (300, 100, 800), 19: (300, 100, 800), 20: (300, 100, 800),
    },

    
    # SUMMER
    'UVPPSBASTUVP': {     
         1: (1000, 500, 600),  2: (1000, 400, 600),  3: (1000, 300, 600),  4: (1000, 300, 600),  5: (900, 300, 600),  
         6: (900, 300, 600),  7: (800, 200, 600),  8: (800, 200, 600),  9: (700, 150, 600), 10: (700, 100, 600),  
        11: (600, 200, 700), 12: (600, 200, 700), 13: (600, 200, 700), 14: (600, 100, 700), 15: (600, 100, 700),
        16: (600, 100, 700), 17: (500, 100, 800), 18: (500, 100, 800), 19: (500, 100, 800), 20: (500, 100, 800),
    },

    # GLASSCANS
    'GLSCAN16OZF1JAN': {     
         1: (200, 200, 450),  2: (200, 200, 450),  3: (200, 200, 450),  4: (200, 200, 450),  5: (200, 200, 450),
         6: (200, 200, 450),  7: (200, 200, 450),  8: (200, 200, 450),  9: (200, 200, 450), 10: (200, 200, 450),  
        11: (200, 200, 450), 12: (200, 200, 450), 13: (200, 200, 450), 14: (200, 200, 450), 15: (200, 200, 450),
        16: (200, 200, 450), 17: (200, 200, 450), 18: (200, 200, 450), 19: (200, 200, 450), 20: (200, 200, 450),
    },
    'GLSCAN16OZF1FEB': {     
         1: (200, 200, 450),  2: (200, 200, 450),  3: (200, 200, 450),  4: (200, 200, 450),  5: (200, 200, 450),
         6: (200, 200, 450),  7: (200, 200, 450),  8: (200, 200, 450),  9: (200, 200, 450), 10: (200, 200, 450),  
        11: (200, 200, 450), 12: (200, 200, 450), 13: (200, 200, 450), 14: (200, 200, 450), 15: (200, 200, 450),
        16: (200, 200, 450), 17: (200, 200, 450), 18: (200, 200, 450), 19: (200, 200, 450), 20: (200, 200, 450),
    },
    'GLSCAN16OZF1MAR': {     
         1: (200, 200, 450),  2: (200, 200, 450),  3: (200, 200, 450),  4: (200, 200, 450),  5: (200, 200, 450),
         6: (200, 200, 450),  7: (200, 200, 450),  8: (200, 200, 450),  9: (200, 200, 450), 10: (200, 200, 450),  
        11: (200, 200, 450), 12: (200, 200, 450), 13: (200, 200, 450), 14: (200, 200, 450), 15: (200, 200, 450),
        16: (200, 200, 450), 17: (200, 200, 450), 18: (200, 200, 450), 19: (200, 200, 450), 20: (200, 200, 450),
    },
    'GLSCAN16OZF1APR': {     
         1: (200, 200, 450),  2: (200, 200, 450),  3: (200, 200, 450),  4: (200, 200, 450),  5: (200, 200, 450),
         6: (200, 200, 450),  7: (200, 200, 450),  8: (200, 200, 450),  9: (200, 200, 450), 10: (200, 200, 450),  
        11: (200, 200, 450), 12: (200, 200, 450), 13: (200, 200, 450), 14: (200, 200, 450), 15: (200, 200, 450),
        16: (200, 200, 450), 17: (200, 200, 450), 18: (200, 200, 450), 19: (200, 200, 450), 20: (200, 200, 450),
    },
    'GLSCAN16OZF1MAY': {     
         1: (200, 200, 450),  2: (200, 200, 450),  3: (200, 200, 450),  4: (200, 200, 450),  5: (200, 200, 450),
         6: (200, 200, 450),  7: (200, 200, 450),  8: (200, 200, 450),  9: (200, 200, 450), 10: (200, 200, 450),  
        11: (200, 200, 450), 12: (200, 200, 450), 13: (200, 200, 450), 14: (200, 200, 450), 15: (200, 200, 450),
        16: (200, 200, 450), 17: (200, 200, 450), 18: (200, 200, 450), 19: (200, 200, 450), 20: (200, 200, 450),
    },
    'GLSCAN16OZF1JUN': {     
         1: (200, 200, 450),  2: (200, 200, 450),  3: (200, 200, 450),  4: (200, 200, 450),  5: (200, 200, 450),
         6: (200, 200, 450),  7: (200, 200, 450),  8: (200, 200, 450),  9: (200, 200, 450), 10: (200, 200, 450),  
        11: (200, 200, 450), 12: (200, 200, 450), 13: (200, 200, 450), 14: (200, 200, 450), 15: (200, 200, 450),
        16: (200, 200, 450), 17: (200, 200, 450), 18: (200, 200, 450), 19: (200, 200, 450), 20: (200, 200, 450),
    },
    'GLSCAN16OZF1JUL': {     
         1: (200, 200, 450),  2: (200, 200, 450),  3: (200, 200, 450),  4: (200, 200, 450),  5: (200, 200, 450),
         6: (200, 200, 450),  7: (200, 200, 450),  8: (200, 200, 450),  9: (200, 200, 450), 10: (200, 200, 450),  
        11: (200, 200, 450), 12: (200, 200, 450), 13: (200, 200, 450), 14: (200, 200, 450), 15: (200, 200, 450),
        16: (200, 200, 450), 17: (200, 200, 450), 18: (200, 200, 450), 19: (200, 200, 450), 20: (200, 200, 450),
    },
    'GLSCAN16OZF1AUG': {     
         1: (200, 200, 450),  2: (200, 200, 450),  3: (200, 200, 450),  4: (200, 200, 450),  5: (200, 200, 450),
         6: (200, 200, 450),  7: (200, 200, 450),  8: (200, 200, 450),  9: (200, 200, 450), 10: (200, 200, 450),  
        11: (200, 200, 450), 12: (200, 200, 450), 13: (200, 200, 450), 14: (200, 200, 450), 15: (200, 200, 450),
        16: (200, 200, 450), 17: (200, 200, 450), 18: (200, 200, 450), 19: (200, 200, 450), 20: (200, 200, 450),
    },
    'GLSCAN16OZF1SEP': {     
         1: (200, 200, 450),  2: (200, 200, 450),  3: (200, 200, 450),  4: (200, 200, 450),  5: (200, 200, 450),
         6: (200, 200, 450),  7: (200, 200, 450),  8: (200, 200, 450),  9: (200, 200, 450), 10: (200, 200, 450),  
        11: (200, 200, 450), 12: (200, 200, 450), 13: (200, 200, 450), 14: (200, 200, 450), 15: (200, 200, 450),
        16: (200, 200, 450), 17: (200, 200, 450), 18: (200, 200, 450), 19: (200, 200, 450), 20: (200, 200, 450),
    },
    'GLSCAN16OZF1OCT': {     
         1: (200, 200, 450),  2: (200, 200, 450),  3: (200, 200, 450),  4: (200, 200, 450),  5: (200, 200, 450),
         6: (200, 200, 450),  7: (200, 200, 450),  8: (200, 200, 450),  9: (200, 200, 450), 10: (200, 200, 450),  
        11: (200, 200, 450), 12: (200, 200, 450), 13: (200, 200, 450), 14: (200, 200, 450), 15: (200, 200, 450),
        16: (200, 200, 450), 17: (200, 200, 450), 18: (200, 200, 450), 19: (200, 200, 450), 20: (200, 200, 450),
    },
    'GLSCAN16OZF1NOV': {     
         1: (200, 200, 450),  2: (200, 200, 450),  3: (200, 200, 450),  4: (200, 200, 450),  5: (200, 200, 450),
         6: (200, 200, 450),  7: (200, 200, 450),  8: (200, 200, 450),  9: (200, 200, 450), 10: (200, 200, 450),  
        11: (200, 200, 450), 12: (200, 200, 450), 13: (200, 200, 450), 14: (200, 200, 450), 15: (200, 200, 450),
        16: (200, 200, 450), 17: (200, 200, 450), 18: (200, 200, 450), 19: (200, 200, 450), 20: (200, 200, 450),
    },
    'GLSCAN16OZF1DEC': {     
         1: (200, 200, 450),  2: (200, 200, 450),  3: (200, 200, 450),  4: (200, 200, 450),  5: (200, 200, 450),
         6: (200, 200, 450),  7: (200, 200, 450),  8: (200, 200, 450),  9: (200, 200, 450), 10: (200, 200, 450),  
        11: (200, 200, 450), 12: (200, 200, 450), 13: (200, 200, 450), 14: (200, 200, 450), 15: (200, 200, 450),
        16: (200, 200, 450), 17: (200, 200, 450), 18: (200, 200, 450), 19: (200, 200, 450), 20: (200, 200, 450),
    },
 }


sku_to_second_fontsize_placement = {  # (font-size, x, y)

    #  tumblers 
    'UVPPSGKNTPUVP': {     
         1: (300, 1200),  2: (300, 1200),  3: (300, 1200),  4: (300, 1200),  5: (300, 1200),  
         6: (300, 1200),  7: (300, 1200),  8: (300, 1200),  9: (300, 1200), 10: (300, 1200),  
        11: (300, 1200), 12: (300, 1200), 13: (250, 1200), 14: (250, 1200), 15: (250, 1200), 
        16: (250, 1200), 17: (200, 1200), 18: (200, 1200), 19: (200, 1200), 20: (200, 1200),
        21: (200, 1200), 22: (200, 1200), 23: (200, 1200), 24: (150, 1200), 25: (150, 1200), 
        26: (150, 1200), 27: (150, 1200), 28: (150, 1200), 29: (150, 1200), 30: (150, 1200),
        31: (150, 1200), 32: (150, 1200), 33: (100, 1200), 34: (100, 1200), 35: (100, 1200), 
        36: (100, 1200), 37: (100, 1200), 38: (100, 1200), 39: (100, 1200), 40: (100, 1200),
        41: (100, 1200), 42: (100, 1200), 43: (100, 1200), 44: (100, 1200), 45: (100, 1200), 
        46: (100, 1200), 47: (100, 1200), 48: (100, 1200), 49: (100, 1200), 50: (100, 1200),
    },
    'UVPPSGKNTSUVP': {     
         1: (300, 1200),  2: (300, 1200),  3: (300, 1200),  4: (300, 1200),  5: (300, 1200),  
         6: (300, 1200),  7: (300, 1200),  8: (300, 1200),  9: (300, 1200), 10: (300, 1200),  
        11: (300, 1200), 12: (300, 1200), 13: (250, 1200), 14: (250, 1200), 15: (250, 1200), 
        16: (250, 1200), 17: (200, 1200), 18: (200, 1200), 19: (200, 1200), 20: (200, 1200),
        21: (200, 1200), 22: (200, 1200), 23: (200, 1200), 24: (150, 1200), 25: (150, 1200), 
        26: (150, 1200), 27: (150, 1200), 28: (150, 1200), 29: (150, 1200), 30: (150, 1200),
        31: (150, 1200), 32: (150, 1200), 33: (100, 1200), 34: (100, 1200), 35: (100, 1200), 
        36: (100, 1200), 37: (100, 1200), 38: (100, 1200), 39: (100, 1200), 40: (100, 1200),
        41: (100, 1200), 42: (100, 1200), 43: (100, 1200), 44: (100, 1200), 45: (100, 1200), 
        46: (100, 1200), 47: (100, 1200), 48: (100, 1200), 49: (100, 1200), 50: (100, 1200),
    },
    'UVPANWTTUVP': {     
         1: (300, 1200),  2: (300, 1200),  3: (300, 1200),  4: (300, 1200),  5: (300, 1200),  
         6: (300, 1200),  7: (300, 1200),  8: (300, 1200),  9: (300, 1200), 10: (300, 1200),  
        11: (300, 1200), 12: (300, 1200), 13: (250, 1200), 14: (250, 1200), 15: (250, 1200), 
        16: (250, 1200), 17: (200, 1200), 18: (200, 1200), 19: (200, 1200), 20: (200, 1200),
        21: (200, 1200), 22: (200, 1200), 23: (200, 1200), 24: (150, 1200), 25: (150, 1200), 
        26: (150, 1200), 27: (150, 1200), 28: (150, 1200), 29: (150, 1200), 30: (150, 1200),
        31: (150, 1200), 32: (150, 1200), 33: (100, 1200), 34: (100, 1200), 35: (100, 1200), 
        36: (100, 1200), 37: (100, 1200), 38: (100, 1200), 39: (100, 1200), 40: (100, 1200),
        41: (100, 1200), 42: (100, 1200), 43: (100, 1200), 44: (100, 1200), 45: (100, 1200), 
        46: (100, 1200), 47: (100, 1200), 48: (100, 1200), 49: (100, 1200), 50: (100, 1200),
    },

    'UVPPSKFGPUVP': {     
         1: (600, 300), 2: (600, 300), 3: (600, 300), 4: (600, 300), 5: (600, 300),  
         6: (600, 300), 7: (600, 300), 8: (600, 300, 300),  9: (600, 300, 300), 10: (600, 300, 300),  
        11: (500, 200, 300), 12: (500, 200, 400), 13: (500, 200, 400), 14: (400, 200, 500), 15: (400, 200, 500), 
        16: (400, 100, 500), 17: (300, 100, 500), 18: (300, 100, 500), 19: (200, 100, 600), 20: (200, 100, 600),
    },
    'UVPPSKFGWUVP': {     
         1: (600, 300), 2: (600, 300), 3: (600, 300), 4: (600, 300), 5: (600, 300),  
         6: (600, 300), 7: (600, 300), 8: (600, 300, 300),  9: (600, 300, 300), 10: (600, 300, 300),  
        11: (500, 200, 300), 12: (500, 200, 400), 13: (500, 200, 400), 14: (400, 200, 500), 15: (400, 200, 500), 
        16: (400, 100, 500), 17: (300, 100, 500), 18: (300, 100, 500), 19: (200, 100, 600), 20: (200, 100, 600),
    },

    # TWO LINE
    'UVPPSVETTBUVP': {     
         1: (300, 2100),  2: (300, 2100),  3: (300, 2100),  4: (300, 2100),  5: (300, 2100),  
         6: (300, 2100),  7: (300, 2100),  8: (300, 2100),  9: (300, 2100), 10: (200, 2100),  
        11: (200, 2100), 12: (200, 2100), 13: (200, 2100), 14: (200, 2100), 15: (150, 2100), 
        16: (150, 2100), 17: (100, 2100), 18: (100, 2100), 19: (50, 2100),  20: (50, 2100),
    },
    'UVPPSVETTWUVP': {     
         1: (300, 2100),  2: (300, 2100),  3: (300, 2100),  4: (300, 2100),  5: (300, 2100),  
         6: (300, 2100),  7: (300, 2100),  8: (300, 2100),  9: (300, 2100), 10: (200, 2100),  
        11: (200, 2100), 12: (200, 2100), 13: (200, 2100), 14: (200, 2100), 15: (150, 2100), 
        16: (150, 2100), 17: (100, 2100), 18: (100, 2100), 19: (50, 2100),  20: (50, 2100),
    },
    'UVPCCGTUMBUVP': {     
         1: (300, 1200),  2: (300, 1200),  3: (300, 1200),  4: (300, 1200),  5: (300, 1200),  
         6: (300, 1200),  7: (300, 1200),  8: (300, 1200),  9: (300, 1200), 10: (300, 1200),  
        11: (300, 1200), 12: (300, 1200), 13: (250, 1200), 14: (250, 1200), 15: (250, 1200), 
        16: (250, 1200), 17: (200, 1200), 18: (200, 1200), 19: (200, 1200), 20: (200, 1200),
        21: (200, 1200), 22: (200, 1200), 23: (200, 1200), 24: (150, 1200), 25: (150, 1200), 
        26: (150, 1200), 27: (150, 1200), 28: (140, 1200), 29: (140, 1200), 30: (130, 1200),
        31: (130, 1200), 32: (120, 1200), 33: (120, 1200), 34: (110, 1200), 35: (110, 1200), 
        36: (100, 1200), 37: (100, 1200), 38: (100, 1200), 39: (100, 1200), 40: (100, 1200),
        41: (100, 1200), 42: (100, 1200), 43: (100, 1200), 44: (100, 1200), 45: (100, 1200), 
        46: (100, 1200), 47: (100, 1200), 48: (100, 1200), 49: (100, 1200), 50: (100, 1200),
    },
    'UVPCCGTUMWUVP': {     
         1: (300, 1200),  2: (300, 1200),  3: (300, 1200),  4: (300, 1200),  5: (300, 1200),  
         6: (300, 1200),  7: (300, 1200),  8: (300, 1200),  9: (300, 1200), 10: (300, 1200),  
        11: (300, 1200), 12: (300, 1200), 13: (250, 1200), 14: (250, 1200), 15: (250, 1200), 
        16: (250, 1200), 17: (200, 1200), 18: (200, 1200), 19: (200, 1200), 20: (200, 1200),
        21: (200, 1200), 22: (200, 1200), 23: (200, 1200), 24: (150, 1200), 25: (150, 1200), 
        26: (150, 1200), 27: (150, 1200), 28: (140, 1200), 29: (140, 1200), 30: (130, 1200),
        31: (130, 1200), 32: (120, 1200), 33: (120, 1200), 34: (110, 1200), 35: (110, 1200), 
        36: (100, 1200), 37: (100, 1200), 38: (100, 1200), 39: (100, 1200), 40: (100, 1200),
        41: (100, 1200), 42: (100, 1200), 43: (100, 1200), 44: (100, 1200), 45: (100, 1200), 
        46: (100, 1200), 47: (100, 1200), 48: (100, 1200), 49: (100, 1200), 50: (100, 1200),
    },
    'UVPJMMAMATBUVP': {     
         1: (300, 1200),  2: (300, 1200),  3: (300, 1200),  4: (300, 1200),  5: (300, 1200),  
         6: (300, 1200),  7: (300, 1200),  8: (300, 1200),  9: (300, 1200), 10: (300, 1200),  
        11: (300, 1200), 12: (300, 1200), 13: (250, 1200), 14: (250, 1200), 15: (250, 1200), 
        16: (250, 1200), 17: (200, 1200), 18: (200, 1200), 19: (200, 1200), 20: (200, 1200),
        21: (200, 1200), 22: (200, 1200), 23: (200, 1200), 24: (150, 1200), 25: (150, 1200), 
        26: (150, 1200), 27: (150, 1200), 28: (140, 1200), 29: (140, 1200), 30: (130, 1200),
        31: (130, 1200), 32: (120, 1200), 33: (120, 1200), 34: (110, 1200), 35: (110, 1200), 
        36: (100, 1200), 37: (100, 1200), 38: (100, 1200), 39: (100, 1200), 40: (100, 1200),
        41: (100, 1200), 42: (100, 1200), 43: (100, 1200), 44: (100, 1200), 45: (100, 1200), 
        46: (100, 1200), 47: (100, 1200), 48: (100, 1200), 49: (100, 1200), 50: (100, 1200),
    },
    'UVPJMMAMATWUVP': {     
         1: (300, 1200),  2: (300, 1200),  3: (300, 1200),  4: (300, 1200),  5: (300, 1200),  
         6: (300, 1200),  7: (300, 1200),  8: (300, 1200),  9: (300, 1200), 10: (300, 1200),  
        11: (300, 1200), 12: (300, 1200), 13: (250, 1200), 14: (250, 1200), 15: (250, 1200), 
        16: (250, 1200), 17: (200, 1200), 18: (200, 1200), 19: (200, 1200), 20: (200, 1200),
        21: (200, 1200), 22: (200, 1200), 23: (200, 1200), 24: (150, 1200), 25: (150, 1200), 
        26: (150, 1200), 27: (150, 1200), 28: (140, 1200), 29: (140, 1200), 30: (130, 1200),
        31: (130, 1200), 32: (120, 1200), 33: (120, 1200), 34: (110, 1200), 35: (110, 1200), 
        36: (100, 1200), 37: (100, 1200), 38: (100, 1200), 39: (100, 1200), 40: (100, 1200),
        41: (100, 1200), 42: (100, 1200), 43: (100, 1200), 44: (100, 1200), 45: (100, 1200), 
        46: (100, 1200), 47: (100, 1200), 48: (100, 1200), 49: (100, 1200), 50: (100, 1200),
    },
    'UVPPSAUNTTBUVP': {     
         1: (300, 1200),  2: (300, 1200),  3: (300, 1200),  4: (300, 1200),  5: (300, 1200),  
         6: (300, 1200),  7: (300, 1200),  8: (300, 1200),  9: (300, 1200), 10: (300, 1200),  
        11: (300, 1200), 12: (300, 1200), 13: (250, 1200), 14: (250, 1200), 15: (250, 1200), 
        16: (250, 1200), 17: (200, 1200), 18: (200, 1200), 19: (200, 1200), 20: (200, 1200),
        21: (200, 1200), 22: (200, 1200), 23: (200, 1200), 24: (150, 1200), 25: (150, 1200), 
        26: (150, 1200), 27: (150, 1200), 28: (140, 1200), 29: (140, 1200), 30: (130, 1200),
        31: (130, 1200), 32: (120, 1200), 33: (120, 1200), 34: (110, 1200), 35: (110, 1200), 
        36: (100, 1200), 37: (100, 1200), 38: (100, 1200), 39: (100, 1200), 40: (100, 1200),
        41: (100, 1200), 42: (100, 1200), 43: (100, 1200), 44: (100, 1200), 45: (100, 1200), 
        46: (100, 1200), 47: (100, 1200), 48: (100, 1200), 49: (100, 1200), 50: (100, 1200),
    },
    'UVPPSAUNTTWUVP': {     
         1: (300, 1200),  2: (300, 1200),  3: (300, 1200),  4: (300, 1200),  5: (300, 1200),  
         6: (300, 1200),  7: (300, 1200),  8: (300, 1200),  9: (300, 1200), 10: (300, 1200),  
        11: (300, 1200), 12: (300, 1200), 13: (250, 1200), 14: (250, 1200), 15: (250, 1200), 
        16: (250, 1200), 17: (200, 1200), 18: (200, 1200), 19: (200, 1200), 20: (200, 1200),
        21: (200, 1200), 22: (200, 1200), 23: (200, 1200), 24: (150, 1200), 25: (150, 1200), 
        26: (150, 1200), 27: (150, 1200), 28: (140, 1200), 29: (140, 1200), 30: (130, 1200),
        31: (130, 1200), 32: (120, 1200), 33: (120, 1200), 34: (110, 1200), 35: (110, 1200), 
        36: (100, 1200), 37: (100, 1200), 38: (100, 1200), 39: (100, 1200), 40: (100, 1200),
        41: (100, 1200), 42: (100, 1200), 43: (100, 1200), 44: (100, 1200), 45: (100, 1200), 
        46: (100, 1200), 47: (100, 1200), 48: (100, 1200), 49: (100, 1200), 50: (100, 1200),
    },
 }


   

