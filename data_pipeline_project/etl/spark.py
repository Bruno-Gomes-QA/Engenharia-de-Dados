from pyspark.sql import SparkSession


class SparkSessionManager:
    def __enter__(self):
        self.spark = SparkSession.builder\
            .appName('etl-reciclagem')\
            .getOrCreate()
        return self.spark

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.spark.stop()
