# Django-REST-JWT-Authentication-App

Django project built with Django REST framework (DRF) and implement JWT authentication. Additionally, user also receives a mail with an OTP. User goes to otp verification endpoint and verifies otp through customized UserModel and Serializer.

## Project Workflow

- User registers, gets an active account with ACCESS_TOKEN and REFRESH_TOKEN
- User also receives a mail with an OTP
- User goes to otp verification endpoint and verifies otp
- User login
- User gets new ACCESS_TOKEN and new REFRESH_TOKEN, requesting with the current REFRESH_TOKEN to refresh token endpoint
- User logs out

## API Reference

| ACTIONS                     | HTTP METHODS | ENDPOINTS        |
| --------------------------- | ------------ | ---------------- |
| REGISTER FOR AN ACCOUNT     | POST         | /api/register/   |
| VERIFY ACCOUNT WITH OTP     | POST         | /api/verify/     |
| LOGIN WITH AN ACCOUNT       | POST         | /api/login/      |
| REFRESH TOKEN               | POST         | /api/refresh/    |
| LOGOUT OF AN ACCOUNT        | GET          | /api/logout/     |



## Repository Structure

```
.
└── Django-REST-JWT-Authentication-App
    ├── JwtAuthenticationProject
    │   ├── JWT_Authentication_App
    │   │   ├── admin.py
    │   │   ├── apps.py
    │   │   ├── emails.py
    │   │   ├── tests.py
    │   │   ├── views.py
    │   │   ├── __init__.py
    │   │   └── api
    │   │       ├── serializers.py
    │   │       ├── urls.py
    │   │       └── views.py
    │   ├── JwtAuthenticationProject
    │   │   ├── asgi.py
    │   │   ├── settings.py
    │   │   ├── urls.py
    │   │   ├── wsgi.py
    │   │   ├── __init__.py
    │   │   └── __init__.py
    │   ├── db.sqlite3
    │   └── manage.py
    ├── .gitignore
    ├── LICENSE
    ├── README.md
    └── requirements.txt

```

## Run Locally

Clone the project:

```
git clone https://github.com/RohitAayushmaan/Django-REST-JWT-Authentication-App.git
```

Go to the project directory:

```
cd Django-REST-JWT-Authentication-App/JwtAuthenticationProject
```

Install virtualenv:

```
pip install virtualenvwrapper
```

Creating the virtualenv:

```
mkvirtualenv venv_name
```

After creating virtial environment we need to activate it:

```
workon venv_name
```

Install dependencies:

```
pip install -r requirement.txt
```

Create all the tables in database.

```
python manage.py migrate
```

Set environment variables:
```
set EMAIL=your_email@example.com
set PASS=your_email_password
```

## Start the server

```
python manage.py runserver
```

The server will initialize in the <http://localhost:8000>

## Feedback:
If you have any feedback, please reach out to us at rohiit.chaurasiya@gmail.com


