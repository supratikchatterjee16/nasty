import rss_util
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
			for sentences in content:
				with open("raw.dat","a+") as rawfile:
					rawfile.write(sentences+"\n")
				print(sentences)

def load_rss_list(arr):
	no_of_threads = 5
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
	open("raw.dat")
except:
	open("rsslist.csv","w+")
	open("raw.dat","w+")

var = input("Do you want to launch?")

start = time.time()

load_rss_list(csv.data)

elapsed = time.time() - start

print(time.strftime("%H:%M:%S", time.gmtime(elapsed)))

