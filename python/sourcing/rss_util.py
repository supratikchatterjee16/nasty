import requests
import feedparser
import re

class RSS():
	def __init__(self, url):
		try:
			page = requests.get(url)
			content = page.content
			rss = feedparser.parse(content)
			#print(rss.keys())
			#for entries in rss["entries"]:
				#print("item" + str(entries))
			self.url = url
			self.feed = rss["feed"]
			self.items = rss["entries"]
			self.valid = False
			if len(rss["items"]) != 0:
				self.valid = True
		except Exception as e:
			print(url+" "+e)

#import csv_util
#import list_util
#sources = csv_util.CSV(filename = "rsslist.csv")
#sources = list_util.remove_duplicates(sources.data)
#sources.sort()
#for source in sources:
	#rss = RSS(source)
	#try:
		#print(rss.url+" : "+rss.feed.get("updated"))
	#except:
		#print("Could not be fetched")

rss ="http://feeds.bbci.co.uk/news/world/europe/rss.xml"
print("rss_util imported")

#page = requests.get(rss)
#content = feedparser.parse(page.content)
#for element in content["items"]:
	#print(element)