import importlib
feedparser = importlib.
class RSS:
	feed
	def __init__(self, url):
		feed = feedparser.parse('http://feedparser.org/docs/examples/atom10.xml')
	
	def get_title():
		return feed['feed']['title']
		
rss = RSS('http://feeds.bbci.co.uk/news/world/rss.xml')
print(rss.get_title())
