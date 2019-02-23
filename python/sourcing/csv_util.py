import csv

class CSV:
	def __init__(self, **kwargs):
		self.data = []
		if "filename" in kwargs.keys():
			self.filename = kwargs.get("filename")
			try:
				with open(self.filename, "r") as csvfile:
					reader = csv.reader(csvfile)
					for row in reader:
						self.data += row
			except:
				if "create" in kwargs.keys():
					if kwargs.get("create"):
						csvfile = open(self.filename,"w+")
				else:	
					raise FileNotFoundError("File not found")

	def open(self, filename):
		self.filename = filename
		self.data = []
		try:
			with open(filename, "r") as csvfile:
				reader = csv.reader(csvfile)
				for row in reader:
					self.data += row
		except:
			raise FileNotFoundError("File not found")

	def add(self, content):
		self.data.append(content)
	
	def add_list(self, ls):
		self.data += ls
	def write_out(self):
		with open(self.filename, "w+") as csvfile:
			writer = csv.writer(csvfile)
			writer.writerow(self.data)

print("Imported csv_util module")
