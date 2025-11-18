# EzyShop Big Data Prototype

## Overview

This prototype demonstrates a Big Data solution for EzyShop's e-commerce analytics using Apache Spark for batch processing of structured and unstructured data.

## Business Problem

EzyShop needs to analyze customer behavior by integrating:

**Structured data:** Sales transactions

**Unstructured data** Customer reviews

The goal is to identify top-selling products and extract customer sentiment insights.


## Architecture

### Components

**Data Sources:** CSV (sales) and JSON (reviews)

**Processing Engine:** Apache Spark 3.5 (local mode)

**Storage:** Parquet format for optimized analytics

**Analytics:** Product rankings and sentiment analysis


### Data Flow

```

sales.csv ──┐

&nbsp;           ├──> Apache Spark ──> Processing ──> Parquet Output

reviews.json┘

```


## Technology Stack

**Python 3.11**

**Apache Spark (PySpark) 3.5.3**

**Java 17 (LTS)**

**Hadoop 3.3.5** (Windows binaries)


## System Requirements

- Windows 10/11

- Python 3.11

- Java 17

- 4GB RAM minimum

- 1GB free disk space


## Installation \& Setup
### 1. Clone Repository

```bash

git clone https://github.com/stacie-kipruto/EzyShop-BigData-Prototype.git

cd EzyShop-BigData-Prototype

```

### 2. Install Dependencies

```bash

pip install pyspark

```


### 3. Configure Hadoop (Windows only)

1\. Download Hadoop 3.3.5 binaries: https://github.com/cdarlint/winutils

2\. Extract to `C:\\hadoop`

3\. Set environment variables:

```powershell

$env:HADOOP\_HOME = "C:\\hadoop"

$env:PATH = "$env:PATH;C:\\hadoop\\bin"

```

## Running the Prototype

### Execute Main Pipeline

```bash

cd scripts

python prototype.py

```

### View Results

```bash

python view\_results.py

```

## Output

The prototype generates two analytics outputs:



1. **Top Products** (`output/top\_products/`)

&nbsp;  - Products ranked by sales volume

&nbsp;  - Identifies bestsellers and underperformers



2. **Sentiment Analysis** (`output/sentiment\_counts/`)

&nbsp;  - Keyword frequency from customer reviews

&nbsp;  - Positive: "good", "love"

&nbsp;  - Negative: "bad", "slow"


## Sample Results
### Top Products

<img width="284" height="225" alt="image" src="https://github.com/user-attachments/assets/08ac93d9-e9c3-42c1-89bd-4d9788aa978b" />



### Sentiment Keywords

<img width="197" height="152" alt="image" src="https://github.com/user-attachments/assets/a02b885b-88b1-4aad-882a-29b4ee0949c4" />


## Project Structure


<img width="208" height="476" alt="image" src="https://github.com/user-attachments/assets/dd5d6c50-95c6-4f18-9662-c13a92d60b94" />



## Testing

See \[test\_log.md](test\_log.md) for detailed test results and issue resolutions.


## Future Enhancements

- Real-time streaming with Kafka

- Machine learning for predictive analytics

- Cloud deployment (AWS EMR / Azure HDInsight)

- Interactive dashboards (Power BI / Tableau)


## Author

Stacie Kipruto

