import os
import logging
from dotenv import load_dotenv

logging.basicConfig(
    level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def get_env() -> str:
    environment = os.getenv('ENV', 'dev')
    return f'.env.{environment}'


environment = get_env()
load_dotenv(environment)


def get_env_variable(var_name, default=None) -> str:
    value = os.getenv(var_name, default)
    if value is None:
        logger.error(f'Variable de entorno faltante: {var_name}')
        raise ValueError(f'Variable de entorno faltante: {var_name}')
    return value


DB_HOST = get_env_variable('DB_HOST')
DB_PORT = int(get_env_variable('DB_PORT'))
DB_DATABASE = get_env_variable('DB_DATABASE')
DB_USERNAME = get_env_variable('DB_USERNAME')
DB_PASSWORD = get_env_variable('DB_PASSWORD')

APP_PORT = int(get_env_variable('APP_PORT'))
APP_HOST = get_env_variable('APP_HOST')
APP_NAME = get_env_variable('APP_NAME')
APP_DESCRIPTION = get_env_variable('APP_DESCRIPTION')

ALLOWED_ORIGINS = get_env_variable('ALLOWED_ORIGINS').split(',')

EXTERNAL_API_URL = get_env_variable('EXTERNAL_API_URL')

ENV = os.getenv('ENV')

logger.info(f'Entorno cargado: {ENV} desde {environment}')
