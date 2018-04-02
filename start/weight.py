import math

def g2kg(weight):
	return float(weight / 1000)
# test the 'g2kg' function
g = 1400
print(g2kg(g))

def getMaxEdgeOfTriangle(a, b):
	print('The right triangle third side\'s length is ' + str(math.sqrt(a * a + b * b)))

getMaxEdgeOfTriangle(3, 4)