import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["inventory"]

mycol = mydb["product_info"]