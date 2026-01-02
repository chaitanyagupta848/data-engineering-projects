# Azure Enterprise Data Lake Pipeline (ADF + Databricks)

## Overview
This project demonstrates an end-to-end Azure data engineering pipeline using
Azure Data Factory, Azure Databricks, and Azure Data Lake Storage (ADLS)
following the Bronze / Silver / Gold architecture.

## Architecture
Source Data → Azure Data Factory → ADLS (Bronze)
→ Azure Databricks (Transformations)
→ ADLS (Silver / Gold)
→ Azure SQL / Synapse

## Technologies Used
- Azure Data Factory
- Azure Databricks (PySpark)
- Azure Data Lake Storage Gen2
- Azure SQL / Synapse
- Python, Spark SQL

## Pipeline Flow
1. Ingest raw CSV/JSON files using ADF
2. Store raw data in ADLS (Bronze)
3. Clean & transform data using Databricks
4. Write curated data to Silver & Gold layers
5. Load final data into Azure SQL/Synapse

## Use Cases
- Enterprise Data Lake
- Analytics & Reporting
- ML-ready curated datasets
