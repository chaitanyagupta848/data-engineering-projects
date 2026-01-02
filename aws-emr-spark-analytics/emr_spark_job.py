from pyspark.sql import SparkSession
from pyspark.sql.functions import col

spark = SparkSession.builder.appName("EMRSparkJob").getOrCreate()

df = spark.read.parquet("s3://my-bucket/raw/sales")

clean_df = df.filter(col("amount") > 0)

clean_df.write.mode("overwrite") \
    .parquet("s3://my-bucket/processed/sales")
