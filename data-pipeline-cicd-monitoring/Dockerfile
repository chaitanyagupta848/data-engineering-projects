FROM apache/spark-py:3.5.1

WORKDIR /app

COPY spark_job.py /app/spark_job.py
COPY logging.conf /app/logging.conf

CMD ["spark-submit", "/app/spark_job.py"]
