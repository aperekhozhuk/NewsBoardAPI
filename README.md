# NewsBoardAPI

## Simple REST API builded with Django-rest-framework.
- API allows you to authenticate your users with Token authentication.
- Authenticated users can add posts to news board. Every such post has title, author name, link and upvotes count (which initialized with zero value), time of publication setted automatically.
- Also users can edit and delete own posts.
- Authenticated users can leave comments for posts. Comment contain author name (which doesn't depend on user name) and text of comment.
- Users can edite own comments.
- Authenticated users can upvote posts (for each post once per day)
- All upvotes resets every day in fixed time (you can set this time parameters in ENV variables - see below)


### Check Postman documentation:
https://documenter.getpostman.com/view/14310036/TW6tNB5C

#

### Currently running on Heroku:
https://serene-tundra-06254.herokuapp.com/api/posts/

It uses WhiteNoise for static files, Gunicorn as wsgi server, Heroku Postgres as DB, Celery as task queue, Redis cloud from redislabs.com as message broker.

#

## **Running locally:**


### *Prerequisites:*
- Python 3 and pip installed
- Redis (local or remote version)
- PostgreSQL (local or remote version). You need to create DB and get its credentials.

### Follow next steps:
1) clone and move to repository directory:
```
git clone https://github.com/aperekhozhuk/NewsBoardAPI && cd NewsBoardAPI
```
2) Create virtual environment and activate it:
```
python3 -m venv env
source env/bin/activate
```
3) Install dependencies:
```
pip install -r requirements.txt
```
(You can skip 4,5, just ensure that you have settings exported as ENV variables)

4) Open "set_env.sh" file and fill it with your settings (Django secrete key, Postgres connection settings, url to your Redis etc)
5) Export settings to ENV:
```
source ./set_env.sh
```
6) Move to project directory:
```
cd NewsBoard
```
7) Create database tables (your Postgres server should be running):
```
python manage.py migrate
```
8) Create superuser (if you want to get access to admin site):
```
python manage.py createsuperuser
```
9) Run server:
```
gunicorn NewsBoard.wsgi
```
10) Run your Redis server (if you don't use cloud version)
11) In other terminal window open repository folder, activate virtual environment, run "source ./set_env.sh", cd into "NewsBoard" folder (which contains "manage.py" file)  and finally run a Celery worker:
```
celery -A NewsBoard worker
```
12) Open in browser.
```
http://127.0.0.1:8000/api/posts
```
13) Visit admin site to add new users if you want
```
http://127.0.0.1:8000/admin
```
**Note:** if DEBUG=True - you can Log in in browser, because session authenticated enabled.

#

Also you are welcome to use my Postman collection. In such case you need to change collection's enviroment variables : url to API, username and password of user that you created in admin site (or your's superuser) and token which you can get if login with credentials of created user.

#
