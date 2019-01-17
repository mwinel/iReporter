[![Build Status](https://travis-ci.org/mwinel/iReporter.svg?branch=develop)](https://travis-ci.org/mwinel/iReporter)    [![Coverage Status](https://coveralls.io/repos/github/mwinel/iReporter/badge.svg?branch=develop)](https://coveralls.io/github/mwinel/iReporter?branch=develop)    [![Maintainability](https://api.codeclimate.com/v1/badges/9249d3e703b3acddeae9/maintainability)](https://codeclimate.com/github/mwinel/iReporter/maintainability)

# iReporter
iReporter enables any/every citizen to bring any form of corruption to the notice of appropriate authorities and the general public. Users can also report on things that needs government intervention.

### Installation and Set Up

Clone the repo from GitHub:

```
https://github.com/mwinel/iReporter.git
```

Create and activate virtualenv

```
python -m venv venv
venv\Scripts\activate
```

Install necessary requirements

```
pip install -r requirements.txt
```

Run the app and access the application at the address **http://localhost:5000/**

```
python run.py
```

Run unit tests

```
python -m unittest discover
```

### Sample request

Test all endpoints and see how they work using Postman.

```

http GET http://localhost:5000/api/v1/index

HTTP/1.0 200 OK
Content-Length: 41
Content-Type: application/json
Date: Tue, 08 Jan 2019 03:30:26 GMT
Server: Werkzeug/0.14.1 Python/3.6.5

{
    "message": "Welcome to iReporter."
}

```

### API Endpoints

| Resource URL | Methods | Description | Requires Auth |
| -------- | ------------- | --------- |--------------- |
| `/api/v1/index` | `GET`  | The index | `FALSE` |
| `/api/v1/auth/signup` | `POST`  | User Signup | `FALSE` |
| `/api/v1/auth/login` | `POST`  | User Login | `TRUE` |
| `/api/v1/red-flags` | `POST`  | Add redflag | `TRUE` |
| `/api/v1/red-flags` | `GET`  | Fetch redflags | `TRUE` |
| `/api/v1/red-flags/<id>` | `GET`  | Fetch redflag | `TRUE` |
| `/api/v1/red-flags/<id>` | `PUT`  | Update redflag | `TRUE` |
| `/api/v1/red-flags/<id>` | `DELETE`  | Delete redflag | `TRUE` |

### UI
[Checkout the app user interface.](https://mwinel.github.io/iReporter/UI/signup.html)

The UI has the following necessary pages as specified below.

- [user signup](https://mwinel.github.io/iReporter/UI/signup.html)
- [user login](https://mwinel.github.io/iReporter/UI/login.html)
- [redflags page](https://mwinel.github.io/iReporter/UI/redflags.html)
- [user profile](https://mwinel.github.io/iReporter/UI/user_profile.html)
- [admin login](https://mwinel.github.io/iReporter/UI/admin_login.html)

### Heroku url

[The app is also hosted on Heroku](https://ireporter-1233.herokuapp.com/api/v1)
