from pyspark import SparkConf, SparkContext
conf = SparkConf().setMaster("local").setAppName("My App")
sc = SparkContext(conf = conf)


lines = sc.textFile("README.md")
lines.count()
pythonLines = lines.filter(lambda line: "Python" in line)
pythonLines.persist(StorageLevel.MEMORY_ONLY_SER)
pythonlines.count()
pythonLines.first()


