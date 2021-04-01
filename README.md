# YieldUp
YieldUp is a web application that can be used by farmers to detect crop diseases mainly in cassava, beans, and coffee by taking pictures of plant leaves.   If a plant(s) is found to have a disease, the App recommends necessary steps to take such as getting the pesticides and agro-chemicals, connecting with an agricultural officer for expert guidance, and also link up with fellow farmers.   The intention is to realize high yields and boost the farmers' livelihoods. This solution is aimed at addressing the UN Sustainable Development Goal of No Hunger.

## To run this project locally, in ```settings.py``` 

set,

```DEBUG = False```

uncomment

```
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }
```

comment

```
# we only need the engine name, as heroku takes care of the rest
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
    }
}
```

and

```
# Allow all host hosts/domain names for this site
ALLOWED_HOSTS = ['*']

# # # Parse database configuration from $DATABASE_URL
import dj_database_url

DATABASES = { 'default' : dj_database_url.config()}

# # # Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# # # try to load local_settings.py if it exists
try:
  from local_settings import *
except Exception as e:
  pass
```


## Set up
To  set up this program, you need to first create a virtual environment, and install the requirements.txt 

```pip install -r reqirements.txt```

## Databases
To run a local database, 

uncomment

```
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }
```

comment

```
# we only need the engine name, as heroku takes care of the rest
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
    }
}
```

Then run 

``` python manage.py makemigrations ``` to make migrations

``` python manage.py migrate ``` to migrate

``` python manage.py createsuperuser ``` to create the superuser

``` python manage.py runserver ``` to run the server

<blockquote>The fully functional app can be found  <a href ="https://yieldupp.herokuapp.com/" target="_blank">here online</a></blockquote>


