
// DESKPLATES
const prefixDSWCLR001 = "DSWCLR001";  
const deskplates = [

"UVPCCACRP3UVP", "UVPPSTNPWUVP", "UVPPSJOSHDNPUVP","UVPUYACPFUVP", "UVPUYACSFUVP", "UVPUYTEAPLUVP",
"UVPUYACSTUVP", 

"UVPCCACRPWHUVP", "UVPCCACRP2UVP", "UVPCCACRPGLCUVP", "UVPCCACRPSCUVP", 

"UVPJMZZCLASSDNUVP","UVPPSCFDNPUVP", "UVPJMZZFLOWDNPUVP", "UVPPSFLOWDNPUVP","UVPJMZZDNP2UVP", 
"UVPPSZZDNPBUVP", "UVPPSLAWDNPUVP","UVPPSTDSJHUVP", "UVPPSTDSASUVP", 

"UVPPSZACH2UVP", "UVPPSZACH68UVP", "UVPPSZACH6969UVP", 
"UVPPSZACH69UVP"];

const validSkus_deskplates = deskplates.map(suffix => prefixDSWCLR001 + suffix);

// STANLEY NAME PLATE
const nameplates = [
    "ACRTOPRCTUVPCCLOVELYTUVP"
];

// 16oz TUM COLORS 
const prefixACSKTUM16ZPNK = "ACSKTUM16ZPNK";
const prefixACSKTUM16ZBLK = "ACSKTUM16ZBLK";
const prefixACSKTUM16ZICB = "ACSKTUM16ZICB";
const prefixACSKTUM16ZMNT = "ACSKTUM16ZMNT";

// 18oz TUM COLORS 
const prefixACSKTUM18ZDBL = "ACSKTUM18ZDBL";
const prefixACSKTUM18ZCLGD = "ACSKTUM18ZCLGD";
const prefixACSKTUM18ZCLRGD = "ACSKTUM18ZCLRGD";

const nonLineTum = [
    "UVP",
];

const oneLineTum = [

    "UVPUYPTBFUVP", "UVPPSACRYLMIUVP", "UVPPSSCCPTUVP", "UVPPSPICBFUVP", "uvpuysdd2uvp", "UVPRADENTUVP", "UVPCCBFTUVP",

    "UVPANWHTUVP", "UVPPSTBUVP", "UVPPSKFGPUVP", "UVPPSKFGWUVP",
    
    "UVPPSDENTTELUVP", "UVPPSDENTBLKUVP", "UVPPSDENTPNKUVP",
    
    "UVPPSKIDTBUVP", "UVPPSKIDTWUVP", "UVPPSKIDTPUVP",
    
    "UVPUYSTD1UVP","UVPUYSTD2UVP", "UVPUYSTD3UVP", "UVPUYSTD4UVP", "UVPUYSTD5UVP", "UVPUYSTD6UVP", "UVPUYSTD7UVP",
    
    "UVPPSAPPTUVP", "UVPPSABCTUVP", "UVPPSPENTUVP", "UVPPSBUSTUVP",
    
    "UVPJMKTDSUVP", "UVPJMKTMTUVP", "UVPJMKTPCUVP", "UVPJMKTUCUVP",
    
    "UVPPSB16BUVP", "UVPPSB16WUVP", "UVPPSTTUMBUVP", "UVPPSTTUMWUVP", "UVPPSPHRMBUVP", "UVPPSPHRMWUVP", "UVPPSSTILGBHUVP",
    "UVPPSSTILGWHUVP", "UVPJMSLCLBUVP", "UVPJMSLCLWUVP", "UVPPSNUBRBUVP", "UVPPSNUBRWUVP", "UVPJMHDBSUVP", "UVPJMHDWSUVP",
    "UVPJMHDBPUVP", "UVPJMHDWPUVP",
    
    "UVPPSEITTTSBUVP", "UVPPSEITTTSWUVP", "UVPPSTTPTBUVP", "UVPPSTTPTWUVP", "UVPPSTTPTABUVP", "UVPPSTTPTAWUVP", "UVPPSTTOTBUVP", 
    "UVPPSTTOTWUVP", "UVPPSTTOTABUVP", "UVPPSTTOTAWUVP", "UVPPSSLPTBUVP", "UVPPSSLPTWUVP", "UVPPSOPTTBUVP", "UVPPSOPTTWUVP",

    'UVPPSHSTGUVP', 'UVPPSHSTWUVP', 'UVPPSHSTPUVP', 'UVPPSHSTHUVP',

    'UVPPSBASTUVP',
     ];

const twoLineTum = [ 

    "UVPPSGKNTPUVP", "UVPPSGKNTSUVP", "UVPANWTTUVP",

    "UVPPSVETTBUVP", "UVPPSVETTWUVP", "UVPCCGTUMBUVP", "UVPCCGTUMWUVP", "UVPJMMAMATBUVP", "UVPJMMAMATWUVP", "UVPPSAUNTTBUVP", 
    "UVPPSAUNTTWUVP" 
];
     
  
const validSkus_pinkTum = nonLineTum.map(suffix => prefixACSKTUM16ZPNK + suffix).concat(oneLineTum.map(suffix => prefixACSKTUM16ZPNK + suffix)).concat(twoLineTum.map(suffix => prefixACSKTUM16ZPNK + suffix));
const validSkus_blackTum = nonLineTum.map(suffix => prefixACSKTUM16ZBLK + suffix).concat(oneLineTum.map(suffix => prefixACSKTUM16ZBLK + suffix)).concat(twoLineTum.map(suffix => prefixACSKTUM16ZBLK + suffix));
const validSkus_iceTum = nonLineTum.map(suffix => prefixACSKTUM16ZICB + suffix).concat(oneLineTum.map(suffix => prefixACSKTUM16ZICB + suffix)).concat(twoLineTum.map(suffix => prefixACSKTUM16ZICB + suffix));  
const validSkus_mintTum = nonLineTum.map(suffix => prefixACSKTUM16ZMNT + suffix).concat(oneLineTum.map(suffix => prefixACSKTUM16ZMNT + suffix)).concat(twoLineTum.map(suffix => prefixACSKTUM16ZMNT + suffix));  
  
const validSkus_dustyblueTum = nonLineTum.map(suffix => prefixACSKTUM18ZDBL + suffix).concat(oneLineTum.map(suffix => prefixACSKTUM18ZDBL + suffix)).concat(twoLineTum.map(suffix => prefixACSKTUM18ZDBL + suffix));  
const validSkus_goldTum = nonLineTum.map(suffix => prefixACSKTUM18ZCLGD + suffix).concat(oneLineTum.map(suffix => prefixACSKTUM18ZCLGD + suffix)).concat(twoLineTum.map(suffix => prefixACSKTUM18ZCLGD + suffix));  
const validSkus_rosegoldTum = nonLineTum.map(suffix => prefixACSKTUM18ZCLRGD + suffix).concat(oneLineTum.map(suffix => prefixACSKTUM18ZCLRGD + suffix)).concat(twoLineTum.map(suffix => prefixACSKTUM18ZCLRGD + suffix)); 

// GLASS CANS
const Lineglscan = ["GLSCAN16OZF1JAN", "GLSCAN16OZF1FEB", "GLSCAN16OZF1MAR", "GLSCAN16OZF1APR", "GLSCAN16OZF1MAY", "GLSCAN16OZF1JUN", "GLSCAN16OZF1JUL", "GLSCAN16OZF1AUG", "GLSCAN16OZF1SEP",
"GLSCAN16OZF1OCT", "GLSCAN16OZF1NOV", "GLSCAN16OZF1DEC", "GLSCAN16OZUVPF1JANUVP", "GLSCAN16OZUVPF1FEBUVP", "GLSCAN16OZUVPF1MARUVP", "GLSCAN16OZUVPF1APRUVP", "GLSCAN16OZUVPF1MAYUVP", 
"GLSCAN16OZUVPF1JUNUVP", "GLSCAN16OZUVPF1JULUVP", "GLSCAN16OZUVPF1AUGUVP", "GLSCAN16OZUVPF1SEPUVP", "GLSCAN16OZUVPF1OCTUVP", "GLSCAN16OZUVPF1NOVUVP", "GLSCAN16OZUVPF1DECUVP" ];

// PLANKS
const prefixWOOD66 = ["WOOD66", "wood66"];
const prefixWOOD88 = ["WOOD88", "wood88"];
const prefixWOOD1010 = ["WOOD1010", "wood1010"];
const prefixWOOD1212 = ["WOOD1212", "wood1212"];
const prefixWOOD186 = ["WOOD186", "wood186"];
const prefixWOOD2412 = ["WOOD2412", "wood2412"];
const combinedWOOD = [...prefixWOOD66, ...prefixWOOD88, ...prefixWOOD1010, ...prefixWOOD1212, ...prefixWOOD186, ...prefixWOOD2412];
const nonLineWOOD = [

    "UVPCCDUDIUVP", "UVPPSNPEBEGOUVP", "UVPCCBESTTMNUVP",
 
    "UVPPSSWIFTUVP", "UVPPSTSSSUVP",

    "UVPAWLHUVP", "UVPCRYSTALBALLUVP",

    "UVPFALLGNOMESUVP", "UVPtfallss1UVP",
  
    "UVPCCGRBSIUVP", "UVPCCSEYOUPUVP", "UVPCCMWGRMUVP", "UVPPSTISCHRUVP", "UVPUYWINTSHIUVP", "UVPCCGSSMUVP",
    
    "UVPPSHVDFUVP"];

const twoLineWOOD = [ 
    "UVPJMMNSUVP",
];  

const threeLineWOOD = [

    "UVPJMBNSSUVP", "UVPJMASSSUVP", "UVPJMBTSSUVP", "UVPPSFDSSUVP",

    "UVPPSADAMSUVP",

    "UVPJMFDWSUVP", "UVPJMWMSUVP", "UVPPSFNFUVP", "UVPPSIWFSUVP", "UVPUYBLDFS3UVP",

    "UVPCCGFSSMUVP", "UVPPSMCF1UVP", "UVPUYADFAMNEWUVP",];

const validSkus_nonplank = nonLineWOOD.flatMap(suffix => combinedWOOD.map(prefix => prefix + suffix));
const validSkus_2plank = twoLineWOOD.flatMap(suffix => combinedWOOD.map(prefix => prefix + suffix));
const validSkus_3plank = threeLineWOOD.flatMap(suffix => combinedWOOD.map(prefix => prefix + suffix));


// change the sku
export function updateRowSku(row, line1Value, line2Value, line3Value, line4Value) {

    // FAVCHILD MUG
    if (line1Value && line2Value && !line3Value && !line4Value && row[2] === "JMUG11WBUVPPSFAVCHUVP") {  
        row[2] = "JMUG11WBUVPPS2FAVCHUVP";  
    } 
    if (line1Value && line2Value && line3Value && !line4Value && row[2] === "JMUG11WBUVPPSFAVCHUVP") {  
        row[2] = "JMUG11WBUVPPS3FAVCHUVP";  
    } 
    if (line1Value && line2Value && line3Value && line4Value && row[2] === "JMUG11WBUVPPSFAVCHUVP") {  
        row[2] = "JMUG11WBUVPPS4FAVCHUVP";
    }

    // GLASSCAN
    if (line1Value && row[2] === "GLSCAN16OZUVPF1JANUVP") {  
        row[2] = "GLSCAN16OZF1JAN";  
    } 
    if (line1Value && row[2] === "GLSCAN16OZUVPF1FEBUVP") {  
        row[2] = "GLSCAN16OZF1FEB";  
    } 
    if (line1Value && row[2] === "GLSCAN16OZUVPF1MARUVP") {  
        row[2] = "GLSCAN16OZF1MAR";  
    } 
    if (line1Value && row[2] === "GLSCAN16OZUVPF1APRUVP") {  
        row[2] = "GLSCAN16OZF1APR";  
    } 
    if (line1Value && row[2] === "GLSCAN16OZUVPF1MAYUVP") {  
        row[2] = "GLSCAN16OZF1MAY";  
    } 
    if (line1Value && row[2] === "GLSCAN16OZUVPF1JUNUVP") {  
        row[2] = "GLSCAN16OZF1JUN";  
    } 
    if (line1Value && row[2] === "GLSCAN16OZUVPF1JULUVP") {  
        row[2] = "GLSCAN16OZF1JUL";  
    } 
    if (line1Value && row[2] === "GLSCAN16OZUVPF1AUGUVP") {  
        row[2] = "GLSCAN16OZF1AUG";  
    } 
    if (line1Value && row[2] === "GLSCAN16OZUVPF1SEPUVP") {  
        row[2] = "GLSCAN16OZF1SEP";  
    } 
    if (line1Value && row[2] === "GLSCAN16OZUVPF1OCTUVP") {  
        row[2] = "GLSCAN16OZF1OCT";  
    } 
    if (line1Value && row[2] === "GLSCAN16OZUVPF1NOVUVP") {  
        row[2] = "GLSCAN16OZF1NOV";  
    } 
    if (line1Value && row[2] === "GLSCAN16OZUVPF1DECUVP") {  
        row[2] = "GLSCAN16OZF1DEC";  
    }
}

export function applyFontRule(originalOptions, row) {  
    let newOptions = originalOptions;  
  
    const fontMatch = originalOptions.match(/(font:)([^,]*)(,|$)/);  
    const fontValue = fontMatch ? fontMatch[2].trim() : "Default";  
  
    let nameKeywords = ['Name 1:', 'Name 2:', 'Name 3:', 'Name 4:'];  
    let nameValues = [];  
  
    for (const keyword of nameKeywords) {  
        const nameMatch = newOptions.match(new RegExp(`(${keyword})([^,]*)(,|$)`));  
        if (nameMatch) {  
            nameValues.push(nameMatch[2].trim());  
            newOptions = newOptions.replace(new RegExp(`(${keyword})([^,]*)(,|$)`), '');  
        }  
    }  

    if (fontMatch) {  
        newOptions = newOptions.replace(/(Custom Name Top:)([^,]*)(,|$)/, `$1$2, font: ${fontValue}$3`);  
        newOptions = newOptions.replace(/(Custom Name Bottom:)([^,]*)(,|$)/, `$1$2, font: ${fontValue}$3`);  
        newOptions = newOptions.replace(/(,\s*font:)([^,]*)(,|$)/, '');  
    }  
  
    if (nameValues.length > 0) {  
        newOptions = newOptions.replace(/Personalization:(.*?)(,|$)/s, `Personalization:"${nameValues.join('\n')}"$2`);  
    }  
  
    // Amazon Orders  
    if (originalOptions.includes(', imageName:')) {  
        newOptions = newOptions.replace(/,\s*imageName:.*$/, '');  
    }  
  
    // C Orders  
    if (originalOptions.includes(', Art Location 1:')) {  
        newOptions = newOptions.replace(/(,\s*Art Location 1:[^,]*).*$/, '$1');  
    }

    if (originalOptions.includes('print_url:')) {  
        newOptions = newOptions.replace(/(,\s*)?print_url:\s*([^,]*),/, '$1Art Location 1:$2,');  
    } 
    
    
    
    if (originalOptions.includes('font: Al Libretto')) {  
        newOptions = newOptions.replace(/,\s*font:\s*Al Libretto/, '');  
        newOptions = newOptions.replace(/Custom Name:/, 'Design: Al Libretto, Personalization:');  
    } else if (originalOptions.includes('font: Autumn Chant')) {  
        newOptions = newOptions.replace(/,\s*font:\s*Autumn Chant/, '');  
        newOptions = newOptions.replace(/Custom Name:/, 'Design: Mon Amour, Personalization:');  
    } else if (originalOptions.includes('_fulfillment:Font: Autumn Chant')) {  
        newOptions = newOptions.replace(/_fulfillment:Font:\s*Autumn Chant/, '');  
        newOptions = newOptions.replace(/Custom Name:/, 'Design: Mon Amour Months, Personalization:'); 
    } else if (originalOptions.includes('font: Shelby Bold')) {  
        newOptions = newOptions.replace(/,\s*font:\s*Shelby Bold/, '');  
        newOptions = newOptions.replace(/Custom Name:/, 'Design: Bella, Personalization:');   
    } else if (originalOptions.includes('font: Bella')) {  
        newOptions = newOptions.replace(/,\s*font:\s*Bella/, '');  
        newOptions = newOptions.replace(/Custom Name:/, 'Design: Bella, Personalization:');  
    } else if (originalOptions.includes('font: Buffalo Nickel')) {  
        newOptions = newOptions.replace(/,\s*font:\s*Buffalo Nickel/, '');  
        newOptions = newOptions.replace(/Custom Name:/, 'Design: Buffalo Nickel, Personalization:');
    } else if (originalOptions.includes('font: Cervantiss')) {  
        newOptions = newOptions.replace(/,\s*font:\s* Cervantiss/, '');  
        newOptions = newOptions.replace(/Custom Name:/, 'Design: Cervanttis, Personalization:');  
    } else if (originalOptions.includes('font: Cervanttis')) {  
        newOptions = newOptions.replace(/,\s*font:\s*Cervanttis/, '');  
        newOptions = newOptions.replace(/Custom Name:/, 'Design: Cervanttis, Personalization:');  
    } else if (originalOptions.includes('font: Claster Regular')) {  
        newOptions = newOptions.replace(/,\s*font:\s*Claster Regular/, '');  
        newOptions = newOptions.replace(/Custom Name:/, 'Design: Claster Regular, Personalization:');  
    } else if (originalOptions.includes('font: Nella Sue')) {  
        newOptions = newOptions.replace(/,\s*font:\s*Nella Sue/, '');  
        newOptions = newOptions.replace(/Custom Name:/, 'Design: Fairy-Bold, Personalization:');  
    } else if (originalOptions.includes('font: UKIJ')) {  
        newOptions = newOptions.replace(/,\s*font:\s*UKIJ/, '');  
        newOptions = newOptions.replace(/Custom Name:/, 'Design: UKIJ, Personalization:');  
    } else if (originalOptions.includes('Custom Name:')) {  
        newOptions = newOptions.replace(/(Custom Name:)([^,]*)(,|$)/, `Design: Default, Personalization:$2$3`);  
    } 

    if (originalOptions.includes('GLSCAN16OZUVPF1JANUVP')) {  
        newOptions = newOptions.replace('GLSCAN16OZUVPF1MAYUVP', 'GLSCAN16OZF1MAY');  
    } 
     
        const name1Match = originalOptions.match(/(Name 1:)([^,]*)(,|$)/);  
        const name2Match = originalOptions.match(/(Name 2:)([^,]*)(,|$)/);  
        const name3Match = originalOptions.match(/(Name 3:)([^,]*)(,|$)/); 
        const name4Match = originalOptions.match(/(Name 4:)([^,]*)(,|$)/); 
        const middleinscriptionMatch = originalOptions.match(/(Middle Inscription:)([^,]*)(,|$)/);
        const leftInscriptionMatch = originalOptions.match(/(Left Inscription:)([^,]*)(,|$)/);  
        const rightInscriptionMatch = originalOptions.match(/(Right Inscription:)([^,]*)(,|$)/);
        const outsidenameMatch = originalOptions.match(/(Outside Inscription:)([^,]*)(,|$)/);  
        const insidenameMatch = originalOptions.match(/(Inside Inscription:)([^,]*)(,|$)/); 
      
        if (name1Match && name2Match && name3Match && name4Match) {      
            newOptions = originalOptions.replace(/(Name 1:)([^,]*)(,|$)/, `Design: ${fontValue}, Personalization:${name1Match[2].trim()}\n${name2Match[2].trim()}$3\n${name3Match[2].trim()}$3\n${name4Match[2].trim()}$3`);      
            newOptions = newOptions.replace(/(Name 2:)([^,]*)(,|$)/, '');      
            newOptions = newOptions.replace(/(Name 3:)([^,]*)(,|$)/, '');
            newOptions = newOptions.replace(/(Name 4:)([^,]*)(,|$)/, '');
        } else if (name1Match && name2Match && name3Match) {      
            newOptions = originalOptions.replace(/(Name 1:)([^,]*)(,|$)/, `Design: ${fontValue}, Personalization:${name1Match[2].trim()}\n${name2Match[2].trim()}$3\n${name3Match[2].trim()}$3`);      
            newOptions = newOptions.replace(/(Name 2:)([^,]*)(,|$)/, '');      
            newOptions = newOptions.replace(/(Name 3:)([^,]*)(,|$)/, '');      
        } else if (name1Match && name2Match) {  
            newOptions = originalOptions.replace(/(Name 1:)([^,]*)(,|$)/, `Design: ${fontValue}, Personalization:${name1Match[2].trim()}\n${name2Match[2].trim()}$3`);  
            newOptions = newOptions.replace(/(Name 2:)([^,]*)(,|$)/, '');  
        } else if (name1Match) {  
            newOptions = originalOptions.replace(/(Name 1:)([^,]*)(,|$)/, `Design: ${fontValue}, Personalization:${name1Match[2].trim()}$3`);  
        } else if (middleinscriptionMatch && leftInscriptionMatch && rightInscriptionMatch) {        
            newOptions = originalOptions.replace(/(Middle Inscription:)([^,]*)(,|$)/, `Design: ${fontValue}, Personalization:${middleinscriptionMatch[2].trim()}\n${rightInscriptionMatch[2].trim()}$3\n${leftInscriptionMatch[2].trim()}$3`);        
            newOptions = newOptions.replace(/(Right Inscription:)([^,]*)(,|$)/, '');        
            newOptions = newOptions.replace(/(Left Inscription:)([^,]*)(,|$)/, '');        
        } else if (leftInscriptionMatch && rightInscriptionMatch) {  
            newOptions = originalOptions.replace(/(Left Inscription:)([^,]*)(,|$)/, `Design: ${fontValue}, Personalization:${leftInscriptionMatch[2].trim()}\n${rightInscriptionMatch[2].trim()}$3`);  
            newOptions = newOptions.replace(/(Right Inscription:)([^,]*)(,|$)/, '');  
        }  
        if (fontMatch) {  
            newOptions = newOptions.replace(/(,\s*font:)([^,]*)(,|$)/, '');  
        }  
    
        console.log("New Options:", newOptions);  
        return newOptions;  
    } 
    
// BRACELETS

const twoLineBCT = [
    "BCT4GLD", "BCT4SIL", "BCT4RSG", "BCT6GLD", "BCT6SIL", "BCT6RSG"
    ]
    const validSkus_bracelet = twoLineBCT;

// MUGS
const prefixJMUG11WB = ["JMUG11WB", "jmug11wb"];
const nonLineMUG = [

    "SUBCCCPWSUB", "SUBCCKWTWSUB", "SUBUYCFSMSUB", "UVPCAITSUVP", "UVPCCBESTTMNUVP", "UVPCCCRYPUVP", "UVPCCSCHITTMUGUVP", "UVPCCUPMILFUVP",
    "UVPCCWEDCUPUVP", "UVPCCWITCHUVP", "UVPDHDED2ME1UVP", "UVPDHWDNSDYNJY1UVP", "UVPHIKEUVP", "UVPHOCUSMUGUVP", "UVPJMBFNEUVP",
    "UVPJMDCCUVP", "UVPJMDIRMEUVP", "UVPJMDLSUVP", "UVPJMDWMMUVP", "UVPJMIHTDMUVP", "UVPJMPCCUVP", "UVPJMSAWTUVP", "SUBBOSSUB", "UVPJMBFMEUVP",
    "UVPMONKEYSCCUVP", "UVPPPSJEFFDMUVP", "UVPPSADHOUVP", "UVPPSASTRMUVP", "UVPPSBFCEUVP", "UVPPSBFNDMUVP", "UVPPSBFWOUVP", "UVPPSROMEUVP",
    "UVPPSCATMUVP", "UVPPSCHIROUVP", "UVPPSCUMUFUVP", "UVPPSDADABMUVP", "UVPPSDFCMUVP", "UVPPSDJLOUVP", "UVPPSDMDWUVP", "UVPPSDOCAUVP", "UVPPSOFFSUVP",
    "UVPPSDTCNUVP", "UVPPSDUMBUVP", "UVPPSEPTUVP", "UVPPSFQOHRUVP", "UVPPSHUDBCUVP", "UVPPSHUDICKUVP", "UVPPSIBGMUVP", "UVPPSIDRBHUVP", 
    "UVPPSIGBBJSUVP", "UVPPSINAMUVP", "UVPPSJBANHUVP", "UVPPSJCM1UVP", "UVPPSJOEBGUVP", "UVPPSKIMJMUVP", "UVPPSLALPUVP", "UVPPSLAYGASMUVP",
    "UVPPSLVSBUVP", "UVPPSMACASSMUVP", "UVPPSMMMBMUVP", "UVPPSMOMBAUVP", "UVPPSNBAHUVP", "UVPPSNCATUVP", "UVPJMSHITTERUVP", "UVPPSPFDKUVP",
    "UVPPSOKILUVP", "UVPPSONEDEGREEUVP", "UVPPSOWACUVP", "UVPPSPBSBMUVP", "UVPPSPFDKUVP", "UVPPSPPLYUVP", "UVPPSPRSWDLUVP", "UVPPSPRSWDMUVP",
    "UVPPSRTTTSMUVP", "UVPPSSHITTERSUVP", "UVPPSSLPCMUVP", "UVPPSSMUGUVP", "UVPPSSTFUUVP", "UVPPSSWALLOWUVP", "UVPPSTDLCMUVP", "UVPPSTHMDCUVP",
    "UVPPSTOB1UVP", "UVPPSTOD1UVP", "UVPPSTOPBMUVP", "UVPPSTWAFUVP", "UVPPSUHOHUVP", "UVPPSVAGMUVP", "UVPPSWGFMUVP", "UVPPSYFACMUVP", "UVPPSNCATUVP",
    "UVPPSYINAPUVP", "UVPRACAIMUVP", "UVPRAPMAGUVP", "UVPRATODPUVP", "UVPRMCMDND5UVP", "UVPRMCMDND6UVP", "UVPROFSUVP", "UVPttsmmuUVP", "UVPPSSWTUVP",
    "UVPJMSJSSMUVP", "UVPPSTHCTWUVP", "UVPPSWGFMUVP",
];

const oneLineMUG = [
    
    //  customizable
    'UVPJMSAYOCMUVP', 'UVPJMSAY1KMUVP', 'UVPPSWIPEUVP', 'UVPPSMUWRMUVP', 'UVPJMBTOIMUVP', 'UVPPSSPERMMUVP', 'SUBUYTHTSUB', 'UVPJMFMEMUVP',
    'UVPPSYBCMUVP', 'UVPPSBALLS2UVP', 'UVPCCFREKEX1UVP','UVPJMCCTNR1UVP', 'UVPJMCCAS1UVP', 'UVPJMCCDS1UVP', 'UVPPSBONDUVP', 'UVPPSBTEMUVP',
    'UVPPSLILMSUVP', 'UVPPSLILMGUVP', 'UVPPSLILMPUVP', 'SUBJMSUWOMSUB', 'UVPPSPFCMUVP', 'UVPPSLAYBNSMUVP', 'UVPPSGDMNUVP', 'UVPPSFLONAMEUVP',
    'UVPJMIFLYMUVP', 'UVPPSNORMUVP', 'UVPPSDLGFBMUVP', 'UVPPSBOBWUVP', 'UVPPSFARTUVP', 'UVPJMMCMWLYUVP', 'UVPPSIMDAMUVP', 'UVPPSTCMUVP',
    'UVPPSPSIBUVP', 'UVPPSFAVEUVP', 'UVPPSUBCNSBUVP',  'UVPPSMBWRUVP', 'UVPJMOVMUVP', 'UVPPSFUNCMUVP', 'UVPPSNCC1UVP', 'UVPPSBFCEUVP',
    'UVPJMFDCM7UVP', 'UVPPSBMMMUVP', 'UVPPSDUWRMUVP',
     
    //  christmas
    'UVPPSCMSMUVP', 'UVPPSCMSRUVP', 'UVPPSCMGRUVP', 'UVPCCKHCSMUVP',
];

const twoLineMUG = [
    
    //  customizable
    'UVPPSICG1UVP', 'UVPPSLNTBBUVP', 'UVPPSTYBMUVP', 'UVPJMCCAS2UVP', 'UVPJMCCTNR2UVP', 'UVPJMCCDS2UVP', 'UVPPSSBNALUVP', 'UVPPS2FAVCHUVP',
    'UVPPSSCMUVP', 'UVPJMRTFTMUVP', 'UVPPSCRAYMUVP',
];

const threeLineMUG = [

    //  customizable
    'UVPPSNNCMUVP', 'UVPPSSBFRUVP',  'UVPJMCCAS3UVP', 'UVPJMCCTNR3UVP', 'UVPJMCCDS3UVP', 'UVPPS3FAVCHUVP',
];

const fourLineMUG = [
    
    //  customizable
    'UVPPSFAVCHUVP', 'UVPPS4FAVCHUVP', 'UVPJMCCAS4UVP', 
];

const validSkus_nonmug = nonLineMUG.flatMap(suffix => prefixJMUG11WB.map(prefix => prefix + suffix));  
const validSkus_1mug = oneLineMUG.flatMap(suffix => prefixJMUG11WB.map(prefix => prefix + suffix));  
const validSkus_2mug = twoLineMUG.flatMap(suffix => prefixJMUG11WB.map(prefix => prefix + suffix));  
const validSkus_3mug = threeLineMUG.flatMap(suffix => prefixJMUG11WB.map(prefix => prefix + suffix));
const validSkus_4mug = fourLineMUG.flatMap(suffix => prefixJMUG11WB.map(prefix => prefix + suffix));   

// GOLFBALLS

const prefixGLFBLWHTSO = ["GLFBLWHTSO01", "GLFBLWHTSO03", "GLFBLWHTSO06", "GLFBLWHTSO12"];

const oneLineGLFBL = [
    
    'UVPCCGNHBTUVP', 
];

const validSkus_GLFBL = oneLineGLFBL.flatMap(suffix => prefixGLFBLWHTSO.map(prefix => prefix + suffix));

export { prefixACSKTUM16ZPNK, prefixACSKTUM16ZBLK, prefixACSKTUM16ZICB, prefixACSKTUM16ZMNT, prefixACSKTUM18ZDBL, prefixACSKTUM18ZCLGD, 
    prefixACSKTUM18ZCLRGD, nameplates, prefixGLFBLWHTSO, nonLineTum, oneLineTum, Lineglscan, oneLineGLFBL, twoLineBCT, combinedWOOD, nonLineWOOD, 
    threeLineWOOD, prefixJMUG11WB, nonLineMUG, oneLineMUG, twoLineMUG, threeLineMUG, fourLineMUG};  
    
export const validSkus = [...validSkus_deskplates, ...validSkus_pinkTum, ...validSkus_blackTum, ...validSkus_iceTum, ...validSkus_mintTum, 
    ...validSkus_dustyblueTum, ...validSkus_goldTum, ...validSkus_rosegoldTum, ...validSkus_dustyblueTum, ...Lineglscan, ...validSkus_nonplank, 
    ...validSkus_2plank, ...validSkus_3plank, ...validSkus_nonmug, ...validSkus_1mug, ...validSkus_2mug, ...validSkus_3mug, ...validSkus_4mug, 
    ...nameplates, ...validSkus_GLFBL, ...validSkus_bracelet];
