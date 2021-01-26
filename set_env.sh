# Change your settings and keep it in secret!

# type "source ./set_env.sh" for import all env vars in current shell
export SECRET_KEY="SECRET_KEY_EXAMPLE"
export DEBUG="1"
export ADMIN_ENABLED="1"
export ALLOWED_HOSTS="localhost 127.0.0.1 0.0.0.0"
export DATABASE_ENGINE="django.db.backends.postgresql_psycopg2"
export DATABASE_NAME="newsboard"
export DATABASE_USER="postgres"
export DATABASE_PASSWORD="1111"
export DATABASE_HOST="localhost"
export DATABASE_PORT="5432"
export UPVOTES_RESET_TIME_HOUR="4"
export UPVOTES_RESET_TIME_MINUTE="0"
export CELERY_BROKER_URL="redis://localhost:6379"
export CELERY_RESULT_BACKEND="redis://localhost:6379"
