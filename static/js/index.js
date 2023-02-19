const myInput = document.getElementById("file-upload");
const resetInfoBtn = document.getElementById("resetInfoBtn");
const resetInfoContainer = document.getElementById("resetInfoContainer")
const closeInfoContainerBtn = document.getElementById("closeInfoContainerBtn");
const restoreMemoryBtn = document.getElementById("restoreMemoryBtn");
const loadAnimationContainer = document.getElementById("loadAnimationContainer");
const uploadImageBtn = document.getElementById("uploadImageBtn");
const cookieInfoContainerBtn = document.getElementById("cookieInfoContainerBtn")
const cookieInfoContainer = document.getElementById("cookieInfoContainer")

function redirect(){
uploadImageBtn.click();
}
try{
myInput.addEventListener("change", redirect)
}
catch{
  console.log("no myInput")
}

function showResetInfo(){

  resetInfoContainer.style.display = "block";
}
try{
  resetInfoBtn.addEventListener("click", showResetInfo);
}
catch{
  console.log("no resetInfoBtn")
}

function closeResetInfo(){

  resetInfoContainer.style.display = "none";
}
try{
  closeInfoContainerBtn.addEventListener("click", closeResetInfo)
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

function acceptCookies(){
  document.cookie = `rememberMe=${new Date().toLocaleString()}`
  cookieInfoContainer.style.display = "none";
}
try{
  cookieInfoContainerBtn.addEventListener("click", acceptCookies)
}
catch{
  console.log("no cookieInfoContainerBtn")
}