from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("ReciclagemETL") \
    .config("spark.some.config.option", "config-value") \
    .getOrCreate()

def json_to_parquet(input_path, output_path):
  df = spark.read.json(input_path)

  df.write.mode("overwrite").parquet("caminho/para/saida_parquet/")

