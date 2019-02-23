import requests
from bs4 import BeautifulSoup as bs
import re
def get_article(url):
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

def get_links(url):
	page = requests.get(url)
	soup = bs(page.content, 'html.parser')
	links = soup.find_all('a')
	arr = []
	for element in links:
		arr.append(element.get('href'))
	return arr

def select_links(url, pattern):
	links = get_links(url)
	arr = []
	for element in links:
		if isinstance(element, str) and re.search(pattern, url):
			arr.append(element)
	return arr

print("imported webpage_util succesfully")
