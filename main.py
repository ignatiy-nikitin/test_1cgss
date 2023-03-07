import datetime

from loguru import logger

from db import create_all_db_tables
from logger import init_logger
from parser import parse_xml_files_dir
from settings import XML_FILES_DIR_PATH


@logger.catch
def main():
    init_logger()
    logger.info(f'New run...')
    datetime_start = datetime.datetime.now()
    create_all_db_tables()
    parse_xml_files_dir(XML_FILES_DIR_PATH)
    datetime_end = datetime.datetime.now()
    datetime_of_execution = datetime_end - datetime_start
    logger.info(f'End run. Time of execution: {datetime_of_execution}')


if __name__ == "__main__":
    main()
