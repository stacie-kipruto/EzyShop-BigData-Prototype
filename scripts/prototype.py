from pyspark.sql import SparkSession
from pyspark.sql.functions import col, split, explode, lower

# 1. Create Spark session
spark = SparkSession.builder.appName("EzyShopPrototype").getOrCreate()

# 2. Load structured data (sales)
sales = spark.read.csv("../data/sales.csv", header=True, inferSchema=True)

# 3. Load unstructured data (customer reviews)
reviews = spark.read.json("../data/reviews.json")

# 4. Simple batch analytics
top_products = sales.groupBy("product_id").count().orderBy(col("count").desc())

# 5. Simple unstructured processing (keyword sentiment)
keywords = ["good", "bad", "slow", "love"]
review_words = reviews.select(explode(split(lower(col("review_text")), " ")).alias("word"))

sentiment_counts = review_words.filter(col("word").isin(keywords)).groupBy("word").count()

# 6. Save output (CHANGED TO PARQUET)
top_products.write.mode("overwrite").parquet("../output/top_products")
sentiment_counts.write.mode("overwrite").parquet("../output/sentiment_counts")

spark.stop()