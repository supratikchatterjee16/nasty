import nltk
import csv

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

def remove_abbreviations(string):
	abbreviation = []
	change = []
	res = ""
	with open("abbreviations.csv") as csvfile:
		reader = csv.reader(csvfile)
		ctr = 0
		for row in reader:
			abbreviation.append(row[0].strip())
			change.append(row[1].strip())
	for word in string.split():
		if word in abbreviation:
			res+=change[abbreviation.index(word)]
		else:
			if word[-1:] == ".":
				full = raw_input("Enter the full form. (NA if it doesn't exist)")
				#if full == "NA"
			res+=word
		res+=" "
	return res

def rm_tags(string, tags, **args):
	res = []
	tagged = get_tagged_tokens(string)
	for dual in tagged:
		if dual[1] not in tags or dual[0] in args["exception"]:
			res.append(dual)
	return res

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

text = "The color of animals is by no means a matter of chance; it depends on many considerations, but in the majority of cases tends to protect the animal from danger by rendering it less conspicuous. Perhaps it may be said that if coloring is mainly protective, there ought to be but few brightly colored animals. There are, however, not a few cases in which vivid colors are themselves protective. The kingfisher itself, though so brightly colored, is by no means easy to see. The blue harmonizes with the water, and the bird as it darts along the stream looks almost like a flash of sunlight. Desert animals are generally the color of the desert. Thus, for instance, the lion, the antelope, and the wild donkey are all sand-colored. The next point is the color of the mature caterpillars, some of which are brown. This probably makes the caterpillar even more conspicuous among the green leaves than would otherwise be the case. Let us see, then, whether the habits of the insect will throw any light upon the riddle. What would you do if you were a big caterpillar? Why, like most other defenseless creatures, you would feed by night, and lie concealed by day. So do these caterpillars. When the morning light comes, they creep down the stem of the food plant, and lie concealed among the thick herbage and dry sticks and leaves, near the ground, and it is obvious that under such circumstances the brown color really becomes a protection. It might indeed be argued that the caterpillars, having become brown, concealed themselves on the ground, and that we were reversing the state of things. But this is not so, because, while we may say as a general rule that large caterpillars feed by night and lie concealed by day, it is by no means always the case that they are brown; some of them still retaining the green color. We may then conclude that the habit of concealing themselves by day came first, and that the brown color is a later adaptation."

print(sentence_tokenize(text))
