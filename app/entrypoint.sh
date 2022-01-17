#!/bin/sh

if [ "$SQL_ENGINE" = "django.db.backends.postgresql" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

# collect static
python manage.py collectstatic --no-input

# compile messages
python manage.py compilemessages

# python manage.py flush --no-input
# python manage.py migrate

exec "$@"