# Django RESTful service

Features CRUD capabilites using Django backend/builtin database to serve as a RESTful endpoint. Features the [Django Rest Framework](https://www.django-rest-framework.org/) 

## Starting the service

### Requisites:
* python 3.6+
* djangorestframework library `pip3 install djangorestframework`

### Locally built:
#### Windows
Create virtual environment (optional)
1. `python -m venv env`
2. `env\Scripts\python.exe -m pip install -r requirements.txt`

Start here if skipping virtual env
1. `pip3 install -r requirements.txt`
2. `python manage.py runserver`
3. Go to http://localhost:8000/api/ (unless port specified otherwise)

#### Mac
1. `cd DjangoRestAPI/general_store`
2. `python3 manage.py runserver`
3. Go to http://localhost:8000/api/ (unless port specified otherwise)

#### Docker
*requires docker-compose*
1. `docker-compose up` from root directory
2. Go to http://0.0.0.0:8000/api or http://localhost:8000/api

## Tasks:
* [x] Create catalog of url patterns
* [x] Achieve CRUD functionality using API decorators (function based)
    * [x] Global Get
    * [x] instance Get
    * [x] instance Post
    * [x] instance Put
    * [x] instance Delete
* [x] Create data model
* [x] Serialize data
* [x] Add superuser

* [ ] Add basic frontend
* [ ] Dockerize project
