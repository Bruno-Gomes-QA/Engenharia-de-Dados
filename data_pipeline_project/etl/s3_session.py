import boto3

class S3Session:
    def __enter__(self):
        try:
            self.s3 = boto3.client('s3')
            return self.s3
        except Exception as e:
            raise ValueError(f'Failed to initialize S3Session: {e}')

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.s3.close()