import logging
import os
from dotenv import load_dotenv
from extract.appsheet import AppSheetExtractor
from spark import SparkSessionManager

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def main():
    try:
        with SparkSessionManager() as spark:

            load_dotenv('.env.appsheet')
            APPSHEET_API_KEY = os.getenv('APPSHEET_API_KEY')
            API_URL = os.getenv('APPSHEET_API_URL')
            APP_ID = os.getenv('APPSHEET_APP_ID')
            TABLE_NAMES = ['Produtos']

            if not all([APPSHEET_API_KEY, API_URL, APP_ID, TABLE_NAMES]):
                raise ValueError('Missing environment variables')

            appsheet_extractor = AppSheetExtractor(API_URL, APPSHEET_API_KEY, APP_ID)

            for table_name in TABLE_NAMES:
                logger.info(f'Extracting data from table: {table_name}')
                error, data = appsheet_extractor.extract(table_name=table_name)

                if error:
                    logger.error(f'Failed to extract data from {table_name}: {error}')
                else:
                    logger.info(f'Data extracted successfully from {table_name}')

    except Exception as e:
        logger.exception('ETL process failed')


if __name__ == '__main__':
    main()
