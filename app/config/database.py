"Connect to Database"
from pymongo import MongoClient

client = MongoClient("mongodb://mongodb_container:27017")

db = client.ML_deploy

collection_name = db["user"]
