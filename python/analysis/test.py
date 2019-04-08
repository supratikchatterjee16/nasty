import pymongo
client = pymongo.MongoClient('mongodb://localhost:27017')
db = client['nasty']
keys = db.collection_names()
mycol = db[keys[0]]
for i in mycol.find():
	print(i)