//SIGNUP
signupform = document.getElementById("signupform")
var loader = document.getElementById("loader")

if(signupform.addEventListener){
    signupform.addEventListener("submit", signup, false);  
}

function signup(e){
e.preventDefault();
loader.style.display = "block"
fetch("https://my-ride-app.herokuapp.com/auth/signup",{
    method:"POST",
    headers:{'Content-Type':'application/json'},
    body:JSON.stringify({
            'firstname':document.getElementById("fname").value,
            'lastname':document.getElementById("lname").value,
            'username':document.getElementById("uname").value,
            'password':document.getElementById("pass").value
    })


})
.then(function(response){
    return response.json()
})
.then(function(data){
    console.log(data)
    if(data.message=="User registered"){
        createCookie("token", data.access_token, 1);
        window.location.href ="index.html";
    }
    else{
        alert(data.message);
    }
    
})
.catch(function(error){
    console.log("An error occured", error)
})
}
