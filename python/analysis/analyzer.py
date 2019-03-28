import csv
import os
import json
import socket

def get_all_triples(text):
	host = "192.168.0.14"
	port = 8001
	server = socket.socket()
	server.connect((host,port))
	msg = "parse "+text
	server.send(msg.encode())
	msg = server.recv(1024).decode()
	print(str(msg))
	return msg



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
			triples = get_all_triples(article)

