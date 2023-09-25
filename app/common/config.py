import os
from dataclasses import dataclass, field

from dotenv import load_dotenv, find_dotenv


load_dotenv(find_dotenv())


@dataclass(frozen=True)
class Config:
    origins: list[str] = field(default_factory=lambda: os.getenv('ORIGINS', '').split(','))

    redis_host: str = os.getenv('REDIS_HOST')
    redis_port: int = os.getenv('REDIS_PORT')

    db_user: str = os.getenv('DB_USER')
    db_pass: str = os.getenv('DB_PASS')
    db_host: str = os.getenv('DB_HOST')
    db_port: int = os.getenv('DB_PORT')
    db_name: str = os.getenv('DB_NAME')

    base_logs_path: str = r'logs/log.log'
    base_logs_format: str = u'#%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s'

    user_logs_path: str = r'logs/user.log'
