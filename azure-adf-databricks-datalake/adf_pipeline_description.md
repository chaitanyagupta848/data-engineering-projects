## Azure Data Factory Pipeline

### Activities
- Copy Activity:
  - Source: Blob Storage / Azure SQL
  - Sink: ADLS Bronze layer

- Databricks Notebook Activity:
  - Executes PySpark transformations
  - Writes Silver & Gold layers

### Triggers
- Daily scheduled trigger
- Supports incremental loads

### Error Handling
- Retry policies enabled
- Failure alerts via Azure Monitor
