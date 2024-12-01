import os
from pyspark.sql import Row
from pyspark.sql import SparkSession


class Convert:
    def __init__(self, spark: SparkSession, logger):
        self.spark = spark
        self.logger = logger

    def json_to_parquet(self, data, temp_path):
        try:
            rows = [Row(**item) for item in data]
            df = self.spark.createDataFrame(rows).repartition(1)

            df.write.parquet(temp_path, mode='overwrite')

            parquet_file = None
            for file in os.listdir(temp_path):
                if file.endswith('.parquet') and file.startswith('part-'):
                    parquet_file = os.path.join(temp_path, file)
                    break

            if not parquet_file:
                self.logger.error(
                    'No Parquet file was found in the temporary directory.'
                )
                raise ValueError('No Parquet file was found in the temporary directory.')
            
            self.logger.info(f'Parquet file generated successfully: {parquet_file}')
            return parquet_file
        except Exception as e:
            self.logger.error(f'Failed to convert JSON to Parquet: {e}')
            raise ValueError(e)
