import csv
import os
import json
import socket

def get_all_triples(text):
	host = ""
	port = 8888
	server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server.connect((host,port))
	server.send(text)
	msg = server.recv().decode()
	print(msg)

files = os.listdir("./data/")
print(files)
for f in files:
	db = {}
	with open("./data/"+f,"r") as data:
		content = data.read()
		try:
			db = json.loads(content)
			print(str(len(db))+" records found. Starting fact finding.")
			#print(db['3']['article'])
			for i in range(len(db)):
				article = db[str(i)]['article']
				triples = get_all_triple(article)
		except Exception as e:
			print(len(content))
			print(e)
