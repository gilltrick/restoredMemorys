const myInput = document.getElementById("file-upload");
const resettInfoBtn = document.getElementById("resettInfoBtn");
const resettInfoContainer = document.getElementById("resettInfoContainer")
const closeInfoContainerBtn = document.getElementById("closeInfoContainerBtn");
const restoreMemoryBtn = document.getElementById("restoreMemoryBtn");
const loadAnimationContainer = document.getElementById("loadAnimationContainer")


function showResettInfo(){

  resettInfoContainer.style.display = "block";
}
try{
  resettInfoBtn.addEventListener("click", showResettInfo);
}
catch{
  console.log("no resettInfoBtn")
}

function closeResettInfo(){

  resettInfoContainer.style.display = "none";
}
try{
  closeInfoContainerBtn.addEventListener("click", closeResettInfo)
}
catch{
  console.log("no closeInfoContainerBtn")
}

function showProgressMsg(){

  loadAnimationContainer.style.display = "flex"
}
try{
  restoreMemoryBtn.addEventListener("click", showProgressMsg)
}
catch{
  console.log("no restoreMemoryBtn")
}