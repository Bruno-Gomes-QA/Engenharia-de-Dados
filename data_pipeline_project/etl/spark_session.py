from pyspark.sql import SparkSession


class SparkSessionManager:
    def __enter__(self):
        try:
            self.spark = (
                SparkSession.builder.appName('ReadParquetFromS3')
                .config(
                    'spark.hadoop.fs.s3a.impl',
                    'org.apache.hadoop.fs.s3a.S3AFileSystem',
                )
                .config(
                    'spark.hadoop.fs.s3a.aws.credentials.provider',
                    'com.amazonaws.auth.profile.ProfileCredentialsProvider',
                )
                .config('spark.hadoop.fs.s3a.aws.profile', 'default')
                .config('spark.hadoop.fs.s3a.endpoint', 's3.amazonaws.com')
                .getOrCreate()
            )
            return self.spark
        except Exception as e:
            raise ValueError(f'Failed to create Spark session')

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.spark.stop()
