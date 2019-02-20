import pymongo
import json

def insert(record):
	connection = pymongo.MongoClient("mongodb://localhost")
	db = connection.nasty
	collection = db[record["name"]]
	element = {"type" : record['type'], "date" : record['date'], "info": record["info"]}
	#info can be a dictionary which can be set to some{"key": "relation/property/article(actual value, i.e. son, daughter, ceo, born)","value" : "Values for the key"}
	collection.insert_one(element)

def get_collections():
	connection = pymongo.MongoClient("mongodb://localhost")
	db = connection.nasty
	print(db.list_collection_names())



get_collections()
