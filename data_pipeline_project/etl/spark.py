from pyspark.sql import SparkSession


class SparkSessionManager:
    def __enter__(self):
        try:
            self.spark = SparkSession.builder.appName(
                'etl-reciclagem'
            ).getOrCreate()
            return self.spark
        except Exception as e:
            raise ValueError(f'Failed to create Spark session')

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.spark.stop()
