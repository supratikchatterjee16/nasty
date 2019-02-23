import csv_util
import rss_util
import webpage_util
import sentence_util
import sys

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
	
	rsslist = rsslist.data
	rsslist_updates = rsslist_updates.data
	links = links.data
	link_updates = link_updates.data
	print(rsslist)
	print(rsslist_updates)
	print(links)
	print(link_updates)

def mainprocess():
	global rsslist
	for source in rsslist:
		rss = rss_util.RSS(url = source)
		try:
			print(rss.url + " "+rss.feed["updated"])
		except Exception as e:
			print(source + " " +str(rss.valid))


try:
	init()
	mainprocess()
	sys.exit(0)
except Exception as e:
	print("System error : ")
	print(e)
	sys.exit(1)