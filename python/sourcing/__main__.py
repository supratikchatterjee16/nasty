import csv_util
import rss_util
import file_util
import webpage_util
import sentence_util
import threading
import sys
import os
import datetime

rsslist = []
rsslist_updates = []
links = []
link_updates = []

def init():
	global rsslist, rsslist_updates, links, link_updates
	rsslist = csv_util.CSV(filename = "rsslist.csv", create = False)
	rsslist_updates = csv_util.CSV(filename = "rsslist_updates.csv", create = True)
	links = csv_util.CSV(filename = "links.csv", create = True)
	link_updates = csv_util.CSV(filename = "link_updates.csv", create = True)

def routine(*arr):
	directory = "./data/"
	if not os.path.exists(directory):
		os.makedirs(directory)
	now = datetime.datetime.now()
	now = now.strftime("%Y-%m-%d_%H_%M")
	for i in arr:
		print(i)
		rss = rss_util.RSS(i)
		fp = open("./data/"+now,"a+")
		for j in rss.items:
			content = j["title"]+"\n"
			content += str( webpage_util.get_article(j["link"]))
			content += "\n\n\n"
			fp.write(content)
		print(i+" done")
		fp.close()

def mainprocess():
	global rsslist
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
	
	#for i in range(num):
		#ls.append(rsslist.data[i:i+1])
	#for source in rsslist:
		#rss = rss_util.RSS(url = source)
		#for i in rss.items:
			#print(i["link"])
	print("Completed at : "+str(datetime.datetime.now()))


#try:
init()
mainprocess()
sys.exit(0)
#except Exception as e:
	#print("System error : ")
	#print(e)
	#sys.exit(1)