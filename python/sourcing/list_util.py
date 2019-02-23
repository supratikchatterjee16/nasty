import csv

def remove_duplicates(ls):
	return list(set(ls))

#def create_csv(name, ls):
	#with open(name, "w+") as csvfile:
		#writer = csv.writer(csvfile)
		#writer.write(ls)