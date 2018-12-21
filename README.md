# sparkproject

# Description: 
Repository for the sparkproject gas prices. Our purpose is to study the evolution of gaz prices on a period of 2 years and to explain the price given previous prices.

# Installation: 

- Download apache spark version 2.4.0 at https://spark.apache.org/downloads.html
- Unzip file
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

**Contents:**
* [Compatibility](#compatibility)
* [Using with PySpark](#using-with-pyspark)
* [Using with PySpark shell](#using-with-pyspark-shell)
* [Building](#building)
* [API](#api)
* [Examples](#examples)
* [Problems / ideas?](#problems--ideas)
* [Contributing](#contributing)



Compatibility
-------------

### Spark
PySpark is tested to be compatible with Spark 1.4, 1.5 and 1.6. 

### Python


### Configuration

Problems / ideas?
-----------------
Feel free to use the issue tracker propose new functionality and / or report bugs.


