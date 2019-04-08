import csv
import os
import json
import pymongo
import socket
import datetime
import nltk

def get_names(triples):
	tagged = nltk.pos_tag(nltk.word_tokenize(triples))
	name_list = []
	name = ""
	for i in tagged:
		if i[1] == "NNP":
			name += i[0]+" "
		else:
			if len(name) != 0:
				name = name.strip()
				if name not in name_list:
					name_list.append(name)
			name = ""
	return name_list

def triple_set(triples):
	return triples.split("\n")
		

def parse_and_store(dic, triples):
	related = get_names(triples)
	#print(related)
	related_str = str(related)
	related_str = related_str[1:(len(related_str)-1)]
	#print(related_str)
	dic.pop('article', None)
	dic['relations'] = related_str.replace('\'','')
	dic['triples'] = triples.split("\n")
	#print(dic)
	client = pymongo.MongoClient('mongodb://localhost:27017')
	db = client['nasty']
	keys = db.collection_names()
	for i in related:
		if i in keys:
			print("Key "+i+" found")
			coll = db[i]
			update = True
			for k in coll.find():
				if k['title'] == dic['title']:
					print(k['title']+"  ==  "+dic['title'])
					update = False
			if update:
				print("Updating : "+i)
				record = db[i]
				result = record.insert_one(dic)
			else:
				print("Replication removed")
		else:
			print("Creating : "+i)
			record = db[i]
			result = record.insert_one(dic)
		#print(result.inserted_id)

def get_all_triples(text):
	host = "192.168.0.14"
	port = 8001
	server = socket.socket()
	server.connect((host,port))
	msg = "parse "+text+"\0"
	server.send(msg.encode())
	msg = server.recv(9216).decode()
	#print(str(msg))
	return msg


def main_routine():
	start = str(datetime.datetime.now())
	files = os.listdir("./data/")
	print(files)
	for f in files:
		db = {}
		with open("./data/"+f,"r") as data:
			content = data.read()
			db = json.loads(content)
			print(str(len(db))+" records found. Starting fact finding.")
			#print(db['3']['article'])
			for i in range(len(db)):
				article = db[str(i)]['article']
				print("Current record : "+str(i))
				triples = get_all_triples(article)
				triples = triples.replace(",", ", ")
				parse_and_store(db[str(i)], triples)
	print("Process started at : "+start)
	print("Process finished at : "+datetime.datetime.now())


main_routine()