


let imagePaths = {};  
let currentImage = 'front';  
  
async function getImagePath(itemID, itemName, side) {  
    const imagePath = `/images/${itemID}_${itemName}_${side}.png`;  
    try {  
        const response = await fetch(imagePath);  
        if (response.ok) {  
            return imagePath;  
        } else {  
            return null;  
        }  
    } catch (error) {  
        console.error('Error fetching image path:', error);  
        return null;  
    }  
}  
  
async function displayItemInfo(scannedNumber) {  
    const item_id = scannedNumber;
    
    // Add the filename to the request body   
    const filename = document.getElementById('txt-files-dropdown').value; 

    // Fetch the designed status using both filename and scannedNumber   
    const getStatusResponse = await fetch('/get_status', {  
        method: 'POST',  
        headers: {  
            'Content-Type': 'application/x-www-form-urlencoded',  
        },  
        body: `scanned_number=${scannedNumber}&filename=${filename}`,  
    });  
    const getStatusText = await getStatusResponse.text();  
      
    if (getStatusText.toUpperCase() !== "DESIGNED") {  
        showModal(getStatusText);  
        return;  
    }  
      
    document.getElementsByName('scanned_number')[0].value = "";  
      
    try { 
        // Fetch the designed status using filename  
        const responseFilename = await fetch(`/get_designed_status/${filename}`);  
        const dataFilename = await responseFilename.json();  
          
        const scannedItem = dataFilename.content.find(line => line.startsWith(`${item_id}_`));  
        if (!scannedItem) {  
            handleImagePaths(null, null, null);  
            document.getElementById('item-description').innerText = "Order details not found";  
            return;  
        }  
          
        const [_, order_number, itemName, , sku] = scannedItem.split('_');  
          
        const responseScannedNumber = await fetch(`/get_designed_status/${itemName}`);  
        const dataScannedNumber = await responseScannedNumber.json();  
          
        const data = { ...dataFilename, content: [...(dataFilename.content || []), ...(dataScannedNumber.content || [])] };  
          
        if (!data.content || data.error) {  
            handleImagePaths(null, itemName, filename);  
            document.getElementById('item-description').innerText = "Order details not found";  
            return;  
        }  
          
        const itemDetailsResponse = await fetch('/dtg_item_description.json');  
        const itemDetailsData = await itemDetailsResponse.json();  
          
        const itemDescription = itemDetailsData[sku] || "Item details not found";  
        document.getElementById('item-description').innerText = itemDescription;  
          
        handleImagePaths(item_id, itemName, filename);  
        await updateStatus(order_number, item_id, itemName, "Scanned-In");  
    } catch (error) {  
        console.error('Error fetching text file:', error);  
    }  
 
    async function updateStatus(order_number, item_id, itemName, new_status) {  
        const formData = new FormData();  
        formData.append('order_number', order_number);  
        formData.append('itemID', item_id);  
        formData.append('itemName', itemName);  
        formData.append('new_status', new_status);  
        formData.append('scanned', 'true');  
        
        const updateStatusResponse = await fetch(`/update_status/${filename}`, {  
            method: 'POST',  
            body: formData,  
        });  
        
        const updateStatusText = await updateStatusResponse.text();  
    }  
}   
async function handleImagePaths(itemID, itemName, filename) {  
    getImagePath(itemID, itemName, 'front').then(imageFrontPath => {  
        getImagePath(itemID, itemName, 'back').then(imageBackPath => {  
            imagePaths.front = imageFrontPath;  
            imagePaths.back = imageBackPath;  
              
            if (imageFrontPath && imageBackPath) {  
                document.getElementById("left-arrow").style.display = "block";  
                document.getElementById("right-arrow").style.display = "block";  
            } else {  
                document.getElementById("left-arrow").style.display = "none";  
                document.getElementById("right-arrow").style.display = "none";  
            }  
              
            console.log('Image front path:', imageFrontPath);  
            console.log('Image back path:', imageBackPath);  
            if (imageFrontPath && imageBackPath) {  
                updateImage('FRONT', imageFrontPath, 'FRONT and BACK');  
            } else if (imageBackPath) {  
                updateImage('BACK', imageBackPath, 'BACK');  
            } else if (imageFrontPath) {  
                updateImage('FRONT', imageFrontPath, 'FRONT');  
            } else {  
                document.getElementById('item-image').innerHTML = `<img src="${blankImagePath}" alt="Blank Image">`;  
                document.getElementById('item-description').innerText = "Order details not found";  
            }  
        });  
    });  
}  
  
function updateImage(bannerText, imagePath, useIndicatorText) {  
    document.getElementById('item-image').innerHTML = `<img src="${imagePath}" alt="Item Image">`;  
    document.getElementById('banner-text').innerText = bannerText;  
    document.getElementById("useIndicator").textContent = useIndicatorText;  
}  
  
function switchImage(direction) {  
    if (direction === 'next') {  
        toggleImage();  
    } else if (direction === 'previous') {  
        toggleImage();  
    }  
}  
  
function toggleImage() {  
    if (currentImage === 'front' && imagePaths.back) {  
        currentImage = 'back';  
        document.getElementById('item-image').innerHTML = `<img src="${imagePaths.back}" alt="Item Image">`;  
        document.getElementById('banner-text').innerText = 'BACK';  
    } else if (currentImage === 'back' && imagePaths.front) {  
        currentImage = 'front';  
        document.getElementById('item-image').innerHTML = `<img src="${imagePaths.front}" alt="Item Image">`;  
        document.getElementById('banner-text').innerText = 'FRONT';  
    }  
}  
  
// BATCH DROPDOWN  
document.addEventListener('DOMContentLoaded', loadTxtFilesDropdown);  
function loadTxtFilesDropdown() {  
    fetch('/get_txt_files')  
        .then(response => response.json())  
        .then(files => {  
            const dropdown = document.getElementById('txt-files-dropdown');  
            dropdown.innerHTML = '';  
            files.forEach(file => {  
                const option = document.createElement('option');  
                option.value = file;  
                option.innerText = file;  
                dropdown.appendChild(option);  
            });  
              
            dropdown.addEventListener('change', function () {  
                fetchDesignedStatus(this.value);  
            });  
              
            if (files.length > 0) {  
                fetchDesignedStatus(files[0]);  
            }  
        })  
        .catch(error => {  
            console.error('Error fetching txt files:', error);  
        });  
}  
  
function fetchDesignedStatus(fileName) {  
    fetch(`/get_designed_status/${fileName}`)  
    .then(response => response.json())  
    .then(data => {  
        console.log('Designed status:', data);  
    })  
    .catch(error => {  
        console.error('Error fetching designed status:', error);  
    });  
}  
  
function showModal(status) {  
    const modal = document.getElementById("myModal");  
    const span = document.getElementsByClassName("close")[0];  
      
    document.getElementById("modal-text").innerHTML = `This item has processed the <a href="#" class="status-link">${status}</a> stage. Check with supervisor.`;  
    modal.style.display = "block";  
      
    span.onclick = function () {  
        modal.style.display = "none";  
    };  
      
    window.onclick = function (event) {  
        if (event.target == modal) {  
            modal.style.display = "none";  
        }  
    };  
}  
