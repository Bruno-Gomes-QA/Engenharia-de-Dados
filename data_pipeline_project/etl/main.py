import logging
import tempfile
from config import Config
from spark_session import SparkSessionManager
from s3_session import S3Session
from extract.appsheet import AppSheetExtractor
from transform.convert import Convert
from loading.upload_manager import UploadManager

# Init Logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('etl.log'), logging.StreamHandler()],
)
logger = logging.getLogger(__name__)


def main():
    try:
        with SparkSessionManager() as spark:
            with S3Session() as s3:
                config = Config()
                appsheet_extractor = AppSheetExtractor(
                    config.API_URL, config.APPSHEET_API_KEY, config.APP_ID, logger
                )
                convert = Convert(spark, logger)
                upload_manager = UploadManager(s3, logger)

                for table_name in config.TABLE_NAMES:
                    logger.info(f'Extracting data from table: {table_name}')
                    data = appsheet_extractor.extract(table_name)
                    with tempfile.TemporaryDirectory() as tmpdir:
                        temp_parquet_file = convert.json_to_parquet(
                            data, tmpdir
                        )
                        logger.info(
                            f'Data from {table_name} transformed to Parquet, and saved at: {temp_parquet_file}'
                        )

                        s3_key = f'{config.AWS_BUCKET_PATH}/{table_name}/{table_name}.parquet'
                        upload_manager.upload_to_s3(
                            temp_parquet_file,
                            config.AWS_BUCKET_NAME,
                            s3_key
                        )

    except Exception as e:
        logger.exception(f'ETL process failed, error: {e}')


if __name__ == '__main__':
    main()
