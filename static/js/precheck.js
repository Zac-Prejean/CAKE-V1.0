

import { prefixACSKTUM16ZPNK, prefixACSKTUM16ZBLK, prefixACSKTUM16ZICB, prefixACSKTUM16ZMNT, prefixACSKTUM18ZDBL, prefixACSKTUM18ZCLGD, prefixACSKTUM18ZCLRGD,     
    nameplates, prefixGLFBLWHTSO, nonLineTum, oneLineTum, Lineglscan, validSkus, applyFontRule, combinedWOOD, nonLineWOOD, threeLineWOOD,    
    prefixJMUG11WB, nonLineMUG, oneLineMUG, threeLineMUG, fourLineMUG, oneLineGLFBL,updateRowSku } from './precheck_config.js';  

import { convertSku } from './convertSku.js';        
        
    let csvUploaded = false;        
    let parsedCsvData;        
    let rowCount = 0;      
    let xlsxFile;      
        
    function handleFileSelect(evt) {        
        const file = evt.target.files[0];        
        if (file.type === "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") {        
            xlsxFile = file;        
            // Show the confirmation modal        
            $('#confirmation-modal').modal('show');        
        } else {        
            // Process the CSV file as usual        
            processCsvFile(file);        
        }        
    }        
          
    function processCsvFile(file) {        
        Papa.parse(file, {        
            complete: function (results) {        
                parsedCsvData = results.data;        
                $('#output').html(generateTableHtml(results.data));        
                $('#preview-modal').modal('toggle');        
                csvUploaded = true;        
            }        
        });        
    }        
                    
    $("#csv-file").on("change", handleFileSelect);        
      
      
    // splitting personalizations for table      
    function getPersonalization(options) {      
        // Check if options is a string, if not return empty personalizations        
        if (typeof options !== 'string') {        
            return { personalizations: [], personalizationLineCount: 0 };        
        }       
                // split by commas          
                const lines = options.split(/,\s*/);          
                const personalizationKeywords = ['Personalization:', 'Personalization', 'Custom Name:', 'Name 1:', 'Name 2:', 'Name 3:', 'Name 4:', 'Custom Name Top:', 'Custom Name Bottom:',         
                'Left Inscription:', 'Middle Inscription:', 'Right Inscription:', 'Outside Inscription:', 'Inside Inscription:', 'InsideTextLine1:'];          
                      
                const personalizations = [];          
                let personalizationLineCount = 0;          
                      
                for (const line of lines) {          
                    for (const keyword of personalizationKeywords) {          
                        if (line.includes(keyword)) {          
                            const startPos = line.indexOf(keyword) + keyword.length;          
                            const personalization = line.slice(startPos).replace(/(^"|"$|\s+,)/g, '').trim().replace(/,(\s*)$/, '').replace(/\s+,$/, '').replace(/\s+(?=")/, '');      
                  
                            if (keyword === 'Inside Inscription:') {      
                                personalizations[1] = personalization;      
                                personalizationLineCount++;      
                            } else if (keyword === 'Name 1:' || keyword === 'Name 2:' || keyword === 'Name 3:' || keyword === 'Name 4:' || keyword === 'Custom Name Top:' || keyword === 'Custom Name Bottom:'       
                            || keyword === 'Left Inscription:' || keyword === 'Middle Inscription:' || keyword === 'Right Inscription:' || keyword === 'InsideTextLine1:') {        
                  
                                personalizations.push(personalization);        
                                personalizationLineCount++;        
                            } else {        
                                const splitPersonalization = personalization.split(/["']\s*[,]\s*["']|["']\s*["']\s*|\r\n|\n|\r/).map(val => val.trim());        
                                personalizationLineCount = splitPersonalization.length;        
                                if (personalizationLineCount === 1) {        
                                    personalizations.push(splitPersonalization[0], "");        
                                } else if (personalizationLineCount > 1) {        
                                    personalizations.push(...splitPersonalization);        
                                }        
                            }        
                        }        
                    }        
                }        
                return { personalizations, personalizationLineCount };        
            }       
      
            function startLoadingBar() {  
                $("#please-stand-by-prompt").show();  
            }  
              
            function hidePrompt() {  
                $("#please-stand-by-prompt").hide();  
            }  
              
            $("#confirm-xlsx-btn").on("click", function () {  
                // Start the prompt  
                startLoadingBar();  
              
                // Process the confirmed XLSX file  
                const formData = new FormData();  
                formData.append("file", xlsxFile);  
              
                fetch("/process_xlsx", {  
                    method: "POST",  
                    body: formData  
                })  
                .then(response => response.json())  
                .then(data => {  
                    // Fetch the combined.csv file from the server  
                    fetch(data.csv_url)  
                    .then(response => response.text())  
                    .then(csvData => {  
                        // Parse the CSV data  
                        const results = Papa.parse(csvData);  
              
                        // Update the UI with the parsed CSV data  
                        parsedCsvData = results.data;  
                        $('#output').html(generateTableHtml(results.data));  
                        $('#preview-modal').modal('toggle');  
                        csvUploaded = true;  
              
                        // Hide the prompt  
                        hidePrompt();  
                    });  
                })  
                .catch(error => {  
                    console.error("Error:", error);  
                });  
            });  
                                                 
    // generating table      
    function generateTableHtml(data) {  
        const indicesToDisplay = [0, 1, 2, 4, 5]; // Indices to display, including "Due Date" and "Batch"  
        const maxPersonalizationLength = 150;  
        rowCount = 0;  
        let tableHtml = '<table class="table table-bordered">';  
          
        for (let i = 0; i < data.length; i++) {  
            const row = data[i];  
            if (i !== 0 && row[2] !== undefined) {  
                row[2] = row[2].toUpperCase();  
            }  
            if (i === 0) {  
                tableHtml += '<thead><tr>';  
                for (let j = 0; j < row.length; j++) {  
                    if (indicesToDisplay.includes(j)) {  
                        if (j === 4) {  
                            tableHtml += '<th>Due Date</th>';  
                        } else if (j === 5) {  
                            tableHtml += '<th>Batch</th>';  
                        } else {  
                            tableHtml += '<th>' + row[j] + '</th>';  
                        }  
                    }  
                }  
                tableHtml += '</tr></thead><tbody>';  
            } else {  
                if (row[2] === "") {  
                    tableHtml += '<tr class="separator"><td colspan="6"></td></tr>';  
                    continue;  
                } else if (row.includes("Discount")) {  
                    tableHtml += '<tr class="separator"><td colspan="6"></td></tr>';  
                    continue;  
                }  
      
                rowCount++;  
                tableHtml += '<tr>';  
                for (let j = 0; j < row.length; j++) {  
                    const sku = row[2];  
                    const options = row[3];  
      
                    function updateSkuBasedOnLineCount(row, lineCount) {  
                        // FAVCHILD MUG  
                        if (lineCount === 2 && row[2] === "JMUG11WBUVPPSFAVCHUVP") {  
                            row[2] = "JMUG11WBUVPPS2FAVCHUVP";  
                        }  
                        if (lineCount === 3 && row[2] === "JMUG11WBUVPPSFAVCHUVP") {  
                            row[2] = "JMUG11WBUVPPS3FAVCHUVP";  
                        }  
                        if (lineCount === 4 && row[2] === "JMUG11WBUVPPSFAVCHUVP") {  
                            row[2] = "JMUG11WBUVPPS4FAVCHUVP";  
                        }  
                    }  
      
                    if (row[2]) {  
                        row[2] = row[2].replace(/-/g, ' '); // Remove all "-" from row[2]  
                        row[2] = convertSku(row[2]);  
                    }  
                    if (typeof options === 'string') {  
                        if (options.includes(', print_url:') || options.includes(', print_url_1:')) {  
                            const skuWithoutCLabel = row[2].replace("CLABEL", "");  
                            row[2] = "CLABEL" + skuWithoutCLabel;  
                        }  
                        if (options.includes(', Art_Location_Front:') || options.includes(', Art_Location_Back:')) {  
                            const skuWithoutBLabel = row[2].replace("BLABEL", "");  
                            row[2] = "BLABEL" + skuWithoutBLabel;  
                        }  
                    }  
      
                    const isNonLine = nonLineWOOD.some(suffix => combinedWOOD.some(prefix => (prefix + suffix) === sku)) || nonLineMUG.some(suffix => prefixJMUG11WB.some(prefix => (prefix + suffix) === sku)) || nonLineTum.some(suffix => (prefixACSKTUM16ZPNK + suffix) === sku || (prefixACSKTUM16ZBLK + suffix) === sku || (prefixACSKTUM16ZICB + suffix) === sku || (prefixACSKTUM16ZMNT + suffix) === sku || (prefixACSKTUM18ZDBL + suffix) === sku || (prefixACSKTUM18ZCLGD + suffix) === sku || (prefixACSKTUM18ZCLRGD + suffix) === sku);  
                    const isOneLine = nameplates.includes(sku) || oneLineMUG.some(suffix => prefixJMUG11WB.some(prefix => (prefix + suffix) === sku)) || oneLineTum.some(suffix => (prefixACSKTUM16ZPNK + suffix) === sku || (prefixACSKTUM16ZBLK + suffix) === sku || (prefixACSKTUM16ZICB + suffix) === sku || (prefixACSKTUM16ZMNT + suffix) === sku || (prefixACSKTUM18ZDBL + suffix) === sku || (prefixACSKTUM18ZCLGD + suffix) === sku || (prefixACSKTUM18ZCLRGD + suffix) === sku) || oneLineGLFBL.some(suffix => prefixGLFBLWHTSO.some(prefix => (prefix + suffix) === sku)) || Lineglscan.includes(sku);  
                    const isThreeLine = threeLineMUG.some(suffix => prefixJMUG11WB.some(prefix => (prefix + suffix) === sku)) || threeLineWOOD.some(suffix => combinedWOOD.some(prefix => (prefix + suffix) === sku));  
                    const isFourLine = fourLineMUG.some(suffix => prefixJMUG11WB.some(prefix => (prefix + suffix) === sku));  
      
                    if (indicesToDisplay.includes(j)) {  
                        if (j === 2) {  
                            const sku = row[j];  
                            console.log("Current SKU:", sku);  
                            const { personalizations, personalizationLineCount } = getPersonalization(row[3]);  
                            updateSkuBasedOnLineCount(row, personalizationLineCount);  
                            if (personalizations.length === 2 && personalizationLineCount === 2) { }  
                            console.log("Personalization line count:", personalizationLineCount);  
                            let icon;  
                            if (sku.startsWith("CLABEL") || sku.startsWith("BLABEL")) {  
                                icon = goodCheckUrl;  
                            } else if (!validSkus.includes(sku)) {  
                                icon = unknownDesignUrl;  
                            } else if (personalizationLineCount === 0 && isNonLine) {  
                                icon = goodCheckUrl;  
                            } else if ((personalizationLineCount === 0 || personalizationLineCount > 2) && !isThreeLine && !isFourLine) {  
                                icon = errorCheckUrl;  
                            } else if (personalizationLineCount === 1 && isOneLine) {  
                                icon = goodCheckUrl;  
                            } else if (personalizationLineCount === 2) {  
                                icon = goodCheckUrl;  
                            } else if (personalizationLineCount === 3 && isThreeLine) {  
                                icon = goodCheckUrl;  
                            } else {  
                                icon = missingCheckUrl;  
                            }  
                            tableHtml += '<td><div style="display: flex; align-items: center;"><img src="' + icon + '" class="icon2" width="25" height="25" alt="Check Logo"><span>' + sku + '</span></div></td>';  
                        } else if (j === 4) { // Adjusted block to handle "Due Date" column  
                            tableHtml += '<td>' + row[j] + '</td>';  
                        } else if (j === 5) { // Adjusted block to handle "Batch" column  
                            tableHtml += '<td>' + row[j] + '</td>';  
                        } else {  
                            tableHtml += '<td>' + row[j] + '</td>';  
                        }  
                    }  
                }  
      
                // delete btn  
                if (row.join('').trim() !== '') {  
                    tableHtml += '<td><img src="/static/images/minus.svg" width="25" height="25" class="icon d-inline-block align-center delete-btn" alt="Delete Button" data-toggle="tooltip" data-placement="top" title="delete line" data-row-index="' + i + '"></td></tr>';  
                } else {  
                    tableHtml += '<td></td></tr>';  
                }  
      
                // non-editable CSV line view  
                const itemOptionsText = row[3] !== undefined ? row[3] : '';  
                let visibilityStyle = "";  
                if (itemOptionsText.length > maxPersonalizationLength) {  
                    visibilityStyle = "display: none;";  
                }  
      
                tableHtml += '<tr><td colspan="5" style="font-size: 12px; color: #999; padding-top: 0; text-align: left;' + visibilityStyle + '">';  
                tableHtml += '<div class="csv-line" data-row-index="' + i + '">' + itemOptionsText + '</div>';  
                tableHtml += '</td></tr>';  
            }  
        }  
        tableHtml += '</tbody></table>';  
        return tableHtml;  
    }  
                        
    $("#csv-file").on("change", handleFileSelect);        
            
    $("#preview-button").on("click", function() {  
        if (csvUploaded) {  
            $('#preview-modal').modal('toggle');  
        } else {  
            $('#warning-modal').modal('show');  
        }  
    });  
      
    $(".close").on("click", function() {  
        $('#warning-modal').modal('hide');  
    });       
    
    let saveButtonClicked = false;  
  
    $('#save-changes-btn').on('click', function () {  
        saveButtonClicked = true;  
        $('#preview-modal').modal('hide');  
        $('#confirmation-modal').modal('hide');  
    });  
      
    $(document).ready(function() {  
        $('.close, .btn.btn-secondary').on('click', function() {  
            $('#preview-modal').modal('hide');  
            $('#confirmation-modal').modal('hide');  
        });  
    });  
      
    $('#preview-modal').on('hidden.bs.modal', function () {  
        if (saveButtonClicked) {  
            const line1Inputs = document.getElementsByClassName('line1-input');  
            const line2Inputs = document.getElementsByClassName('line2-input');  
            const line3Inputs = document.getElementsByClassName('line3-input');  
            const line4Inputs = document.getElementsByClassName('line4-input');  
            const newBatchName = $('#batch-name-input').val().trim(); // Get the new batch name  
            const filterDate = $('#filter-date-input').val().trim(); // Get the date to filter by  
      
            console.log('New Batch Name:', newBatchName); // Debugging output  
            console.log('Filter Date:', filterDate); // Debugging output  
      
            // Filter parsedCsvData to keep only rows with the specified date  
            const filteredData = parsedCsvData.filter((row, index) => {  
                if (index === 0) return true; // Keep the header row  
                return row[4] === filterDate; // Assuming the date is in the fifth column (index 4)  
            });  
      
            for (let i = 0; i < filteredData.length; i++) {  
                const row = filteredData[i];  
                if (row === null || row.includes("Discount") || i === 0) {  
                    continue;  
                }  
      
                // Update the batch name in row 5  
                row[5] = newBatchName;  
      
                console.log('Updated Row:', row); // Debugging output  
            }  
      
            const updatedCsv = Papa.unparse(filteredData.filter(row => row !== null));  
            const blob = new Blob([updatedCsv], { type: "text/csv;charset=utf-8;" });  
            const downloadLink = document.createElement("a");  
            const url = URL.createObjectURL(blob);  
            downloadLink.href = url;  
            downloadLink.setAttribute("download", "updated_csv.csv");  
            document.body.appendChild(downloadLink);  
            downloadLink.click();  
            document.body.removeChild(downloadLink);  
            deleteCombinedCsv();  
            saveButtonClicked = false;  
        }  
    });  
                  
    $(document).ready(function(){       
        $('[data-toggle="tooltip"]').tooltip();         
      });      
      
      $(document).on('click', '.delete-btn', function () {        
        const rowIndex = parseInt($(this).data('row-index'));        
        parsedCsvData[rowIndex] = null;        
            
        // Find the closest 'tr' element and also the previous and next 'tr' elements        
        const currentRow = $(this).closest('tr');        
        const prevRow = currentRow.prev('tr');        
        const nextRow = currentRow.next('tr');        
            
        // Remove the current row, the previous row, and the next row        
        currentRow.remove();        
        prevRow.remove();        
        nextRow.remove();        
            
        // Remove the non-editable CSV line view        
        const csvLine = $('.csv-line[data-row-index="' + rowIndex + '"]');        
        csvLine.remove();        
    });

function deleteCombinedCsv() {
    fetch("/delete_combined_csv", {  
        method: "POST"  
    })  
    .then(response => response.json())  
    .then(data => {  
        console.log(data.message);  
    })  
    .catch(error => {  
        console.error("Error:", error);  
    });  
}  
    