import os
from dataclasses import dataclass, field

from dotenv import load_dotenv, find_dotenv


load_dotenv(find_dotenv())


@dataclass(frozen=True)
class Config:
    origins: list[str] = field(default_factory=lambda: os.getenv('ORIGINS', '').split(','))

    smtp_user: str = os.getenv('SMTP_USER')
    smtp_pass: str = os.getenv('SMTP_PASS')
    smtp_host: str = os.getenv('SMTP_HOST')
    smtp_port: int = os.getenv('SMTP_PORT')

    redis_host: str = os.getenv('REDIS_HOST')
    redis_port: int = os.getenv('REDIS_PORT')

    db_user: str = os.getenv('DB_USER')
    db_pass: str = os.getenv('DB_PASS')
    db_host: str = os.getenv('DB_HOST')
    db_port: int = os.getenv('DB_PORT')
    db_name: str = os.getenv('DB_NAME')

    user_log_path: str = r'logs/user.log'
