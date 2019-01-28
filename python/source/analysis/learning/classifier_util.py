import re
import csv

classifiers = ['political','technical','opinion','sports','market','crime','art','business']
def classify_word(word, classification):
	lst = []
	if classification not in classifiers:
		raise ValueError('The classification was not found. Possible classifiers : ',classifiers)
	try:
		with open(classification+'.csv', 'r') as csvfile:
			csvr = csv.reader(csvfile)
			for row in csvr:
				lst += row
	except FileNotFoundError:
		open(classification+'.csv','w+')
	except AttributeError:
		pass
	if word not in lst:
		with open(classification+'.csv','a') as csvfile:
			csvfile.write(word+',')

def classify_text(text, classification):
	for word in text:
		classify_word(word, classification)

def classify_set(arr, classification):
	for word in arr:
		classify_word(word, classification)
		
print("imported classifer_util succesfully")
