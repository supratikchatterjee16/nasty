import os
import datetime

print("1 for declarative\n2 for assertive\n3 for neither/ignore\n\nEntering nothing ignores\nEntering an alphabet causes program termination\n\n\n")

now = datetime.datetime.now()
date = now.strftime("%Y-%m-%d")
with open("assertive"+date+".dat","w+") as datfile:
	pass
with open("declarative"+date+".dat","w+") as datfile:
	pass

def sentence_tokenize(text):
	punctuation = ['?','!','.',';',':','"']
	res = []
	temp = ""
	#types are INTE, EXCL, IMPR, DECL
	#others are speech(SPCH), part(PART)
	#DK is don't know
	types = {
		'?' : 'INTE',
		'!' : 'EXCL',
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

stats = [0,0,0]
print(">>Opening raw.dat")
rawfile = open("raw.dat","r")
sentences = rawfile.readlines()
opt = 0
for sentence in sentences:
	tagged = sentence_tokenize(sentence)
	for temp in tagged:
		if temp[1] == "DK":
			print(">>"+temp[0])
			opt = input(">>")
			try:
				opt = int(opt)
			except:
				if opt == '':
					opt = 3
				else:
					exit()
			if opt == 1:
				datfile = open("declarative"+date+".dat","a+")
				datfile.write(temp[0]+"\n")
				datfile.flush()
				datfile.close()
				stats[0]+=1
			elif opt == 2:
				datfile = open("assertive"+date+".dat","a+")
				datfile.write(temp[0]+"\n")
				datfile.flush()
				datfile.close()
				stats[1]+=1
			else:
				stats[2] += 1
		else:
			print(">>"+temp[0])
			print("\nAutomatically ignored\n")
			stats[2]+=1
		if opt == 3:
			break
print("---------------- Completed ----------------")
print("Total sentences\t:\t"+str(stats[0]+stats[1]+stats[2]))
print("Assertive sentences\t:\t"+str(stats[0]))
print("Declarative sentences\t:\t"+str(stats[1]))
print("Ignored sentences\t:\t"+str(stats[2]))
