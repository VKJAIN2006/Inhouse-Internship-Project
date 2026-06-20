from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .master("local[*]") \
    .appName("PartitionManagement") \
    .getOrCreate()

df = spark.range(5000000)

print("Initial partitions:", df.rdd.getNumPartitions())

df_repartition = df.repartition(12)
print("After repartition:", df_repartition.rdd.getNumPartitions())

df_coalesce = df_repartition.coalesce(3)
print("After coalesce:", df_coalesce.rdd.getNumPartitions())

spark.stop()