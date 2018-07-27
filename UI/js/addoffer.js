// adding an offer
addoffer = document.getElementById("addoffer")
    
if(addoffer.addEventListener){
      addoffer.addEventListener("submit",addOffer, false);  
    }

function addOffer(e){
    e.preventDefault();

    fetch("https://my-ride-app.herokuapp.com/users/rides",{
        method:"POST",
        headers:{'Content-Type':'application/json',
                 'Authorization': 'Bearer ' + readCookie('token')
                },
        body:JSON.stringify({
                'meetingpoint':document.getElementById("meetingpoint").value,
                'departure':document.getElementById("departure").value,
                'destination':document.getElementById("destination").value,
                'slots':document.getElementById("slots").value
        })
        })
    .then(function(response){
        return response.json()
    })
    .then(function(data){
        console.log(data)
        if(data.message=="Ride offer created"){

            window.location.href ="View ride offers.html";
        }    
    })
    .catch(function(error){
        console.log("An error occured", error)
    })
}
