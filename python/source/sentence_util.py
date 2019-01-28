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

def extract_nouns_proper(string):
	arr = [word for (word, pos) in nltk.pos_tag(nltk.word_tokenize(string)) if pos == 'NNP']
	return arr

def extract_nouns_improper(string):
	arr = [word for (word, pos) in nltk.pos_tag(nltk.word_tokenize(string)) if pos != 'NNP' and pos[0] == 'N']
	return arr
	
print("imported sentence_util succesfully")
