# Docs

## How to run
    $ Download project
    $ Create pro_gaming.local_settings.py file based on pro_gaming.local_settings.py.sample
    $ create venv (On Windows: python -m venv venv)
    $ Activate venv (On Windows: venv\Scripts\activate)
    $ pip install -r requirements.txt
    $ python manage.py migrate
    $ python manage.py collectstatic --noinput
    $ uvicorn pro_gaming.asgi:application --host 0.0.0.0 --port 8000

## How to run tests
    $ navigate to the project folder
    $ pytest

## How to access the tasks API
    $ http://localhost:8000/api/tasks/

## How to access the admin panel
    $ http://localhost:8000/admin/

## How to access the API documentation
    $ http://localhost:8000/swagger/

## How to connect to websockets
    $ ws://localhost:8000/ws/tasks/

## How to get or refresh auth token
    $ http://localhost:8000/api/get_token/
    $ http://localhost:8000/api/refresh_token/

## ToDo
    - Dockerize the project
    - Create caching for the tasks API


