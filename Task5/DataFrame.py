from pyspark.sql import SparkSession

spark = SparkSession.builder\
        .master("local")\
        .appName("SparkSql")\
        .getOrCreate()
sc = spark.sparkContext

df = spark.read\
    .format("s3selectCSV")\
    .load("s3://raniai/student_marks_data.csv")

print(df.printSchema())
print(df.show(5))