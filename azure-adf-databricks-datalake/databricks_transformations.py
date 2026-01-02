from pyspark.sql import SparkSession
from pyspark.sql.functions import col, to_date

spark = SparkSession.builder.appName("AzureDatabricksETL").getOrCreate()

# Read Bronze data
bronze_df = spark.read.format("csv") \
    .option("header", "true") \
    .load("/mnt/adls/bronze/sales_data")

# Clean & transform
silver_df = bronze_df \
    .filter(col("amount").isNotNull()) \
    .withColumn("order_date", to_date(col("order_date")))

# Write Silver layer
silver_df.write.mode("overwrite") \
    .parquet("/mnt/adls/silver/sales_data")

# Aggregate for Gold layer
gold_df = silver_df.groupBy("country") \
    .sum("amount") \
    .withColumnRenamed("sum(amount)", "total_sales")

gold_df.write.mode("overwrite") \
    .parquet("/mnt/adls/gold/sales_summary")
