document
.getElementById("registrationForm")
.addEventListener("submit", async function(e){

e.preventDefault();

const payload = {

fullname:
document.getElementById("fullname").value,

email:
document.getElementById("email").value,

phone:
document.getElementById("phone").value,

course:
document.getElementById("course").value,

experience:
document.getElementById("experience").value,

comments:
document.getElementById("comments").value

};

try {

const response = await fetch(
"http://demo-alb-1427019949.eu-north-1.elb.amazonaws.com/api/register",
{
method:"POST",
headers:{
"Content-Type":"application/json"
},
body:JSON.stringify(payload)
}
);

const result = await response.json();

document.getElementById("message")
.innerHTML=result.message;

}
catch(error){

document.getElementById("message")
.innerHTML="Error submitting registration.";

}

});