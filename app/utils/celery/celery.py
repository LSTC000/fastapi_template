from app.common import config

from celery import Celery


send_log_celery = Celery('send_log', broker=f'redis://{config.redis_host}:{config.redis_port}')
