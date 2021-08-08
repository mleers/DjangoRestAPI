# Django RESTful service

Features CRUD capabilites using Django backend/builtin database to serve as a RESTful endpoint. Features the [Django Rest Framework](https://www.django-rest-framework.org/) 

## Starting the service

### Requisites:
* python 3.6+
* djangorestframework library `pip3 install djangorestframework`
* npm/node
* Docker desktop (if using Docker deployment)

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

#### Accessing the frontend:
* `cd cd DjangoRestAPI/general_store/frontend`
* `npm install`
* `npm start`
* Got to http://localhost:3000/ with backend running to see data

### Docker
*requires docker-compose*
1. `docker-compose up` from root directory
 * Frontend: http://localhost:3000/ 
 * Backend: http://0.0.0.0:8000/api or http://localhost:8000/api

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

* [x] Add basic frontend
* [x] Dockerize project
