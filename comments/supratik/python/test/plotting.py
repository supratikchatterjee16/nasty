import matplotlib.pyplot as plot

def plot_line(arr):
	x =[i for i in range(0,len(arr)*2,2)]
	y = arr
	plot.plot(x, y)
	plot.title('Result plot')
	plot.show()

def plot_bar(arr):
	x = range(len(arr))
	y = arr
	plot.bar(x,y,width=0.2,color=['blue','green'])
	plot.title('Result')
	plot.show()

plot_bar([5,4,9,100,5])
