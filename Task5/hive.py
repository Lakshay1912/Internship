# Databricks notebook source
import os
os.listdir(os.getcwd())
from pyspark.sql import SparkSession

spark = SparkSession.builder.enableHiveSupport().getOrCreate()
os.listdir(os.getcwd())
spark.sql('show databases').show()
spark.sql('show tables').show()
spark.sql("describe function instr").show(truncate = False)
spark.sql('create database movies')
spark.sql('show databases').show()

spark.sql('use movies')
spark.sql('create table movies \
         (movieId int,title string,genres string) \
         row format delimited fields terminated by ","\
         stored as textfile')
spark.sql("show tables").show()
spark.sql("create table genres_by_count\
           ( genres string,count int)\
           stored as AVRO" )
spark.sql("show tables").show()
spark.sql('create table student \
         (roll_no int,name string,phone int) \
         row format delimited fields terminated by ","\
         stored as textfile')
spark.sql('create table customer \
         (customer_id int,name string,phone int) \
         row format delimited fields terminated by ","\
         stored as textfile')
spark.sql("show tables").show()

# COMMAND ----------


