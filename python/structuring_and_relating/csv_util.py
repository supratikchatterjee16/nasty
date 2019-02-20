import csv

class CSV:
	filename = ""
	data = []
	def open(self, filename):
		self.filename = filename
		try:
			with open(filename, "r") as csvfile:
				reader = csv.reader(csvfile)
				for row in reader:
					self.data += row
		except:
			raise FileNotFoundError("File not found")
	
#	def open(self, filename, create):
#		if create is True:
#			try:
#				with open(filename, "r") as csvfile:
#					reader = csv.reader(csvfile)
#					for row in reader:
#						self.data += row
#			except:
#				open(filename, "w+")
#		else:
#			try:
#				with open(filename, "r") as csvfile:
#					reader = csv.reader(csvfile)
#					for row in reader:
#						self.data += row
#			except:
#				pass
	
	def add(self, content):
		with open(filename, "a") as csvfile:
			csvfile.write(","+content)
	
	def add_row(self, filename, content):
		with open(filename, "a") as csvfile:
			for element in content:
				csvfile.write(","+element)
			csvfile.write("\n")
	
	def write_out(self):
		with open(self.filename, "w+") as csvfile:
			csvfile.write(self.data)
			
print("Imported csv_util module")
