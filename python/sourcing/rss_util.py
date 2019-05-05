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
			self.items = rss["entries"]
			self.valid = False
			if len(rss["items"]) != 0:
				self.valid = True
		except Exception as e:
			print(url+" "+e)

rss ="http://feeds.bbci.co.uk/news/world/europe/rss.xml"
print("rss_util imported")