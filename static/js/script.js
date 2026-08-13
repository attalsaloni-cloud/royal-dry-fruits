
// Royal Dry Fruits JavaScript



// Page Load Message

document.addEventListener(
"DOMContentLoaded",
function(){


console.log(
"Royal Dry Fruits Website Loaded Successfully"
);


});





// Button Click Animation


let buttons=document.querySelectorAll(
".btn"
);


buttons.forEach(
function(button){


button.addEventListener(
"click",
function(){


button.style.transform="scale(0.95)";


setTimeout(
function(){


button.style.transform="";


},
150
);


});


});





// Confirm Logout


function confirmLogout(){


return confirm(
"Are you sure you want to logout?"
);


}