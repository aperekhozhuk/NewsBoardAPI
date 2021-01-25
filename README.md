# NewsBoardAPI

Check Postman documentation:
https://documenter.getpostman.com/view/14310036/TW6tNB5C


## Prerequisites:
1) python3
2) redis-server
3) "DJANGO_SECRET_KEY" enviroment variable (if you dont want to type it in settings file)

## Running locally:
1) glone and move to repo directory
```
git clone https://github.com/aperekhozhuk/NewsBoardAPI && cd NewsBoardAPI
```
2) Create venv & activate it
```
python3 -m venv env
source env/bin/activate
```
3) Install dependencies:
```
pip install -r requirements.txt
```
4) Move to project directory
```
cd NewsBoard
```
5) Create local SQlite db inside project folder
```
python manage.py migrate
```
6) Create superuser
```
python manage.py createsuperuser
```
7) Run Celery worker
```
celery -A NewsBoard worker -l info -B
```
8) In second terminal window run redis-server
10) In third terminal window which running in NewsBoardAPI/NewsBoard with enabled virtual enviroment, run django app:
```
python manage.py runserver
```
10) Open in browser (in DEBUG=TRUE mode you can use API in browser, bcs session authenticated enabled)
```
http://localhost:8000/api/posts
```
11) Visit admin site to add new users if you want
```
http://localhost:8000/admin
```
