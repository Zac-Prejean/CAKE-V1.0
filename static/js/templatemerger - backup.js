
// Array to store the loaded PNGs
const loadedPNGs = [];

const fileInput = document.getElementById('file-input');
const previewArea = document.getElementById('preview-area');
const exportButton = document.getElementById('export-button');

// Add event listeners to the file input and export button
exportButton.addEventListener('click', handleExportButtonClick);

function handleExportButtonClick() {

  // DESK PLATES

  if (searchInput.getAttribute('data-selected-item') === 'desk-plates') {  

    const files = document.getElementById('file-input').files;
    if (files.length > 28) {
      alert('Error: You can only select up to 28 images.');
      return;
    }
    setTimeout(() => {

      const canvas = document.createElement('canvas');
      const ctx = canvas.getContext('2d');
      const canvasWidthInches = 24;
      const canvasHeightinches = 36;
      const dpi72 = 72.01558002 * 5;
      const canvasWidth = canvasWidthInches * dpi72;
      const canvasHeight = canvasHeightinches * dpi72;
      canvas.width = canvasWidth;
      canvas.height = canvasHeight;
      for (let i = 0; i < loadedPNGs.length; i++) {
        const loadedPNG = loadedPNGs[i];

        const positions = [ // [x, y]
            [1.03, 0.93],   [15.38, 0.93],  [1.03, 3.446],  [15.38, 3.446],
           [1.03, 5.962],  [15.38, 5.962],  [1.03, 8.478],  [15.38, 8.478],
          [1.03, 10.994], [15.38, 10.994],  [1.03, 13.51],  [15.38, 13.51],
          [1.03, 16.026], [15.38, 16.026], [1.03, 18.542], [15.38, 18.542],
          [1.03, 21.058], [15.38, 21.058], [1.03, 23.574], [15.38, 23.574],
           [1.03, 26.09],  [15.38, 26.09], [1.03, 28.606], [15.38, 28.606],
          [1.03, 31.122], [15.38, 31.122], [1.03, 33.638], [15.38, 33.638],
          [1.03, 36.154], [15.38, 36.154]
        ];

        let x, y, width, height;
        if (i < positions.length) {
          x = positions[i][0] * dpi72;
          y = positions[i][1] * dpi72;
          width = 8.08 * dpi72;
          height = 2 * dpi72;
        } else {
          x = i % 2 === 0 ? canvasWidth - (8 * dpi72) : canvasWidth / 24;
          y = Math.floor((i - 1) / 2) * (2 * dpi72) + canvasHeight / 36;
          width = 8.08 * dpi72;
          height = 2 * dpi72;
        }


        if (i < 28) {
          ctx.save();
          ctx.translate(x + width / 2, y + height / 2);
          ctx.rotate(Math.PI);
          ctx.scale(-1, 1);
          ctx.drawImage(loadedPNG, -width / 2, -height / 2, width, height);
          ctx.restore();
        } else {
          ctx.drawImage(loadedPNG, x, y, width, height);
        }
      }
      const dataURL = canvas.toDataURL('image/png', 1);
      const blob = dataURLToBlob(dataURL);
      const link = document.createElement('a');
      link.href = URL.createObjectURL(blob);
      link.download = 'desk_plates.png';
      link.click();
    }, 100);
  }

}

// Get the search input element and add an event listener  
const searchInput = document.getElementById('search-input');  
const searchResults = document.getElementById('search-results');  
searchInput.addEventListener('input', handleSearchInputChange);  
  

  
// Populate the search results dropdown  
function updateSearchResults(filter = '') {  
  searchResults.innerHTML = '';  
  const filteredItems = items.filter(item => item.text.toLowerCase().includes(filter.toLowerCase()));  
  filteredItems.forEach(item => {  
    const li = document.createElement('li');  
    li.id = item.id;  
    const a = document.createElement('a');  
    a.href = '#';  
    a.className = 'dropdown-item';  
    const img = document.createElement('img');  
    img.src = item.image;  
    img.width = 18;  
    img.height = 18;  
    img.className = 'd-inline-block align-center';  
    img.alt = `Click to add ${item.text}`;  
    a.appendChild(img);  
    a.appendChild(document.createTextNode(item.text));  
    li.appendChild(a);  
    searchResults.appendChild(li);  
  
    // Add click event listener to the item  
    li.addEventListener('click', function () {  
      searchInput.value = item.text;  
      searchInput.setAttribute('data-selected-item', item.id);  
      searchResults.innerHTML = ''; 
    });  
  });  
}  
  
// Handle search input change event  
function handleSearchInputChange(event) {  
  updateSearchResults(event.target.value);  
}  
  
// Update the search results when the page loads  
updateSearchResults();  

// Function to convert data URL to Blob
function dataURLToBlob(dataURL) {
  const binaryString = atob(dataURL.split(',')[1]);
  const arrayBuffer = new ArrayBuffer(binaryString.length);
  const view = new Uint8Array(arrayBuffer);
  for (let i = 0; i < binaryString.length; i++) {
    view[i] = binaryString.charCodeAt(i);
  }
  const blob = new Blob([arrayBuffer], { type: 'image/png' });

  return blob;
}  