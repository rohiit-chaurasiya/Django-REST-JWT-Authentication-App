# Django-REST-JWT-Authentication-App

Setup a Django project with DRF and create a JWT (email-password) authentication system by customizing UserModel and Serializer.

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
| LOGIN WITH AN ACCOUNT       | POST         | /api/login/      |
| VERIFY ACCOUNT WITH OTP     | POST         | /api/verify/     |
| REFRESH TOKEN               | POST         | /api/refresh/    |
| LOGOUT OF AN ACCOUNT        | GET          | /api/logout/     |
| REGISTER FOR AN ACCOUNT     | POST         | /api/register/   |
| EXPERIMENT WITH AN ENDPOINT | POST         | /api/experiment/ |

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

## Project setup

Clone this project:

```
git clone https://github.com/RohitAayushmaan/Django-REST-JWT-Authentication-App.git
```

Access:

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

Package you need to install:

```
pip install -r requirement.txt
```

Create all the tables in database.

```
python manage.py migrate
```

## Run the project

```
python manage.py runserver
```

The server will initialize in the <http://localhost:8000>
