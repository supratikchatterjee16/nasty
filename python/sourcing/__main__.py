import csv_util
import rss_util
import file_util
import webpage_util
import sentence_util
import threading
import sys
import os
import datetime
import json

rsslist = []
rsslist_updates = []
links = []
link_updates = []
count = 0
store = {}
def init():
	global rsslist, rsslist_updates, links, link_updates
	rsslist = csv_util.CSV(filename = "customlist.csv", create = False)
	rsslist_updates = csv_util.CSV(filename = "rsslist_updates.csv", create = True)
	links = csv_util.CSV(filename = "links.csv", create = True)
	link_updates = csv_util.CSV(filename = "link_updates.csv", create = True)

def mutex_for_store(count, content):
	try:
		store[count] = content
	except Exception:
		mutex_for_store(count, content)

def routine(*arr):
	global count
	global store
	for i in arr:
		print(i)
		try:
			rss = rss_util.RSS(i)
			content = {}
			for j in rss.items:
				content["title"] = j["title"]
				content["date"] = j["published"]
				content["link"] = j["link"]
				content["article"]= str( webpage_util.get_article(j["link"]))
				mutex_for_store(count,content)
				count += 1
			#print(store.keys())
			print(i+" done. "+str(count)+" records generated.")
		except Exception as e:
			print(e)

def mainprocess():
	global rsslist
	global store
	start = str(datetime.datetime.now())
	#Generate 5 threads
	num = 5
	length = len(rsslist.data)/num
	ls = []
	threads = []
	for i in range(num):
		ls.append(rsslist.data[int(i*length):int((i+1)*length)])
		
	for i in ls:
		threads.append(threading.Thread(target=routine, args=i))
	print("Started sourcing data")
	print("Number of sources : "+str(len(rsslist.data)))
	for i in threads:
		i.start()
	for i in threads:
		i.join()
	
	directory = "./data/"
	if not os.path.exists(directory):
		os.makedirs(directory)
	now = datetime.datetime.now()
	now = now.strftime("%Y-%m-%d_%H_%M")
	with open(directory+now,"w+") as df:
		json.dump(store,df)
	
	#for i in range(num):
		#ls.append(rsslist.data[i:i+1])
	#for source in rsslist:
		#rss = rss_util.RSS(url = source)
		#for i in rss.items:
			#print(i["link"])
	print("Started at : "+start)
	print("Completed at : "+str(datetime.datetime.now()))


#try:
init()
mainprocess()
sys.exit(0)
#except Exception as e:
	#print("System error : ")
	#print(e)
	#sys.exit(1)