import rss_util
import classifier_util
import sentence_util
import webpage_util
import file_util
import csv_util
import threading
import time

def load_part(*arr):
	rss = rss_util.RSS()
	for i in arr:
		rss.open(i)
	for i in rss.links:
		content = webpage_util.get_article(i)
		nouns=[]
		for j in content:
			nouns += sentence_util.extract_nouns_proper(j)
		print("\n\n"+str(i)+"\n"+str(nouns))

def load_rss_list(arr):
	n = int(len(arr)/4) #for 4 threads
	arr1 = arr[0:n]
	arr2 = arr[n:2*n]
	arr3 = arr[n*2:3*n]
	arr4 = arr[n*3:]
	print(str(len(arr)))
	print(str(len(arr1)))
	print(str(len(arr2)))
	print(str(len(arr3)))
	print(str(len(arr4)))
	thread1 = threading.Thread(target=load_part, args=arr1)
	thread2 = threading.Thread(target=load_part, args=arr2)
	thread3 = threading.Thread(target=load_part, args=arr3)
	thread4 = threading.Thread(target=load_part, args=arr4)
	thread1.start()
	thread2.start()
	thread3.start()
	thread4.start()
	thread1.join()
	thread2.join()
	thread3.join()
	thread4.join()
	

csv = csv_util.CSV()
try:
	csv.open("rsslist.csv")
except:
	open("rsslist.csv","w+")
print(str(csv.data)+"\n\nLength : "+str(len(csv.data)))
var = input("Press a key")
start = time.time()
load_rss_list(csv.data)
elapsed = time.time() - start
print(time.strftime("%H:%M:%S", time.gmtime(elapsed)))

