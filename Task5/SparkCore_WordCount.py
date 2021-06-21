import argparse
import logging

from pyspark.sql import SparkSession

#logger = logging.getLogger('emr_logger')
#logging.basicConfig(filename = 's3://raniai/output.log',level=logging.INFO, format='%(levelname)s: %(message)s',filemode='w')
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

def wordCount(output_uri):

	spark = SparkSession.builder\
        	.master("local")\
        	.appName("Task2")\
        	.getOrCreate()
	sc = spark.sparkContext
	data = [1,2,3,4,5,1,2,3,4,5,4]
	rdd = sc.parallelize(data,5)
	word_count = rdd.map(lambda x: (x,1))\
                	.reduceByKey(lambda x,y:(x+y))
	print(word_count.collect())

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--output_uri', help="The URI where output is saved, typically an S3 bucket.")
    args = parser.parse_args()
    wordCount('s3://raniai')

