# WhatBytes Healthcare Backend

A secure healthcare backend REST API built using Django, Django REST Framework, PostgreSQL, and JWT authentication.

## Features

- User registration and JWT login
- JWT access and refresh tokens
- Patient CRUD operations
- Doctor CRUD operations
- Patient-doctor mapping
- Patient ownership and access control
- Duplicate mapping protection
- Request validation and error handling
- PostgreSQL database integration
- Environment-based configuration
- Automated API tests

## Tech Stack

- Python
- Django
- Django REST Framework
- PostgreSQL
- djangorestframework-simplejwt
- psycopg
- python-dotenv

## Project Structure

```text
whatbytes-healthcare-backend/
├── accounts/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── tests.py
├── patients/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── tests.py
├── doctors/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── tests.py
├── mappings/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── tests.py
├── config/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── manage.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md