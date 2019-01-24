import requests
from bs4 import BeautifulSoup as bs
import re
def get_sentences(url):
	page = requests.get(url)
	soup = bs(page.content, 'html.parser')
	pat = re.compile(r'^[A-Z]+.*[.!?]$', re.M)
	temp_list = []
	for text in soup.body.stripped_strings:
		arr = pat.findall(text)
		if len(arr) != 0:
			temp_list = temp_list + arr
	return temp_list

def get_content(url):
	page = requests.get(url)
	return page.content

def get(url):
	return get_content(url);

