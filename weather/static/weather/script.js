var today = new Date();
var time = today.getHours() + ":" + today.getMinutes() + ":" + today.getSeconds();

console.log(time);
let img=document.getElementById("bg-image");

// if(today.getMinutes()>4){
//     console.log("in");
//     img.style.backgroundImage="url('sunny.jpg')";
// }