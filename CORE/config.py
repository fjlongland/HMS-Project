from pydantic import BaseSettings
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    db_hostname: str
    db_port: str
    db_password: str
    db_name: str
    db_username: str
    secret_key: str
    token_algorythm: str
    token_exp_minutes: int

    class config:
        env_file = ".env"

settings = Settings()