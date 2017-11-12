from pyspark.mllib.regression import LabeledPoint
from pyspark.mllib.tree import DecisionTree
from pyspark import SparkConf, SparkContext
from numpy import array

conf = SparkConf().setMaster("local").setAppName("SparkDecisionTree")
sc = SparkContext(conf = conf)
textFile = sc.textFile("./ml-20m/ratings.csv")
print("textFile.count()")
print(textFile.count())
print("textFile.first()")
print(textFile.first())
