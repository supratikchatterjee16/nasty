import requests
import feedparser
import re

class RSS():
	def __init__(self, url):
		try:
			page = requests.get(url)
			content = page.content
			rss = feedparser.parse(content)
			self.url = url
			self.feed = rss["feed"]
			self.items = rss["items"]
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
		
print("rss_util imported")