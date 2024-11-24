import logging
import tempfile
from config import config
from extract.appsheet import AppSheetExtractor
from spark import SparkSessionManager
from transform.convert import Convert

# Init Logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("etl.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

def main():
    try:
        with SparkSessionManager() as spark:
            appsheet_extractor = AppSheetExtractor(config.API_URL, config.APPSHEET_API_KEY, config.APP_ID)
            convert = Convert(spark)

            for table_name in config.TABLE_NAMES:
                logger.info(f'Extracting data from table: {table_name}')
                error, data = appsheet_extractor.extract(table_name=table_name)

                if error:
                    logger.error(f'Failed to extract data from {table_name}: {error}')
                else:
                    logger.info(f'Data extracted successfully from {table_name}')
                    with tempfile.TemporaryDirectory() as tmpdir:
                        temp_parquet_path = convert.json_to_parquet(data, tmpdir)
                        logger.info(f'Data from {table_name} transformed to Parquet, and saved at: {temp_parquet_path}')
                    
                    # Create a UploadManager class to upload the Parquet file to S3

    except Exception as e:
        logger.exception('ETL process failed')

if __name__ == '__main__':
    main()