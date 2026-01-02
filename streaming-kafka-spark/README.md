# Streaming Data Pipeline (Kafka → Spark → Parquet)

## Overview
End-to-end streaming data pipeline that simulates real-time e-commerce events,
ingests them into Kafka, processes using Spark Structured Streaming,
and stores cleaned data in Parquet format.

## Architecture
Producer (Python) → Kafka → Spark Structured Streaming → Parquet

## Technologies
- Apache Kafka
- PySpark (Structured Streaming)
- Python
- Parquet
- Docker (optional)

## How to Run
1. Start Kafka using Docker
2. Run Kafka producer
3. Run Spark streaming job

## Use Cases
- Real-time analytics
- Fraud detection pipelines
- Clickstream processing
