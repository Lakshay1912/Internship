# Databricks notebook source
import pyspark
from pyspark.sql import SparkSession
#SparkSession is now the entry point of Spark
#SparkSession can also be construed as gateway to spark libraries
  
#create instance of spark class
spark=SparkSession.builder.appName('housing_price_model').getOrCreate()
  
#create spark dataframe of input csv file
df = spark.read\
    .format("s3selectCSV")\
    .load("s3://raniai/cruise_ship_info.csv")

df.show(10)
df.printSchema()

from pyspark.ml.feature import StringIndexer
indexer=StringIndexer(inputCol='_c1',outputCol='cruise_cat')
indexed=indexer.fit(df).transform(df)

for item in indexed.head(5):
    print(item)
    print('\n')
    
from pyspark.ml.linalg import Vectors
from pyspark.ml.feature import VectorAssembler
#creating vectors from features
#Apache MLlib takes input if vector form
assembler=VectorAssembler(inputCols=['_c2',
 '_c3',
 '_c4',
 '_c5',
 '_c6',
 '_c7',
 'cruise_cat'],outputCol='features')
output=assembler.transform(indexed)
output.select('features','_c8').show(5)
#output as below

#final data consist of features and label which is crew.
final_data=output.select('features','_c8')
#splitting data into train and test
train_data,test_data=final_data.randomSplit([0.7,0.3])
train_data.describe().show()
test_data.describe().show()
