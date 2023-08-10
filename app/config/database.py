"Connect to Database"
from pymongo import MongoClient

client = MongoClient("mongodb+srv://hungledut:hung782002@hung3que.yxqk6qs.mongodb.net/")

db = client.ML_deploy

collection_name = db["user"]
