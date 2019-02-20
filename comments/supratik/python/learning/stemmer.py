from pyparsing import StringEnd, oneOf, FollowedBy, Optional, ZeroOrMore, SkipTo
from csv_util import CSV

def find_root(text):
	csv1 = CSV()
	csv2 = CSV()
	csv1.open("nlp_data/prefix.csv")
	csv2.open("nlp_data/suffix.csv")
	suffix_str = ""
	prefix_str = ""
	for i in csv1.data:
		prefix_str += i + " "
	for i in csv2.data:
		suffix_str += i + " "
	endOfString = StringEnd()
	prefix = oneOf(prefix_str)
	suffix = oneOf(suffix_str) + FollowedBy(endOfString)

	word = (ZeroOrMore(prefix)("prefixes") + 
			SkipTo(suffix | endOfString)("root") + 
			Optional(suffix)("suffix"))
	res = word.parseString(text)
	return res.root

def find_roots(arr):
	res = []
	for i in arr:
		res.append(find_root(i))
	return res


def find_structure(text):
	csv1 = CSV()
	csv2 = CSV()
	csv1.open("nlp_data/prefix.csv")
	csv2.open("nlp_data/suffix.csv")
	suffix_str = ""
	prefix_str = ""
	for i in csv1.data:
		prefix_str += i + " "
	for i in csv2.data:
		suffix_str += i + " "
	endOfString = StringEnd()
	prefix = oneOf(prefix_str)
	suffix = oneOf(suffix_str) #+ FollowedBy(endOfString)

	word = (ZeroOrMore(prefix)("prefixes") + 
			SkipTo(suffix | endOfString)("root") + 
			ZeroOrMore(suffix)("suffixes"))
	res = word.parseString(text)
	return (res.prefixes, res.root, res.suffixes)

def find_structures(arr):
	res = []
	for i in arr:
		res.append(find_root(i))
	return res


print(find_structure("autobiography"))
