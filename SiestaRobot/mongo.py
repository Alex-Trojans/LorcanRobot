from pymongo import MongoClient

from SiestaRobot import MONGO_DB_URI

client = MongoClient()
client = MongoClient(MONGO_DB_URI)
db = client["Anonymous"]
