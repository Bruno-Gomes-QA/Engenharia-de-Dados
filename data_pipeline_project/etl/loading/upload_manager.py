class UploadManager:
    def __init__(self, spark, logger):
        self.logger = logger
        try:
            self.spark = spark
        except Exception as e:
            self.logger.error(f'Failed to initialize UploadManager: {e}')
            raise ValueError(e)

    def upload_to_s3(self, file_path, bucket_name, s3_key):
        try:
            df = self.spark.read.parquet(file_path)
            df.write.mode('overwrite').parquet(s3_key)
            self.logger.info(
                f'Successfully uploaded {file_path} to s3://{bucket_name}/{s3_key}'
            )
        except Exception as e:
            self.logger.error(
                f'Failed to upload {file_path} to s3://{bucket_name}/{s3_key}: {e}'
            )
            raise ValueError(e)
