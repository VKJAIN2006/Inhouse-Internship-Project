from pyspark.sql import SparkSession
from pyspark.sql.functions import col
import os

# Create Spark Session
spark = SparkSession.builder \
    .appName("SalesAnalysis") \
    .getOrCreate()

# Create output directory if it doesn't exist
os.makedirs("output", exist_ok=True)

# Read CSV file
df = spark.read.csv(
    "data/sales.csv",
    header=True,
    inferSchema=True
)

print("\n===== Original Data =====")
df.show()


# 1. Sort products by sales descending

sorted_df = df.orderBy(col("sales").desc())

print("\n===== Products Sorted By Sales =====")
sorted_df.show()

sorted_rows = sorted_df.collect()

with open("output/sorted_products.csv", "w") as f:
    f.write("product_id,product_name,category,sales\n")
    for row in sorted_rows:
        f.write(
            f"{row.product_id},{row.product_name},{row.category},{row.sales}\n"
        )


# 2. Top 3 products with highest sales

top3_df = sorted_df.limit(3)

print("\n===== Top 3 Products =====")
top3_df.show()

top3_rows = top3_df.collect()

with open("output/top3_products.csv", "w") as f:
    f.write("product_id,product_name,category,sales\n")
    for row in top3_rows:
        f.write(
            f"{row.product_id},{row.product_name},{row.category},{row.sales}\n"
        )


# 3. Products with sales > 80000

high_sales_df = df.filter(col("sales") > 80000)

print("\n===== Products With Sales > 80000 =====")
high_sales_df.show()

high_sales_rows = high_sales_df.collect()

with open("output/high_sales_products.csv", "w") as f:
    f.write("product_id,product_name,category,sales\n")
    for row in high_sales_rows:
        f.write(
            f"{row.product_id},{row.product_name},{row.category},{row.sales}\n"
        )

print("\nAll output files saved successfully!")

spark.stop()