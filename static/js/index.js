// const chooseFileBtn = document.getElementById("file-upload");
const myInput = document.getElementById("file-upload");
const resettInfoBtn = document.getElementById("resettInfoBtn");
const resettInfoContainer = document.getElementById("resettInfoContainer")
const closeInfoContainerBtn = document.getElementById("closeInfoContainerBtn");
const restoreMemoryBtn = document.getElementById("restoreMemoryBtn");
// function chooseFile(){

//     console.log(myInput.value);
// }

// // chooseFileBtn.addEventListener("click", chooseFile);


// async function showimage(){
  
//     var file = myInput.files[0];
//     if (file == null){console.log("here is nothing");return;}
//     canvas.style.display = "block";
//     selfieContainer.style.display = "none";
//     getImage(file)
//   }
  
//   function dispalyimage(imageData){
  
//     var image = new Image();
//     image.src = imageData;
  
//     console.log(imageData);
  
//     image.onload = function(){
//       canvas.getContext('2d').drawImage(image, 0, 0, canvas.width, canvas.height);  
//     }
//   }
  
//   async function getImage(file){
  
//     var reader = new FileReader();
//     var image = new Image();
  
//     reader.onloadend = function () {
//       console.log(reader.result);
  
//       image.src = reader.result;
//       image.onload = function(){
  
//         canvas.getContext('2d').drawImage(image, 0, 0, canvas.width, canvas.height);  
//       }
//     }
//     reader.onerror = function () {
//       console.log('There was an error reading the file!');
//     }
//     reader.readAsDataURL(file);  
//   }

function showResettInfo(){

  resettInfoContainer.style.display = "block";
}

resettInfoBtn.addEventListener("click", showResettInfo);

function closeResettInfo(){

  resettInfoContainer.style.display = "none";
 }
closeInfoContainerBtn.addEventListener("click", closeResettInfo)
