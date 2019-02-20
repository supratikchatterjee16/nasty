import rss_util
import classifier_util
import sentence_util
import webpage_util
import file_util
import csv_util
import threading
import time

count = 0
def load_part(*arr):
	rss = rss_util.RSS()
	global count
	for i in arr:
		rss.open(i)
		for j in rss.links:
			count += 1
			content = webpage_util.get_article(j)
			nouns=[]
			for k in content:
				nouns += sentence_util.extract_nouns_proper(k)
			print("\n\n"+str(i)+"\n"+str(nouns))
	
def load_rss_list(arr):
	no_of_threads = 4
	n = int(len(arr)/no_of_threads) 
	threads = []
	for i in range(no_of_threads):
		threads.append(threading.Thread(target=load_part, args=arr[(i*n):((i+1)*n)]))
	for i in threads:
		i.start()
	for i in threads:
		i.join()
	

csv = csv_util.CSV()
try:
	csv.open("rsslist.csv")
except:
	open("rsslist.csv","w+")

var = input("Press a key")

start = time.time()

load_rss_list(csv.data)

elapsed = time.time() - start

print(time.strftime("%H:%M:%S", time.gmtime(elapsed)))

