import feedparser

class RSS:
	titles = []
	links = []
	dates = []
	count = 0
	def open(self, url):
		feed = feedparser.parse(url)
		for element in feed['entries']:
			try:
				self.dates.append(element['published'])
				self.titles.append(element['title'])
				self.links.append(element['link'])
				self.count+=1
			except:
				pass


print("Imported rss_util module")
#Test code :
#r = RSS()
#r.open("http://rss.cnn.com/rss/edition_world.rss")
#r.open("https://www.aljazeera.com/xml/rss/all.xml")

#print(r.count)
#print(*r.titles, sep='\n')
