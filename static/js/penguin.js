

function showPasswordModal() {  
  return new Promise((resolve, reject) => {  
    const passwordModal = new bootstrap.Modal(  
      document.getElementById("passwordModal")  
    );  
    const submitButton = document.querySelector("#passwordModal .btn-primary");  
  
    passwordModal.show();  
  
    function handleModalHidden(event) {  
      submitButton.removeEventListener("click", handleSubmitButtonClick);  
    }  
  
    function handleSubmitButtonClick() {  
      const passwordInput = document.querySelector(  
        "#passwordModal #passwordInput"  
      );  
      const password = passwordInput.value;  
  
      checkPassword(password)  
        .then(() => {  
          passwordInput.value = "";  
          passwordModal.hide();  
          resolve(password);  
        })  
        .catch(() => {  
          passwordInput.value = "";  
          reject();  
        });  
    }  
  
    document  
      .getElementById("passwordModal")  
      .addEventListener("hidden.bs.modal", handleModalHidden, { once: true });  
    submitButton.addEventListener("click", handleSubmitButtonClick);  
  });  
}  

function checkPassword(input_password) {      
  return new Promise((resolve, reject) => { 
    fetch('/check_password', {  
      method: 'POST',  
      body: JSON.stringify({ password: input_password }),  
      headers: {  
        'Content-Type': 'application/json'  
      }  
    })  
    .then(response => {  
      if (!response.ok) {  
        throw new Error('Network response was not ok');  
      }  
      return response.json();  
    })  
    .then(data => {
  
      if (data.result !== 'failure') {  
        resolve();  
      } else {  
        alert('Incorrect password. Access denied.');  
        reject();  
      }  
    })  
    .catch(error => {  
      console.error('There was a problem with the fetch operation:', error);  
      reject();  
    });  
  });  
}   

function confirmDeleteBox() {  
  const password = document.getElementById('deletePasswordInput').value;  

  // Send a request to the Flask endpoint to check the password  
  fetch('/check_password', {  
      method: 'POST',  
      headers: {  
          'Content-Type': 'application/json',  
      },  
      body: JSON.stringify({password: password}),  
  })  
  .then(response => response.json())  
  .then(data => {  
      if (data.result === 'success') {  
          const boxNumber = parseInt(document.getElementById('deleteBoxNumber').innerText, 10);  
          removeBox(boxNumber);  

          // Clear the password input field  
          document.getElementById('deletePasswordInput').value = '';  

          // Close the delete warning modal  
          $('#deleteWarningModal').modal('hide');  
          // Close the box info modal  
          $('#boxInfoModal').modal('hide');  
      } else {  
          alert('Incorrect password. Please try again.');  
      }  
  });  
}

  document.addEventListener('DOMContentLoaded', function() {  
    // Check if you are on the admin page  
    if (document.getElementById('admin-page')) {  
      showPasswordModal()  
        .then(password => {  
          return checkPassword(password);  
        })  
        .then(() => {  
          // The password is correct, display the content container and initialize your admin page here  
          document.querySelector('.content-container').style.display = 'block';  
        })  
        .catch(() => {  
          // The password is incorrect or not entered, the user is redirected to the home route  
          window.location.href = '/';  
        });  
    }   

    var deleteBoxBtn = document.getElementById('deleteBoxBtn');  
    if (deleteBoxBtn) {  
        deleteBoxBtn.addEventListener('click', function () {  
            const boxNumber = parseInt(document.getElementById('boxInfoNumber').innerText, 10);  
            deleteBox(boxNumber);  
        });  
    }  
    var confirmDeleteBtn = document.getElementById('confirmDeleteBtn');  
    if (confirmDeleteBtn) {  
        confirmDeleteBtn.addEventListener('click', confirmDeleteBox);  
    } 
  // Add event listeners for the password modal  
  if (document.getElementById('passwordModal')) {  
      document.getElementById('passwordModal').addEventListener('shown.bs.modal', function () {  
          document.getElementById('passwordInput').focus();  
      });  

      document.getElementById('passwordModal').addEventListener('hidden.bs.modal', function () {  
          document.getElementById('passwordInput').value = '';  
      });  
  }  
});   

document.addEventListener('DOMContentLoaded', function() {  
  // Check if the main element exists  
  const mainElement = document.querySelector('main');  
  if (mainElement) {  
      showPasswordModal()  
          .then(password => {  
              return checkPassword(password);  
          })  
          .then(() => {  
              // The password is correct, display the main element  
              mainElement.style.display = 'block';  
          })  
          .catch(() => {  
              // The password is incorrect or not entered, the user is redirected to the home route  
              window.location.href = '/';  
          });  
  }  
});  

function showWarningModal() {  
  return new Promise((resolve, reject) => {  
      const warningModal = new bootstrap.Modal(document.getElementById("warningModal"));  
      const submitButton = document.querySelector("#warningModal .btn-primary");  

      warningModal.show();  

      function handleModalHidden(event) {  
          submitButton.removeEventListener("click", handleSubmitButtonClick);  
      }  

      function handleSubmitButtonClick() {  
          const passwordInput = document.querySelector("#warningModal #warningPasswordInput");  
          const password = passwordInput.value;  
          checkPassword(password)  
              .then(() => {  
                  passwordInput.value = "";  
                  warningModal.hide();  
                  resolve(password);  
              })  
              .catch(() => {  
                  passwordInput.value = "";  
                  reject();  
              });  
      }  

      document.getElementById("warningModal").addEventListener("hidden.bs.modal", handleModalHidden, { once: true });  
      submitButton.addEventListener("click", handleSubmitButtonClick);  
  });  
}  

function showModal(status) {  
  const modal = document.getElementById("warningModal");  
  const mainElement = document.querySelector('main');  

  document.getElementById("modal-text").innerHTML = `This item has processed the <a href="#" class="status-link">${status}</a> stage. Check with supervisor.`;  

  // Hide main element when showing the warning modal  
  mainElement.style.display = 'none';  

  showWarningModal()  
      .then(() => {  
          // Password was correct, proceed with further actions  
          mainElement.style.display = 'block';  
          modal.style.display = "none";  
      })  
      .catch(() => {  
          // Password was incorrect  
          alert("Incorrect password. Access denied.");  
      });  
}  

document.addEventListener('DOMContentLoaded', function() {  
  const mainElement = document.querySelector('main');  
    
  if (mainElement) {  
      showPasswordModal()  
          .then(password => {  
              return checkPassword(password);  
          })  
          .then(() => {  
              // The password is correct, display the main element  
              mainElement.style.display = 'block';  
          })  
          .catch(() => {  
              // The password is incorrect or not entered, the user is redirected to the home route  
              window.location.href = '/';  
          });  
  }  
});  
