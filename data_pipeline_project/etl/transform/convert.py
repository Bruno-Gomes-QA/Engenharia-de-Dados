import os
from pyspark.sql import Row
from pyspark.sql import SparkSession


class Convert:
    def __init__(self, spark: SparkSession):
        self.spark = spark

    def json_to_parquet(self, data, temp_path):
        rows = [Row(**item) for item in data]
        df = self.spark.createDataFrame(rows).repartition(1)

        df.write.parquet(temp_path, mode='overwrite')

        parquet_file = None
        for file in os.listdir(temp_path):
            if file.endswith(".parquet") and file.startswith("part-"):
                parquet_file = os.path.join(temp_path, file)
                break

        if not parquet_file:
            raise FileNotFoundError("Nenhum arquivo Parquet foi encontrado no diretório temporário.")

        return parquet_file
