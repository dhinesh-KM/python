import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["student"]

mycol = mydb["grade_info"]