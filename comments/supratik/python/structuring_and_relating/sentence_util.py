import nltk
def extract_nouns(string):
	arr = [word for (word, pos) in nltk.pos_tag(nltk.word_tokenize(string)) if pos[0] == 'N']
	return arr

def extract_verbs(string):
	arr = [word for (word, pos) in nltk.pos_tag(nltk.word_tokenize(string)) if pos[0] == 'V']
	return arr

def extract_nouns_proper(string):
	arr = [word for (word, pos) in nltk.pos_tag(nltk.word_tokenize(string)) if pos == 'NNP']
	return arr

def extract_nouns_improper(string):
	arr = [word for (word, pos) in nltk.pos_tag(nltk.word_tokenize(string)) if pos != 'NNP' and pos[0] == 'N']
	return arr

def get_tokens(string):
	return nltk.word_tokenize(string)

def get_tagged_tokens(string):
	return nltk.pos_tag(nltk.word_tokenize(string))

def cleanse_pos_tags(string, *arr):
	tagged = get_tagged_tokens(string)
	text = ""
	for tuples in tagged:
		if tuples[1] not in arr:
			text += tuples[0]+" "
	return text

def extract_names(string):
	if  not string.endswith("."): string += "."
	tokens = get_tagged_tokens(string)
	name = ""
	ctr = 0
	arr = []
	for word in tokens:
		if word[1] == 'NNP':
			name += word[0]+" "
			ctr += 1
		else:
			if ctr > 1:
				name = name.strip()
				arr.append(name)
			ctr = 0
			name = ""
	return arr

def extract_relations(string):
	names = extract_names(string)
	mod_text = string
	ctr = 0
	for name in names:
		mod_text = mod_text.replace(name, "U"+str(ctr))
		ctr += 1
	
	res = get_tagged_tokens(mod_text)
	print(res)
	
	
print("Imported sentence_util succesfully")
