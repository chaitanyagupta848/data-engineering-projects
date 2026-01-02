from pyspark.sql import SparkSession
from pyspark.sql.functions import col
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("DataPipelineJob")

spark = SparkSession.builder \
    .appName("CICD_Spark_Pipeline") \
    .getOrCreate()

logger.info("Spark job started")

df = spark.read.json("input/data.json")

clean_df = df.filter(col("amount") > 0)

clean_df.write.mode("overwrite").parquet("output/processed_data")

logger.info("Spark job completed successfully")

spark.stop()
