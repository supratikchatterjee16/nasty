import nltk
def extract_nouns(string):
	arr = [word for (word, pos) in nltk.pos_tag(nltk.word_tokenize(string)) if pos[0] == 'N']
	return arr

def extract_verbs(string):
	arr = [word for (word, pos) in nltk.pos_tag(nltk.word_tokenize(string)) if pos[0] == 'V']
	return arr

def extract_interesting(string):
	arr = [word for (word, pos) in nltk.pos_tag(nltk.word_tokenize(string)) if pos[0] == 'V' or pos[0] == 'N']
	return arr

