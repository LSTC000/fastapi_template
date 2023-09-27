#!/bin/bash

if [[ "${1}" == "celery" ]]; then
  celery --app=app.utils.celery.celery:send_log_celery worker -l INFO
elif [[ "${1}" == "flower" ]]; then
  celery -app=app.utils.celery.celery:send_log_celery flower
fi