# Import SparkSession
from pyspark.sql import SparkSession

# Create SparkSession 
spark = SparkSession.builder \
      .master("local[1]") \
      .appName("SparkByExamples.com") \
      .getOrCreate() 

# Create RDD from external Data source
rdd2 = spark.sparkContext.textFile("/Users/some_path/sample_json/json1.json")

pass

