from pyspark.sql import SparkSession

# Create Spark session
spark = SparkSession.builder.appName("ViewResults").getOrCreate()

# Read the outputs
print("=" * 50)
print("TOP PRODUCTS (Most Sold)")
print("=" * 50)
top_products = spark.read.parquet("../output/top_products")
top_products.show()

print("\n" + "=" * 50)
print("SENTIMENT ANALYSIS (Keyword Counts)")
print("=" * 50)
sentiment_counts = spark.read.parquet("../output/sentiment_counts")
sentiment_counts.show()

spark.stop()