


function reloadPage() { 
  setTimeout(() => {  
    location.reload();  
  }, 1000); // Wait for 1 second before reloading 
}  
  
setTimeout(reloadPage, 90000); // Reload every 90 seconds

function startBackupScheduler() {  
  if (window.location.pathname === '/cubbysystem') {
    $.get('/cubbysystem', { start_backup: 'true' });  
  }  
}  

function stopBackupScheduler() {  
  if (window.location.pathname === '/cubbysystem' && document.hidden) {  
    $.get('/stop_backup');  
  }  
} 

window.addEventListener('load', startBackupScheduler);  

// SORT SCANNED NUMBERS
function organizeNumbers(scannedNumbers) {    
  const boxes = {};    
  const numberPattern = /^\d{8}_\d+_\d+_\d+_\d{2}-\d{2}-\d{4} \d{2}:\d{2}$/;     
      
  for (const numberWithDate of scannedNumbers) {      
    // Split the scanned number and date      
    const [number, date] = numberWithDate.split(',');        
      
    // Check if the numberWithDate matches the pattern      
    if (numberPattern.test(number + '_' + date)) {      
      const orderNumber = number.split('_')[1];      
      if (!boxes[orderNumber]) {      
        boxes[orderNumber] = [];      
      }      
      boxes[orderNumber].push(number + ',' + date);      
    }      
  }      
  return boxes;      
}  

// BOX MODAL
async function getImagePath(itemNumber, side) {  
  const selectedFilename = document.getElementById("txt-files-dropdown").value;  
  const response = await fetch(`/get_image_data/${itemNumber}/${selectedFilename}`);  
  if (response.ok) {  
    const data = await response.json();  
    const imageFilename = data.filename; // Replace 'filename' with the correct property name returned from the server  
    const imagePath = `/images/${imageFilename}_${side}.png`;  
    return imagePath;  
  } else {  
    return null;  
  }  
} 

// async function showPreviewModal(itemNumber) {  
//   const side = 'front'; // You can change this based on your requirements  
//   const imagePath = await getImagePath(itemNumber, side);  
//   if (imagePath) {  
//     document.getElementById('previewImage').src = imagePath;  
//     $('#previewModal').modal('show');  
//   }  
// } 

function showBoxInfo(boxNumber, orderNumber, totalQuantity, firstScannedTime) { 
  document.getElementById('boxInfoNumber').innerText = boxNumber;  
  const boxInfoOrderNumber = document.getElementById('boxInfoOrderNumber');  
  boxInfoOrderNumber.innerHTML = `<a href="https://zstat.zazzle.com/order/${orderNumber}" target="_blank" class="red-text" text-decoration: none;">${orderNumber}</a>`;
  $('#boxInfoModal').modal('show'); 
  
  // Show the complete button if the condition is met and hide the delete button  
  if (scannedOrders[orderNumber] === parseInt(totalQuantity, 10)) {  
      document.getElementById('completeBoxBtn').style.display = 'inline-block';  
      document.getElementById('deleteBoxBtn').style.display = 'none';  
  } else {  
      document.getElementById('completeBoxBtn').style.display = 'none';  
      document.getElementById('deleteBoxBtn').style.display = 'inline-block';  
  }  
  document.getElementById('boxInfoFirstScannedTime').innerText = firstScannedTime; 
  
  // Add scanned items display  
  const scannedItemsContainer = document.getElementById('scannedItems');  
  scannedItemsContainer.innerHTML = '';  
  const boxItems = scannedNumbers.filter(numberWithDate => {  
    const [number] = numberWithDate.split(',');  
    const boxNum = number.split('_')[3];  
    return boxNum == boxNumber;  
  }).map(numberWithDate => numberWithDate.split(',')[0].split('_')[0]);  
  
  for (const item of boxItems) {  
    const itemElement = document.createElement('p');  
    itemElement.textContent = item;  
    itemElement.style.cursor = 'pointer'; 
    // itemElement.addEventListener('click', () => showPreviewModal(item));  
    scannedItemsContainer.appendChild(itemElement);  
  }  
}  

// CLOSE BUTTON
document.querySelectorAll('.closeModalBtn').forEach(function (closeBtn) {  
  closeBtn.addEventListener('click', function () {  
      if ($('#boxNumberModal').hasClass('show')) {  
          $('#boxNumberModal').modal('hide');  
      } else if ($('#boxInfoModal').hasClass('show')) {  
          $('#boxInfoModal').modal('hide');  
          $('input[type="search"]').focus();  
      } else if ($('#boxNumberModal').hasClass('show')) {  
          $('#boxNumberModal').modal('hide');  
          $('input[type="search"]').focus();  
      } else if ($('#alreadyScannedModal').hasClass('show')) {  
      $('#alreadyScannedModal').modal('hide');  
      } else if ($('#notScannedModal').hasClass('show')) {    
        $('#notScannedModal').modal('hide');  
      } else if ($('#invalidNumberModal').hasClass('show')) {    
        $('#invalidNumberModal').modal('hide');   
      }   
  });  
});  
document.addEventListener('keydown', function (event) {  
  if (event.key === 'Enter' || event.key === 'Escape') {  
      if ($('#boxNumberModal').hasClass('show')) {  
          $('#boxNumberModal').modal('hide');  
      } else if ($('#boxInfoModal').hasClass('show')) {  
          $('#boxInfoModal').modal('hide');  
          $('input[type="search"]').focus();   
      }  else if ($('#deleteWarningModal').hasClass('show')) {  
        $('#deleteWarningModal').modal('hide');  
        $('input[type="search"]').focus();  
    }  
  }  
}); 
document.getElementById('cancelDeleteBtn').addEventListener('click', function () {  
  $('#deleteWarningModal').modal('hide');  
  $('#boxInfoModal').modal('hide');  
  $('input[type="search"]').focus();  
}); 
document.getElementById('confirmCompleteBtn').addEventListener('click', async function () {  
  const boxNumber = parseInt(document.getElementById('completeBoxNumber').innerText, 10);  
  completeBox(boxNumber);  
  $('#completeWarningModal').modal('hide');  
  $('#boxInfoModal').modal('hide');  

  // Get the box items from the scanned items container  
  const scannedItemsContainer = document.getElementById('scannedItems');  
  const scannedItems = Array.from(scannedItemsContainer.children);  

  for (const itemElement of scannedItems) {  
    console.log("Scanned item textContent:", itemElement.textContent);  
} 

  // Get unique order numbers in the box  
  const orderNumbers = new Set(scannedItems.map(itemElement => itemElement.textContent));  

  console.log("Order numbers:", Array.from(orderNumbers));

  // Update the status for each unique order number in the box  
  for (const orderNumber of orderNumbers) {  
      // Call the updateStatus function for all items in the order  
      const selectedFilename = document.getElementById("txt-files-dropdown").value;  
      const updated = await updateStatus(orderNumber, "", "", "Shipped", selectedFilename);  
      if (!updated) {  
          console.error(`Failed to update status for order: ${orderNumber}`);  
      }  
  }  
});

$('#boxNumberModal, #boxInfoModal').on('hidden.bs.modal', function () {  
  $('input[type="search"]').focus();  
}); 

function removeBox(boxNumber) {  
  // Remove the box from the scannedNumbers array  
  scannedNumbers = scannedNumbers.filter(numberWithDate => {  
      const number = numberWithDate.split(',')[0];  
      // Ensure that only the specific box is removed  
      return !number.endsWith(`_${boxNumber}`);  
  });  

  // Update the boxes display  
  const boxes = organizeNumbers(scannedNumbers);  
  displayBoxes(boxes);  

  // Update the scanned numbers on the server  
  $.post(addBoxUrl, {scanned_number: `DELETE_${boxNumber}`}, function (data) {  
  });  
} 

 
// DELETE BUTTON
function deleteBox(boxNumber) {  
  // Show the delete warning modal and set the box number  
  document.getElementById('deleteBoxNumber').innerText = boxNumber;  
  $('#deleteWarningModal').modal('show');  
}
 
// COMPLETE BUTTON
document.getElementById('confirmCompleteBtn').addEventListener('click', function () {  
  const boxNumber = parseInt(document.getElementById('completeBoxNumber').innerText, 10);  
  completeBox(boxNumber);  
  $('#completeWarningModal').modal('hide');  
});  

document.getElementById('cancelCompleteBtn').addEventListener('click', function () {  
  $('#completeWarningModal').modal('hide');  
});  
document.getElementById('completeBoxBtn').addEventListener('click', function () {  
  const boxNumber = parseInt(document.getElementById('boxInfoNumber').innerText, 10);  
  showCompleteWarning(boxNumber);  
});  

function showCompleteWarning(boxNumber) {  
  document.getElementById('completeBoxNumber').innerText = boxNumber;  
  $('#completeWarningModal').modal('show');  
}   

function completeBox(boxNumber) {
  // Remove the box  
  removeBox(boxNumber);  

  // Close the modal  
  $('#boxInfoModal').modal('hide');  
}  

// BOX DISPLAYS  
const numberOfBoxes = 264;  

function daysDifference(firstScannedTime) {  
  const currentTime = new Date();  
  const scannedDate = new Date(firstScannedTime);  
  const timeDifference = Math.abs(currentTime - scannedDate);  
  const daysDifference = Math.ceil(timeDifference / (1000 * 60 * 60 * 24));  
  return daysDifference;  
} 

function createBoxes() {  
    const boxContainer = document.getElementById('boxContainer');  
  
    for (let i = 1; i <= numberOfBoxes; i++) {  
        const box = document.createElement('div');  
        box.id = `box${i}`;  
        box.classList.add('emptybox');  
        boxContainer.appendChild(box);  
    }  
}  
  
// Call the createBoxes function when the page loads  
window.addEventListener('DOMContentLoaded', createBoxes); 
function displayBoxes(boxes) {  
  let boxesInUse = 0;  
  
  // Clear all boxes  
  for (let i = 1; i <= 100; i++) {  
    const boxContainer = document.getElementById(`box${i}`);  
    if (boxContainer) {  
      boxContainer.className = 'emptybox';  
      boxContainer.innerHTML = '';  
    }  
  }  
  
  document.getElementById('boxesInUse').textContent = `${boxesInUse} BOXES`;  
  
  scannedOrders = {};  
  
  for (const orderNumber in boxes) {  
    let totalQuantity;  
    let boxIndex;  
    let firstScannedTime = null;  
  
    for (const orderDetail of boxes[orderNumber]) {  
      const [number, date] = orderDetail.split(',');  
      const [itemID, order, total, boxNumber] = number.split('_');  
      totalQuantity = total;  
      boxIndex = parseInt(boxNumber, 10);  
  
      if (firstScannedTime === null || new Date(date) < new Date(firstScannedTime)) {  
        firstScannedTime = date;  
      }  
      if (!scannedOrders[order]) {  
        scannedOrders[order] = 0;  
      }  
      scannedOrders[order]++;  
  
      const boxContainer = document.getElementById(`box${boxIndex}`);  
      boxContainer.className = 'box';  
  
      // Clear the existing content of the box container  
      boxContainer.innerHTML = '';  
  
      const colorBar = document.createElement('div');  
      colorBar.className = 'color-bar';  
      boxContainer.appendChild(colorBar);  
  
      const boxLabel = document.createElement('h4');  
      boxLabel.className = 'box-number box-number-overlay';  
      boxLabel.textContent = `${boxIndex}`;  
      boxContainer.appendChild(boxLabel);  
  
      // Add order number display to each box  
      const orderNumberLabel = document.createElement('p');  
      orderNumberLabel.textContent = orderNumber.slice(-7); //show last 7 digits of order 
      boxContainer.appendChild(orderNumberLabel);  
  
      const quantityLabel = document.createElement('p');  
      quantityLabel.textContent = `${scannedOrders[orderNumber]}/${totalQuantity}`;  
      boxContainer.appendChild(quantityLabel);  
  
      if (scannedOrders[orderNumber] === parseInt(totalQuantity, 10)) {  
        colorBar.style.backgroundColor = '#44AF51';  
      } else if (daysDifference(firstScannedTime) > 1 && daysDifference(firstScannedTime) <= 2) {  
        colorBar.style.backgroundColor = '#F3A116';  
      } else if (daysDifference(firstScannedTime) > 2) {  
        colorBar.style.backgroundColor = '#D6324D';  
      }  
  
      // Update the onclick attribute to show the scanned order number and date  
      boxContainer.setAttribute('onclick', `showBoxInfo(${boxIndex}, '${orderNumber}', '${totalQuantity}', '${firstScannedTime}')`);  
    }  
  }  
  
  // Update the boxesInUse variable after the loop  
  boxesInUse = Object.keys(boxes).length;  
  
  document.getElementById('boxesInUse').textContent = `${boxesInUse} BOXES USED`;  
}  
  

const addBoxUrl = "/add_box";  
let scannedNumbers = [];  
let nextAvailableBox = 1;
let scannedOrders = {};  


// Fetch the scanned numbers from the server  
$.get('/get_scanned_numbers', function(data) {  
  scannedNumbers = data;  
  const boxes = organizeNumbers(scannedNumbers);  
  displayBoxes(boxes);  
});  

$('form.search-bar').on('submit', function (event) {    
  event.preventDefault();    
    
  // Define the number pattern    
  const numberPattern = /^\d{8}$/;    
    
  const scannedNumber = $('input[type="search"]').val();    
  const addBoxUrl = $(this).data('addBoxUrl');    
    
  // Validate scanned number format    
  if (!numberPattern.test(scannedNumber)) {    
    $('#invalidNumberModal').modal('show');     
    $('input[type="search"]').val('');    
    return;    
  }      
    
  // Get the selected txt file from the dropdown    
  const selectedTxtFile = $('#txt-files-dropdown').val();  
  
  // Fetch the total quantity from the matched number in the selected txt file    
  $.get(`/get_order_and_total_quantity/${scannedNumber}/${selectedTxtFile}`, function (data) {    
    if (data) {    
        const [itemID] = scannedNumber.split('_');    
        const orderNumber = data.order_number;    
        const totalQuantity = data.total_quantity;    
        const scannedWithBox = `${itemID}_${orderNumber}_${totalQuantity}_`;    
  
        // Rest of the code using scannedWithBox    
        if (scannedNumbers.some(number => number.startsWith(scannedWithBox))) {    
            // Find the box number where the order was already scanned    
            const scannedBox = scannedNumbers.find(number => number.startsWith(scannedWithBox));    
            const boxNumber = scannedBox.split(',')[0].split('_')[3];  
   
  
            // Update the scanned box number in the modal and show it    
            $('#scannedBoxNumber').text(boxNumber);    
            $('#alreadyScannedModal').modal('show');    
  
            // Clear the search bar after the scan    
            $('input[type="search"]').val('');    
        } else {  
            // Show the notScannedModal if the scanned number is not found in the scannedNumbers array  
            $('#notScannedModal').modal('show');  
            $('input[type="search"]').val('');  
        }  
    } else {    
        // Show the notScannedModal if the scanned number is not found in the txt file  
        $('#notScannedModal').modal('show');  
        $('input[type="search"]').val('');  
    }    
  });  
});

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

async function fetchDesignedStatus(fileName) {
  
  fetch(`/get_designed_status/${fileName}`)  
    .then(response => response.json())  
    .then(data => {  
      console.log('Designed status:', data);  
    })  
    .catch(error => {  
      console.error('Error fetching designed status:', error);  
    });  
}   

async function updateStatus(order_number, item_id, itemName, status, filename) {  
  const url = `/update_all_items_status/${filename}`;  

  // Prepare the data to be sent in the request body  
  const data = new FormData();  
  data.append('order_number', order_number);  
  data.append('new_status', status);  
  data.append('cubby_number', ""); // Assuming you don't need a cubby_number for this request  

  console.log("URL:", url);  
  console.log("Order number:", order_number);  
  console.log("New status:", status);  
  console.log("Cubby number:", ""); // Assuming you don't need a cubby_number for this request  

  // Send the fetch request  
  const response = await fetch(url, {  
      method: 'POST',  
      body: data,  
  });  

  if (!response.ok) {  
      throw new Error(`Failed to update status: ${response.statusText}`);  
  }  

  return response.json();  
}  
