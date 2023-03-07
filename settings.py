import os

from dotenv import load_dotenv

env_file = os.path.join(os.path.dirname(__file__), '.env')

if os.path.exists(env_file):
    load_dotenv(env_file)

DEBUG = os.environ.get('DEBUG') == 'True'
DOCKER = os.environ.get('DOCKER') == 'True'

LOGGING_LEVEL = os.environ.get('LOGGING_LEVEL', 'INFO')
LOGGING_FILE_PATH = os.environ.get('LOGGING_FILE_PATH', 'logs/logs.log')

DB_HOST = os.environ.get('DB_HOST', 'localhost')

try:
    DB_NAME = os.environ['DB_NAME']
    DB_USER = os.environ['DB_USER']
    DB_PASSWORD = os.environ['DB_PASSWORD']

    if DOCKER:
        XML_FILES_DIR_PATH = '/xml_files'
    else:
        XML_FILES_DIR_PATH = os.environ['XML_FILES_DIR_PATH']

except KeyError as e:
    raise Exception(f'Set all variables in .env file. Variable required: {e}')
