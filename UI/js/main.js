//view all ride requests specific to a user
display_requests()
  function display_requests(){
  fetch("https://my-ride-app.herokuapp.com/currentuser/requests",{
        method:"GET",
        headers:{'Content-Type':'application/json',
        'Authorization': 'Bearer ' + readCookie('token')
      }
    })

  .then(function(response){
    return response.json()
  })
  .then(function(data){
    console.log(data)
    if(data.message=="No requests available"){
    document.getElementById("rtaken").innerHTML = 0;
      return;
    }
    var requests = data.requests;
    var output = requests.length ;
    document.getElementById("rtaken").innerHTML = output;
  })
  .catch(function(error){
        console.log("An error occured", error)

    })
}

//view all ride offers specific to a user

countmyrides();
function countmyrides(){
  
fetch("https://my-ride-app.herokuapp.com/currentuser/rides",{
        method:"GET",
      headers:{'Content-Type':'application/json',
        'Authorization': 'Bearer ' + readCookie('token')
      }
  })
  .then(function(response){
      return response.json()
  })
.then(function(data){
    console.log(data)
    if(data.message=="No ride offers available"){
    document.getElementById("rgiven").innerHTML = 0;
      return;
    }
    var ride_offers = data.ride_offers;
    var output = ride_offers.length;
    document.getElementById("rgiven").innerHTML = output;
  })
  .catch(function(error){
      console.log("An error occured", error)
  })
}

//login
        formlogin = document.getElementById("formlogin")
        
        if(formlogin.addEventListener){
            formlogin.addEventListener("submit", login, false);  
        }
    
    function login(e){
        e.preventDefault();
    
        fetch("https://my-ride-app.herokuapp.com/auth/login",{
            method:"POST",
            headers:{'Content-Type':'application/json'},
            body:JSON.stringify({
                    'username':document.getElementById("uname").value,
                    'password':document.getElementById("pass").value
            })
        
    
        })
        .then(function(response){
            return response.json()
        })
        .then(function(data){
            console.log(data)

            if(data.message=="Successfully logged in"){
                createCookie("token", data.access_token, 1);
                window.location.href ="driver.html";  
            }
            else{
                alert(data.message);
            }
            
        })
        .catch(function(error){
            console.log("An error occured", error)
        })
    }
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
//view all ride offers
viewrides();
function viewrides(){
  
    fetch("https://my-ride-app.herokuapp.com/rides",{
        method:"GET"
    })
    .then(function(response){
        return response.json()
    })
    .then(function(data){
      console.log(data)
      var ride_offers = data.ride_offers;
      var all_rides = '';
      for(var i=0;i<ride_offers.length;i++){
        var ride = ride_offers[i];
        var output = '<tr>'+
                     '<td>'+ride["ride_id"]+'</td>'+
                     '<td>'+ride["user_id"]+'</td>'+
                     '<td>'+ride["meetingpoint"]+'</td>'+
                     '<td>'+ride["departure"]+'</td>'+
                     '<td>'+ride["destination"]+'</td>'+
                     '<td>'+ride["slots"]+'</td>'+
                     '<td><button onclick="make_request('+ride["ride_id"]+')">Request</button></td>'+
                     '</tr>';
        all_rides += output;
      }      
      document.getElementById('tbody').innerHTML = all_rides;
      
    })
    .catch(function(error){
        console.log("An error occured", error)
    })
}

//making a request


function make_request(ride_id){
  fetch("https://my-ride-app.herokuapp.com/rides/"+ride_id+"/requests",{
        method:"POST",
        headers:{'Content-Type':'application/json',
        'Authorization': 'Bearer ' + readCookie('token')
      }
    })

  .then(function(response){ 
    return response.json()
  })
  .then(function(data){
    console.log(data)
    if(data.message == "Request successfully sent"){
        alert(data.message);
        window.location.href ="View requests.html";
        }
        else{
            alert(data.message);
        }
     
  })
  .catch(function(error){
        console.log("An error occured", error)

    })
}
//view all ride offers specific to a user
viewmyrides();
function viewmyrides(){
  
  fetch("https://my-ride-app.herokuapp.com/currentuser/rides",{
      method:"GET",
      headers:{'Content-Type':'application/json',
        'Authorization': 'Bearer ' + readCookie('token')
      }
  })
  .then(function(response){
      return response.json()
  })
  .then(function(data){
    console.log(data)
    var ride_offers = data.ride_offers;
    var all_rides = '<table class="Tride" id="ridetable">'+
                    '<tr>'+
                        '<th>Ride Id</th>'+
                        '<th>Meeting Point</th>'+
                        '<th>Departure time</th>'+
                        '<th>Destination</th>'+
                        '<th>Slots</th>'     +                
                        '<th>Action</th>'+
                    '</tr>'; 
    if(data.message=="No ride offers available"){
        document.getElementById("error").innerHTML = data.message;
        return;
    } 
    for(var i=0;i<ride_offers.length;i++){
      var ride = ride_offers[i];
      var output = '<tr>'+
                   '<td>'+ride["ride_id"]+'</td>'+
                   '<td>'+ride["meetingpoint"]+'</td>'+
                   '<td>'+ride["departure"]+'</td>'+
                   '<td>'+ride["destination"]+'</td>'+
                   '<td>'+ride["slots"]+'</td>'+
                   '<td><button onclick="view_requests('+ride["ride_id"]+')">View Requests</button></td>'+
                   '</tr>';
      all_rides += output;
    } 
    all_rides+='</table>'  ;   
    document.getElementById('myrides').innerHTML = all_rides;
    
  })
  .catch(function(error){
      console.log("An error occured", error)
  })
}

//view request to specific ride offer
function view_requests(ride_id){
  
  fetch("https://my-ride-app.herokuapp.com/users/rides/"+ride_id+"/requests",{
      method:"GET"
  })
  .then(function(response){
      return response.json()
  })
  .then(function(data){
    console.log(data)
    var requests = data.requests;
    var all_requests = '<table class="Tride" id="reqtable">'+
                      '<tr>' +
                          '<th>Request ID</th>' +
                          '<th>Name</th>' +
                          '<th>Status</th>' +
                          '<th>Action</th>' +
                      '</tr>';
    if(data.message === "No requests found"){
        document.getElementById("trequest").innerHTML = "";
        document.getElementById("rerror").innerHTML = data.message;
        return;
    }
    for(var i=0;i<requests.length;i++){
      var request = requests[i];
      var output = '<tr>'+
                   '<td>'+request["request_id"]+'</td>'+
                   '<td>'+request["name"]+'</td>'+
                   '<td>'+request["status"]+'</td>'+
                   '<td><button onclick="accept_reject('+request["ride_id"]+','+request["request_id"]+',\'accepted\')">Accept</button></td>'+
                   '<td><button onclick="accept_reject('+request["ride_id"]+','+request["request_id"]+',\'rejected\')">Reject</button></td>'+
                   '</tr>';
      all_requests += output;
    }      
      all_requests += '</table>';
    document.getElementById('trequest').innerHTML = all_requests;    
  })
  .catch(function(error){
      console.log("An error occured", error)
  })
}

//change accept/rejected request

    function accept_reject(ride_id,request_id,status){
  fetch("https://my-ride-app.herokuapp.com/users/rides/"+ride_id+"/requests/"+request_id,{
        method:"PUT",
        headers:{'Content-Type':'application/json',
        'Authorization': 'Bearer ' + readCookie('token')
      },
      body:JSON.stringify({
                    'status':status
            })

    })

  .then(function(response){
    return response.json()
  })
  .then(function(data){
    console.log(data)
    view_requests(ride_id)
    if(data.status=="accepted" && data.message=="Status updated successfully"){
        alert(data.message);
        }
        else{
            alert(data.message);
        }
     
  })
  .catch(function(error){
        console.log("An error occured", error)

    })
}
