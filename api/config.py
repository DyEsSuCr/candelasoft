from pydantic_settings import BaseSettings
import os


class Settings(BaseSettings):
    DB_HOST: str
    DB_PORT: int
    DB_DATABASE: str
    DB_USERNAME: str
    DB_PASSWORD: str

    APP_PORT: int
    APP_HOST: str
    APP_NAME: str
    APP_DESCRIPTION: str

    ALLOWED_ORIGINS: str
    EXTERNAL_API_URL: str
    ENV: str

    class Config:
        env_file = '.env.prod' if os.getenv('ENV') == 'prod' else '.env.dev'


settings = Settings()
