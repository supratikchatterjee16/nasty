import importlib


#The following is the test code for webpage_util.py to test the sentence extraction unit
#webman = importlib.import_module("webpages_util")

#print("\n\nThe following are excerpts from the TOI websites : \n\n")
#for element in webman.get_sentences("https://timesofindia.indiatimes.com/india/n-chandrababu-naidu-indicates-tdp-will-go-it-alone-in-ap-polls/articleshow/67674483.cms"):
#	print(element)

#print("\n\nThe following are excerpts from the NDTV websites : \n\n")

#for element in webman.get_sentences("https://www.ndtv.com/world-news/amid-shutdown-donald-trump-daughter-in-law-lara-trump-calls-missed-paychecks-sacrifices-1982732"):
#	print(element)

#print("\n\nThe following are excerpts from the BBC websites : \n\n")

#for element in webman.get_sentences("https://www.bbc.com/news/world-us-canada-46983349"):
#	print(element)




#The following is the test code for sentence_util.py to test the words extraction unit
#webman = importlib.import_module("webpage_util")
#sentence = importlib.import_module("sentence_util")
#array = []
#for element in webman.get_sentences("https://www.bbc.com/news/world-latin-america-46997555"):
#	print(element)
#	array += sentence.extract_nouns(element)
#print(array)



#The following is the test code for webpages_util.py to fetch all links from the url passed
#webman = importlib.import_module("webpage_util")
#links = webman.get_links('https://timesofindia.indiatimes.com/rss.cms')
#arr = []
#for element in links:
#	if isinstance(element, str) and "timesofindia" in element:
#		arr.append(element)
#print(arr)
#arr = webman.select_links('https://timesofindia.indiatimes.com/rss.cms', 'http://timesofindia.indiatimes.com/rssfeeds/.+\bcms\b$')
#for element in arr:
#	print(element)


#webutil = importlib.import_module("webpage_util")
#textutil = importlib.import_module("sentence_util")
#learnutil = importlib.import_module("./stats/learning/classifier_util.py")
#from stats.learning import classifier_util as learnutil
import webpage_util as webutil
import sentence_util as textutil
import analysis.learning as learnutil
arr = []
for element in webutil.get_sentences("https://www.bbc.com/news/world-latin-america-46997555"):
	arr += textutil.extract_nouns_improper(element)
learnutil.classifier_util.classify_set(arr,'political')

