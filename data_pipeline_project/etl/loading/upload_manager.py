import boto3


class UploadManager:
    def __init__(self):
        self.s3_client = boto3.client('s3')

    def upload_to_s3(self, file_path, bucket_name, s3_key, logger):
        try: 
            self.s3_client.upload_file(file_path, bucket_name, s3_key)
            logger.info(
                f'Successfully uploaded {file_path} to s3://{bucket_name}/{s3_key}'
            )
        except Exception as e:
            logger.error(
                f'Failed to upload {file_path} to s3://{bucket_name}/{s3_key}: {e}'
            )
            raise
