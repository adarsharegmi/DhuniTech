import os
import typing
from pydantic import PostgresDsn
from dotenv import load_dotenv, find_dotenv
from nepAddy_core.lib.settings import AbstractSettings


load_dotenv(find_dotenv())
DB_USER = os.environ.get("DB_USER", "ncligagsmtvynw")
DB_PASSWORD = os.environ.get("DB_PASSWORD", "64f263ce4b9c0ed3529197f0414e6c6cb055b94db51ef02c9f06546789929794")
DB_PORT = os.environ.get("DB_PORT", "5432")
DB_HOST = os.environ.get("HOST", "ec2-54-165-90-230.compute-1.amazonaws.com")
DB_NAME = os.environ.get("DB_NAME", "d7odjtd7b05gh8")


class Settings(AbstractSettings):
    pg_dsn: PostgresDsn
    components: typing.List[str]
    secret_key: str
    alembic_config: str
    page_size: int
    debug: bool
    token_life_time: int
    SIGN_IN_URL: str
    SIGN_UP_URL: str


def settings_factory() -> Settings:
    return Settings(
        pg_dsn=typing.cast(
            PostgresDsn,
            f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}",
        ),
        components=[
            "dhuni_tech.candidate",
            "dhuni_tech.job"
            
        ],
        secret_key="2#$%^&SDFGHJKLOIUYTR@#$%^&*987654#$%^&*kJHGF3$%^&*",
        alembic_config="alembic.ini",
        page_size=50,
        debug=True,
        token_life_time=259200,
        SIGN_IN_URL = "http://127.0.0.1:8000/api/v1/login/",
        SIGN_UP_URL = "http://127.0.0.1:8000/api/v1/user_register/"
    )
