# [Django REST - getting started](https://www.youtube.com/watch?v=263xt_4mBNc)


## setup
```
virtualenv venv // or any name
source venv/bin/activate // starts virtual env
pip install django djangorestframework 
django-admin startproject example
python manage.py migrate
python manage.py createsuperuser
```

## workflow (sorta)
1. mess with api
    1. `manage.py` startapp `:model` 
    2. edit `models.py`
    3. edit `urls.py`
2. `manage.py makemigrations`
3. `manage.py migrate`


## serializer
communicates how data models are sent via HTTP (ex. JSON, XML)
- create `serializers.py` inside model
    - need `Meta` with `models` and `fields` definition
- `serializers.ModelSerializer` is a 'default' way serializer can be inherited from

## views
displays given CRUD operations on your api
- edit `views.py` inside model
    - need to import model and serializer
- `viewsets.ModelViewSet` is a default view that can be inherited from

manually interact with endpoints via djangoadmin ex. `localhost:8000/admin` or through postman


