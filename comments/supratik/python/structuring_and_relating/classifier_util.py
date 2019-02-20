import re
import csv
import csv_util

classifiers = ['political','technical','opinion','sports','market','crime','art','business']
def classify_word(word, classification):
	lst = []
	csvobj = csv_util.CSV()
	if classification not in classifiers:
		raise ValueError('The classification was not found. Possible classifiers : ',classifiers)
	try:
		csvobj.open(classifier+'.csv')
		if word not in csvobj.data:
			csv.add(word)
	except FileNotFoundError:
		open(classification+'.csv','w+')
	except AttributeError:
		pass
	if word not in lst:
		with open(classification+'.csv','a') as csvfile:
			csvfile.write(word+',')

def classify_text(text, classification):
	for word in text:
		classify_word(text, classification)

def classify_set(arr, classification):
	for word in arr:
		classify_word(text, classification)
