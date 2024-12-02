

class UploadManager:
    def __init__(self, s3, logger):
        self.logger = logger
        try:
            self.s3_client = s3
        except Exception as e:
            self.logger.error(f'Failed to initialize UploadManager: {e}')
            raise ValueError(e)

    def upload_to_s3(self, file_path, bucket_name, s3_key):
        try:
            self.s3_client.upload_file(file_path, bucket_name, s3_key)
            self.logger.info(
                f'Successfully uploaded {file_path} to s3://{bucket_name}/{s3_key}'
            )
        except Exception as e:
            self.logger.error(
                f'Failed to upload {file_path} to s3://{bucket_name}/{s3_key}: {e}'
            )
            raise ValueError(e)
