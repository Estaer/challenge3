[![Build Status](https://travis-ci.org/Estaer/challenge3.svg?branch=develop)](https://travis-ci.org/Estaer/challenge3)

[![Maintainability](https://api.codeclimate.com/v1/badges/24e74ab4656aa8f45200/maintainability)](https://codeclimate.com/github/Estaer/challenge3/maintainability)

[![Coverage Status](https://coveralls.io/repos/github/Estaer/challenge3/badge.svg?branch=master)](https://coveralls.io/github/Estaer/challenge3?branch=master)

# RIDE MY WAY
Ride my way App is a carpooling application that provides drivers with the ability to create ride offers
and passengers to join available ride offers.

## Getting Started
`These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.`

### Prerequisites
```
- git : To be used for version control
- python3: The base language used to develop the api endpoints
- pip: A python package used to install the necessary libraries and dependencies
- postman: For testing the api endpoints
```

### Installing

Type "git clone https://github.com/Estaer/challenge.git" in your terminal.

To install the requirements. run:
pip3 install -r requirements

The following commands are then used to run the app.
>`python run.py`

The following  are the api URLs:

Create an account or signup, method[POST]
>`http://127.0.0.1:5000/auth/signup`

Log into an account, method[POST]
>`http://127.0.0.1:5000/auth/login`

View details of a particular ride. 
>`e.g ride 5, method[GET]`
http://127.0.0.1:5000/rides/5`

View all ride offers, method[GET]
>`http://127.0.0.1:5000/rides`

Add a ride offer, method[POST]
>`http://127.0.0.1:5000/users/rides`

Request to join a particular ride 
> `eg ride 4, method[POST]
http://127.0.0.1:5000/users/rides/4/request`

View requests for a particular ride 
> `eg ride 4, method[GET]
http://127.0.0.1:5000/users/rides/2/requests`

Accept or Reject a request for a ride offer 
>`e.g Ride offer 2, and Request 3 Method[PUT]
http://127.0.0.1:5000/users/rides/2/requests/3`

## Running the tests
Running the tests
To run the tests, make sure you are working under test/, Then run either of the following commands
>`pytest`
>`nosetests`

## Built With

* Flask - Python web based framework
* Python - Framework language

## Authors

* **Nammanda Esther** - *Initial work* - https://github.com/Estaer

## Acknowledgments

* Andela 
* YOYO
* Bootcamp-9

