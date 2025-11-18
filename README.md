# EzyShop Big Data Prototype

## Overview

This prototype demonstrates a Big Data solution for EzyShop's e-commerce analytics using Apache Spark for batch processing of structured and unstructured data.

## Business Problem

EzyShop needs to analyze customer behavior by integrating:

\- \*\*Structured data:\*\* Sales transactions

\- \*\*Unstructured data:\*\* Customer reviews

The goal is to identify top-selling products and extract customer sentiment insights.


## Architecture

### Components

1\. \*\*Data Sources:\*\* CSV (sales) and JSON (reviews)

2\. \*\*Processing Engine:\*\* Apache Spark 3.5 (local mode)

3\. \*\*Storage:\*\* Parquet format for optimized analytics

4\. \*\*Analytics:\*\* Product rankings and sentiment analysis


### Data Flow

```

sales.csv ──┐

&nbsp;           ├──> Apache Spark ──> Processing ──> Parquet Output

reviews.json┘

```


## Technology Stack

\- \*\*Python 3.11\*\*

\- \*\*Apache Spark (PySpark) 3.5.3\*\*

\- \*\*Java 17 (LTS)\*\*

\- \*\*Hadoop 3.3.5\*\* (Windows binaries)


## System Requirements

\- Windows 10/11

\- Python 3.11

\- Java 17

\- 4GB RAM minimum

\- 1GB free disk space


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



1\. \*\*Top Products\*\* (`output/top\_products/`)

&nbsp;  - Products ranked by sales volume

&nbsp;  - Identifies bestsellers and underperformers



2\. \*\*Sentiment Analysis\*\* (`output/sentiment\_counts/`)

&nbsp;  - Keyword frequency from customer reviews

&nbsp;  - Positive: "good", "love"

&nbsp;  - Negative: "bad", "slow"


## Sample Results
### Top Products

| Product ID | Sales Count |

|------------|-------------|

| 101        | 3           |

| 102        | 3           |

| 108        | 2           |


### Sentiment Keywords

| Keyword | Count |

|---------|-------|

| good    | 8     |

| bad     | 5     |

| slow    | 4     |

| love    | 3     |


## Project Structure

```

EzyShop\_BigData\_Prototype/

├── data/

│   ├── sales.csv

│   └── reviews.json

├── scripts/

│   ├── prototype.py

│   └── view\_results.py

├── output/

│   ├── top\_products/

│   └── sentiment\_counts/

├── test\_log.md

└── README.md

```


## Testing

See \[test\_log.md](test\_log.md) for detailed test results and issue resolutions.


## Future Enhancements

\- Real-time streaming with Kafka

\- Machine learning for predictive analytics

\- Cloud deployment (AWS EMR / Azure HDInsight)

\- Interactive dashboards (Power BI / Tableau)


## Author

Stacie Kipruto

