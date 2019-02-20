import nltk
import matplotlib.pyplot as plotter
import numpy

nltk_identifiers = ['CC', 'CD', 'DT', 'EX', 'FW', 'IN', 'JJ', 'JJR', 'JJS', 'LS', 'MD', 'NN', 'NNS', 'NNP', 'NNPS', 'PDT', 'POS', 'PRP', 'PRP$', 'RB', 'RBR', 'RBS', 'RP', 'TO', 'UH', 'VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ', 'WDT', 'WP', 'WP$', 'WRB']

def sentence_tokenize(text):
	punctuation = ['?','!','.',',',';',':','"']
	res = []
	temp = ""
	#types are INTE, EXCL, IMPR, DECL
	#others are speech(SPCH), part(PART)
	#DK is don't know
	types = {
		'?' : 'INTE',
		'!' : 'EXCL',
		',' : 'PART',
		';' : 'PART',
		':' : 'PART',
		'"' : 'SPCH',
		'.' : 'DK'
		}
	last_is_punctuation = False
	for i in text:
		if i in punctuation and not last_is_punctuation:
			last_is_punctuation = True
			res.append((temp, types[i]))
			temp = ""
		else:
			last_is_punctuation = False
			temp += i
	return res

def analyze(string):
	mat =[[0 for x in range(len(nltk_identifiers))] for y in range(len(nltk_identifiers))]
	sentences = [i[0].strip("\n \r") for i in sentence_tokenize(string)]
	cases = len(sentences)
	for sentence in sentences:
		pos_tags = [i[1] for i in nltk.pos_tag(nltk.word_tokenize(sentence))]
		for i in range(len(pos_tags)-1):
			mat[nltk_identifiers.index(pos_tags[i])][nltk_identifiers.index(pos_tags[i+1])] += 1
	print("Number of cases : "+str(cases))
	for i in range(len(nltk_identifiers)):
		for j in range(len(nltk_identifiers)):
			if mat[i][j] > (cases/4)-(cases/16) :
				print(nltk_identifiers[i]+"->"+nltk_identifiers[j]+" "+str(mat[i][j]))
	
	plot = plotter.imshow(mat)
	plotter.colorbar()
	plotter.show()

with open("assertive.txt","r") as textfile:
	analyze(textfile.read())

with open("declarative.txt","r") as textfile:
	analyze(textfile.read())
