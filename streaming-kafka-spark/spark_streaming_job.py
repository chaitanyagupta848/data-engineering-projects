from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col, to_timestamp
from pyspark.sql.types import StructType, StringType, DoubleType, IntegerType

spark = SparkSession.builder \
    .appName("KafkaSparkStreaming") \
    .getOrCreate()

spark.sparkContext.setLogLevel("WARN")

schema = StructType() \
    .add("event_id", IntegerType()) \
    .add("user_id", IntegerType()) \
    .add("event_type", StringType()) \
    .add("amount", DoubleType()) \
    .add("event_time", StringType())

df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "ecommerce_events") \
    .load()

parsed_df = df.select(
    from_json(col("value").cast("string"), schema).alias("data")
).select("data.*")

final_df = parsed_df.withColumn(
    "event_time", to_timestamp("event_time")
)

query = final_df.writeStream \
    .format("parquet") \
    .option("path", "output/events") \
    .option("checkpointLocation", "output/checkpoints") \
    .outputMode("append") \
    .start()

query.awaitTermination()
