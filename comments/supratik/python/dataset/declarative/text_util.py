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
