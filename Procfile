web: gunicorn --pythonpath NewsBoard NewsBoard.wsgi --log-file -

worker: cd NewsBoard && celery -A NewsBoard worker -l debug -B
