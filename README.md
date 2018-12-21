# sparkproject


## Description: 
Repository for the sparkproject gas prices. Our purpose is to study the evolution of gaz prices on a period of 2 years and to explain the price given previous prices.

### Date : Friday 21 December
### Language : Python
### Context : Mini Project For Course of Big Data



## Getting Started

### Prerequisites

- Download apache spark version 2.4.0 at https://spark.apache.org/downloads.html
- Unzip file
- Download Java SE Development Kit 8u191 at https://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html

### Installation

- Download pyspark
```bash
pip install pyspark
```
- change environment variable from Python and launch SparkContext
```python
os.environ['JAVA_HOME'] = 'C:\Program Files\Java\jdk1.8.0_144'
os.environ['SPARK_HOME'] = 'C:\\Users\\Name\\spark-2.4.0-bin-hadoop2.7'
os.environ['SPARK_LOCAL_HOSTNAME'] = 'localhost'
os.environ['SPARK_LOCAL_IP'] = 'LOCAl_IP'
sc = pyspark.SparkContext()
```

You are ready !


# Authors
- Fanny DOUCHET & Mickael JUILLET



