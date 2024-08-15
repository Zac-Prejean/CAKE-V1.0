



 
let imagePaths = {};
let globalImagePaths = {};   
let currentImage = 'front';

async function getImagePath(itemID, itemName, side) {  
    const imagePath = `/images/${itemID}_${itemName}_${side}_mockup.png`;  
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
    const filename = document.getElementById('txt-files-dropdown').value;  
  
    const getStatusResponse = await fetch('/get_status', {  
        method: 'POST',  
        headers: {  
            'Content-Type': 'application/x-www-form-urlencoded',  
        },  
        body: `scanned_number=${scannedNumber}&filename=${filename}`,  
    });  
    const getStatusText = await getStatusResponse.text();  
  
    if (getStatusText.toUpperCase() !== "PRINTED") {  
        showModal(getStatusText);  
        return;  
    }  
  
    document.getElementsByName('scanned_number')[0].value = "";  
  
    try {  
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
  
        const combinedContent = [...(dataFilename.content || []), ...(dataScannedNumber.content || [])];  
        const matchingContent = combinedContent.filter(line => line.startsWith(scannedNumber + "_"));  
  
        if (!matchingContent.length) {  
            handleImagePaths(scannedNumber, filename);  
            document.getElementById('item-description').innerText = "Order details not found";  
            return;  
        }  
  
        const maxTotalQtyLine = matchingContent.reduce((maxLine, currentLine) => {  
            const maxTotalQty = parseInt(maxLine.split("_")[2], 10);  
            const currentTotalQty = parseInt(currentLine.split("_")[2], 10);  
            return currentTotalQty > maxTotalQty ? currentLine : maxLine;  
        });  
  
        const [, , , orderTotalQty] = maxTotalQtyLine.split('_').map(s => s.trim());  
  
        const confirmButton = document.getElementById('confirmButton');  
        confirmButton.replaceWith(confirmButton.cloneNode(true));  
        document.getElementById('confirmButton').addEventListener('click', async function () {  
            if (orderTotalQty == 1) {  
                showSingleModal("Are you ready to ship?", "CONFIRM", "CANCEL", item_id, itemName, order_number, async function () {  
                    await updateStatus(order_number, item_id, itemName, "Scanned-Out", filename);  
                }, async function () {  
                    await updateStatus(order_number, item_id, itemName, "Scanned-Out", filename);  
                });  
            } else if (orderTotalQty > 1) {  
                const currentStatusResponse = await fetch('/get_status', {  
                    method: 'POST',  
                    headers: {  
                        'Content-Type': 'application/x-www-form-urlencoded',  
                    },  
                    body: `scanned_number=${scannedNumber}&filename=${filename}`,  
                });  
                const currentStatusText = await currentStatusResponse.text();  
  
                if (currentStatusText.toUpperCase() === "PRINTED") {  
                    showQuantityModal("Add to cubbyhole", "CONFIRM", null, item_id, itemName, null, async function () {  
                        const boxNumber = await addToCubby(order_number, item_id, itemName, orderTotalQty, filename);  
                        await updateStatus(order_number, item_id, itemName, "Cubby", filename, boxNumber);  
                    // Show the BoxNumberModal after a delay  
                    setTimeout(() => { 
                        showBoxNumberModal(boxNumber);
                        document.getElementById("quantityModal").style.display = "none";  
                    }, 200); 
                });  
                }  
            }  
        });  
  
        const itemDetailsResponse = await fetch('/dtg_item_description.json');  
        const itemDetailsData = await itemDetailsResponse.json();  
        const itemDescription = itemDetailsData[sku] || "Item details not found";  
        document.getElementById('item-description').innerText = itemDescription;  
  
        handleImagePaths(item_id, itemName, filename, async (callbackImagePaths) => {  
            if (callbackImagePaths.front && callbackImagePaths.back) {  
                showNoticeModal(async (action) => {  
                    if (action === 'continue') {  
                        await updateStatus(order_number, item_id, itemName, "Printed", filename);  
                    } else if (action === 'design') {  
                        await updateStatus(order_number, item_id, itemName, "Designed", filename);  
                    }  
                });  
            } else {  
                await updateStatus(order_number, item_id, itemName, "Printed", filename);  
            }  
            if (typeof callback === 'function') {  
                callback(imagePaths);  
            }  
        });  
    } catch (error) {  
        console.error('Error fetching text file:', error);  
    }  
}  
  
async function updateStatus(order_number, item_id, itemName, new_status, filename, cubby_number) {  
    const formData = new FormData();  
    formData.append('order_number', order_number);  
    formData.append('itemID', item_id);  
    formData.append('itemName', itemName);  
    formData.append('new_status', new_status);  
    formData.append('scanned', 'true');  
    formData.append('cubby_number', cubby_number); // Add the cubby_number to formData  
  
    const updateStatusResponse = await fetch(`/update_status/${filename}`, {  
        method: 'POST',  
        body: formData,  
    });  
  
    const updateStatusText = await updateStatusResponse.text();  
} 
    
function showNoticeModal(onAction) {  
    const noticeModal = document.getElementById("noticeModal");  
    const continueButton = document.getElementById("continueButton");  
    const designButton = document.getElementById("designButton");  
    
    noticeModal.style.display = "block";  
    
    continueButton.onclick = function () {  
        noticeModal.style.display = "none";  
        if (typeof onAction === 'function') {  
            onAction('continue');  
        }  
    };  
    
    designButton.onclick = function () {  
        noticeModal.style.display = "none";  
        if (typeof onAction === 'function') {  
            onAction('design');  
        }  
    };  
    
    window.onclick = function (event) {  
        if (event.target == noticeModal) {  
            noticeModal.style.display = "none";  
        }  
    };  
}  

let addedItems = [];  

function showQuantityModal(message, confirmText, itemId, itemName, orderNumber, onConfirm, onClose) {  
    const modal = document.getElementById("quantityModal");  
    const shipButton = document.getElementById("quantity-shipButton");  
        
    if (!modal) {  
        console.error('Quantity Modal element not found');  
        return;  
    }  
    
    // Clear any previous content or event listeners  
    shipButton.innerText = "";  
    shipButton.onclick = null;  
    shipButton.style.display = "inline"; // Ensure the confirm button is displayed  
        
    document.getElementById("quantity-modal-message").innerHTML = message;  
    shipButton.innerText = confirmText;  
        
    modal.style.display = "block";  
        
    shipButton.onclick = async function () {  
        if (orderNumber) {
            shipButton.style.display = "none"; // Hide the confirm button  
            if (typeof onClose === 'function') {  
                await onClose(); // Call the onClose callback to update the status after the modal is closed  
            }  
        } else {  
            if (addedItems.includes(itemId)) {  
                // Display a warning modal when the item is already added  
                showModal("Cubby");  
                return;  
            }  
            addedItems.push(itemId);  
            if (typeof onConfirm === 'function') {  
                await onConfirm(); // Execute the callback function when the confirm button is clicked  
            }  
            modal.style.display = "none"; // Hide the modal after confirming  
        }  
    };  
        
    window.onclick = function (event) {  
        if (event.target == modal) {  
            modal.style.display = "none";  
        }  
    };  
} 

function showSingleModal(message, confirmText, cancelText, itemId, itemName, orderNumber, onConfirm, onClose) {  
    const modal = document.getElementById("singleModal");  
    const shipButton = document.getElementById("shipButton");  
    const cancelButton = document.getElementById("cancelButton");  
        
    if (!modal) {  
        console.error('Modal element not found');  
        return;  
    }  
    
    // Clear any previous content or event listeners  
    shipButton.innerText = "";  
    cancelButton.innerText = "";  
    shipButton.onclick = null;  
    cancelButton.onclick = null;  
    shipButton.style.display = "inline"; // Ensure the confirm button is displayed  
        
    document.getElementById("modal-message").innerHTML = message;  
    shipButton.innerText = confirmText;  
        
    if (cancelText) {  
        cancelButton.style.display = "inline";  
        cancelButton.innerText = cancelText;  
    } else {  
        cancelButton.style.display = "none";  
    }  
        
    modal.style.display = "block";  
        
    shipButton.onclick = async function () {  
        if (orderNumber) {  
            document.getElementById("modal-message").innerHTML = `ItemID: <a href="https://zstat.zazzle.com/order/${orderNumber}" target="_blank">${itemName}</a>`; // Update modal-message with ItemID and hyperlink  
            shipButton.style.display = "none"; // Hide the confirm button  
            if (typeof onClose === 'function') {  
                await onClose(); // Call the onClose callback to update the status after the modal is closed  
            }  
        } else {  
            if (addedItems.includes(itemId)) {  
                // Display a warning modal when the item is already added  
                showModal("Cubby");  
                return;  
            }  
            addedItems.push(itemId);  
            if (typeof onConfirm === 'function') {  
                await onConfirm(); // Execute the callback function when the confirm button is clicked  
            }  
            modal.style.display = "none"; // Hide the modal after confirming  
        }  
    };  
        
    cancelButton.onclick = function () {  
        modal.style.display = "none";  
    };  
        
    window.onclick = function (event) {  
        if (event.target == modal) {  
            modal.style.display = "none";  
        }  
    };  
}       
              
const addBoxUrl = "/add_box";

let scannedNumbers = [];  
  
// Fetch the scanned numbers from the server  
fetch('/get_scanned_numbers')  
    .then(response => response.json())  
    .then(data => {  
        scannedNumbers = data;  
    })  
    .catch(error => {  
        console.error('Error fetching scanned numbers:', error);  
    });  
  
  
async function addToCubby(order_number, item_id, itemName, totalQuantity, filename) {      
    // Fetch the latest scanned numbers from the server    
    const responseScannedNumbers = await fetch('/get_scanned_numbers');    
    scannedNumbers = await responseScannedNumbers.json();    
    
    // Find all boxes with the same order number      
    const existingBoxes = scannedNumbers.filter(numberWithDate => numberWithDate.split(',')[0].split('_')[1] === order_number);     

    let nextEmptyBox;    
  
    // If there are no existing boxes for the current order_number, find the next available empty box    
    if (existingBoxes.length === 0) {    
        nextEmptyBox = 1;    
        while (scannedNumbers.some(numberWithDate => numberWithDate.split(',')[0].endsWith(`_${nextEmptyBox}`))) {    
            nextEmptyBox++;    
        }    
    } else {    
        // If there are existing boxes for the current order_number, use the same box number    
        nextEmptyBox = existingBoxes[0].split(',')[0].split('_')[3];    
    }    
  
    const scanned_number = `${item_id}_${order_number}_${totalQuantity}_${nextEmptyBox}`;    
    const boxNumber = scanned_number.split('_')[3]; // Extract the boxNumber from the scanned_number     
  
    const response = await fetch(addBoxUrl, {    
        method: 'POST',    
        headers: {    
            'Content-Type': 'application/x-www-form-urlencoded',    
        },    
        body: `scanned_number=${item_id}_${order_number}_${totalQuantity}_${nextEmptyBox}&selected_txt_file=${filename}`,    
    });    
  
    const data = await response.json();    
    scannedNumbers = data;    
    return boxNumber;    
}  


async function handleImagePaths(itemID, itemName, filename, callback) {  
    const imageFrontPath = await getImagePath(itemID, itemName, 'front');  
    const imageBackPath = await getImagePath(itemID, itemName, 'back');  
      
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
  
    if (typeof callback === 'function') {  
        callback(imagePaths);  
    }  
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

// WARNING MODAL
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
  
  function showBoxNumberModal(boxNumber) {    
    const boxNumberModal = document.getElementById("boxNumberModal");    
    document.getElementById("boxNumber").innerText = boxNumber;  
    
    // Add a CSS class to the modal window to trigger the transition  
    boxNumberModal.classList.add("show-modal");  
    
    // Show the modal window after a short delay to allow the transition to take effect  
    setTimeout(function() {  
      $(boxNumberModal).modal("show");  
    }, 120);  
    
    const closeModalBtn = document.getElementsByClassName("closeModalBtn")[0];    
    closeModalBtn.onclick = function () {    
      $(boxNumberModal).modal("hide");    
    };    
  } 
