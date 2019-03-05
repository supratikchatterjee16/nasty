import rss_util
import csv_util
import list_util

rsslist = csv_util.CSV(filename = "rsslist.csv")
rsslist.data = list_util.remove_duplicates(rsslist.data)
valid = []
no_dates = []
invalid = []

for source in rsslist.data:
		try:
			rss = rss_util.RSS(url = source)
			try:
				print(rss.url + " "+rss.feed["updated"])
				valid.append(source)
			except Exception as e:
				print(source + " " +str(rss.valid))
				if rss.valid:
					no_dates.append(source)
				else:
					invalid.append(source)
		except Exception as e:
			print("Connection refused")
				
print(valid)
print(no_dates)
print(invalid)

rsslist.data = valid + no_dates
rsslist.write_out()