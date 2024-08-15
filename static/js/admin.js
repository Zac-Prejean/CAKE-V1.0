let originalTableContent;   
  
function reloadPage() {    
  location.reload();    
}    
    
setTimeout(reloadPage, 180000); // 6000 milliseconds = 1 minute  
  
document.addEventListener('DOMContentLoaded', fetchDesignedStatus);    

function onArchiveButtonClick() {  
  const archiveButton = document.getElementById("archiveButton");  
  
  if (archiveButton.textContent === "ARCHIVE") {  
    archiveButton.textContent = "STATUS";  
    loadTxtFilesDropdown("archive");  
  } else {  
    archiveButton.textContent = "ARCHIVE";  
    loadTxtFilesDropdown("status");  
  }  
}  
  
// Add this line inside your `DOMContentLoaded` event listener  
archiveButton.addEventListener("click", onArchiveButtonClick); 


function fetchDesignedStatus(selectedFile) {   
  let lineCountElement;     
  if (selectedFile instanceof Event) {    
    return;    
  }    
  
  function getBackgroundColor(status) {    
    switch (status) {    
      case 'Designed':    
        return '#736B99';    
      case 'Scanned-In':    
        return '#9094CC';    
      case 'Printed':    
        return '#ABBDFF';    
      case 'Scanned-Out':    
        return '#B38EDE';    
      case 'Cubby':    
        return '#BF5F97';    
      case 'Shipped':    
        return '#CC5566';    
      default:    
        return '';    
    }    
  }    
    
  fetch(`/get_designed_status/${encodeURIComponent(selectedFile)}`)  
  .then(response => response.json())  
  .then(data => {  
    const tableBody = document.getElementById('designed-status-table').getElementsByTagName('tbody')[0];  
    tableBody.innerHTML = '';  
    if (data.error) {  
      const errorRow = tableBody.insertRow();  
      const errorCell = errorRow.insertCell(0);  
      errorCell.colSpan = 9;  
      errorCell.innerText = data.error;  
    } else {  
      data.content.forEach(line => {  
        const [itemID, orderNumber, itemName, totalQty, skuPart, batch, status, date, cubby] = line.split('_');  
        const sku = `${skuPart}`.replace('BLABEL', '');  
        const lastScan = `${date}`.trim();  
  
        const row = tableBody.insertRow();  
        row.insertCell().innerText = itemID;  
        row.insertCell().innerText = orderNumber;  
        const itemNameCell = row.insertCell();  
        itemNameCell.innerHTML = `<a href="https://zstat.zazzle.com/order/${orderNumber}" target="_blank";">${itemName}</a>`;  
  
        const statusCell = row.insertCell();  
  
        // Check if the selected file is from the 'archive' folder  
        const isArchive = selectedFile.includes("archive");  
  
        if (!isArchive) {  
          const statusDropdown = document.createElement('select');  
  
          statusDropdown.innerHTML = `  
            <option value="Designed" ${status === 'Designed' ? 'selected' : ''}>Designed</option>  
            <option value="Scanned-In" ${status === 'Scanned-In' ? 'selected' : ''}>Scanned-In</option>  
            <option value="Printed" ${status === 'Printed' ? 'selected' : ''}>Printed</option>  
            <option value="Scanned-Out" ${status === 'Scanned-Out' ? 'selected' : ''}>Scanned-Out</option>  
            <option value="Cubby" ${status === 'Cubby' ? 'selected' : ''}>Cubby</option>  
            <option value="Shipped" ${status === 'Shipped' ? 'selected' : ''}>Shipped</option>  
          `;  
  
          function updateDropdownBackgroundColor() {  
            const selectedOption = statusDropdown.options[statusDropdown.selectedIndex];  
            statusDropdown.style.backgroundColor = getBackgroundColor(selectedOption.value);  
          }  
  
          updateDropdownBackgroundColor();  
  
          statusDropdown.onchange = function () {  
            updateStatus(itemID, orderNumber, itemName, this.value);  
            updateDropdownBackgroundColor();  
          };  
  
          statusCell.appendChild(statusDropdown);  
        } else {  
          // If it's an archive file, display only the status text  
          statusCell.innerText = status;  
        }  
  
        row.insertCell().innerText = lastScan;  
        row.insertCell().innerText = sku;  
        row.insertCell().innerText = totalQty;  
        row.insertCell().innerText = cubby;  
        row.insertCell().innerText = batch;  
      });

      lineCountElement = document.getElementById('line-count-indicator');    
      if (lineCountElement) {    
        lineCountElement.innerText = `Total Items: ${data.content.length}`;    
      }  
    }  
  })  
  .catch(error => {  
    console.error('Error fetching designed status:', error);  
  });  
}  

  
function loadTxtFilesDropdown(folder = "status") {  
  fetch(`/get_txt_files/${folder}`)  
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
  
document.addEventListener('DOMContentLoaded', () => {  
});  
window.onload = function() {  
  loadTxtFilesDropdown();  
}; 
  
function searchItemTag(searchValue) {  
  const table = document.getElementById('designed-status-table');  
  const rows = table.getElementsByTagName('tr');  
  
  // Store original table content before the search, starting from the second row  
  if (!originalTableContent) {  
    originalTableContent = Array.from(rows).slice(1).map(row => row.cloneNode(true));  
  }  
  
  // Convert searchValue to lowercase  
  searchValue = searchValue.toLowerCase();  
  
  for (let i = 1; i < rows.length; i++) {  
    const cells = rows[i].getElementsByTagName('td');  
    const itemIdCell = cells[0];  
    const orderNumberCell = cells[1];  
    const itemNameCell = cells[2];  
    const skuCell = cells[5];  
    const statusCell = cells[3];  
  
    // Get the selected value from the <select> element and convert it to lowercase  
    const statusValue = statusCell.querySelector('select') ? statusCell.querySelector('select').value.toLowerCase() : statusCell.innerText.toLowerCase();  
  
    if (itemIdCell && orderNumberCell) {  
      if (itemIdCell.innerText.toLowerCase().indexOf(searchValue) > -1 || orderNumberCell.innerText.toLowerCase().indexOf(searchValue) > -1 || itemNameCell.innerText.toLowerCase().indexOf(searchValue) > -1 || skuCell.innerText.toLowerCase().indexOf(searchValue) > -1 || statusValue.indexOf(searchValue) > -1) {  
        rows[i].style.display = '';  
      } else {  
        rows[i].style.display = 'none';  
      }  
    }  
  }  
}  

function restoreOriginalTable() {  
  if (originalTableContent) {  
    const table = document.getElementById('designed-status-table');  
    const tbody = table.getElementsByTagName('tbody')[0];  
    tbody.innerHTML = '';  
  
    originalTableContent.forEach(row => {  
      tbody.appendChild(row);  
    });  
  
    originalTableContent = null;  
  }  
} 
  
function updateStatus(itemID, order_number, itemName, new_status) {  
  const formData = new FormData();  
  formData.append('itemID', itemID);  
  formData.append('order_number', order_number);  
  formData.append('itemName', itemName);  
  formData.append('new_status', new_status);  
  
  const selectedFile = document.getElementById('txt-files-dropdown').value;  
  
  fetch(`/update_status/${encodeURIComponent(selectedFile)}`, {  
    method: 'POST',  
    body: formData,  
  })  
    .then(response => {  
      response  
        .clone()  
        .text()  
        .then(text => console.log('Raw response text:', text));  
      return response.json();  
    })  
    .then(data => {  
      if (data.message) {  
        console.log(data.message);  
      } else if (data.error) {  
        console.error(data.error);  
      }  
    })  
    .catch(error => {  
      console.error('Error updating status:', error);  
    });  
}  
