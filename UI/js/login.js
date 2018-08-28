
//login
formlogin = document.getElementById("formlogin")
var loader = document.getElementById("loader")
if (formlogin.addEventListener) {
    formlogin.addEventListener("submit", login, false);
}

function login(e) {
    e.preventDefault();
    loader.style.display = "block"
    fetch("https://my-ride-app.herokuapp.com/auth/login", {
        method: "POST",
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
            'username': document.getElementById("uname").value,
            'password': document.getElementById("pass").value
        })
    })
        .then(function (response) {
            return response.json()
        })
        .then(function (data) {
            console.log(data)

            if (data.message == "Successfully logged in") {
                createCookie("token", data.access_token, 1);
                window.location.href = "driver.html";
            }
            else {
                alert(data.message);
            }

        })
        .catch(function (error) {
            console.log("An error occured", error)
        })
}
