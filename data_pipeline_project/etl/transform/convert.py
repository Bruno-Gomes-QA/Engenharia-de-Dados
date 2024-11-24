import tempfile
from pyspark.sql import Row
from pyspark.sql import SparkSession

class Convert:
    def __init__(self, spark: SparkSession):
        self.spark = spark

    def json_to_parquet(self, data, temp_path):
        rows = [Row(**item) for item in data]
        df = self.spark.createDataFrame(rows).repartition(1)
        
        temp_parquet_path = f"{temp_path}/data.parquet"
        df.write.parquet(temp_parquet_path, mode='overwrite')

        return temp_parquet_path
