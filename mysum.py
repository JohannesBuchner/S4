import numpy

def mysum_lists(a, b):
	i = 0
	out = []
	
	while i < len(a):
		out.append( a[i] * b[i] )
		i += 1
	
	return out

def mysum_numpyalloc(a, b):
	i = 0
	out = numpy.zeros_like(a)
	
	while i < len(a):
		out[i] = a[i] * b[i]
		i += 1
	
	return out

def mysum_numpy(a, b):
	out = numpy.product(a, b)
	return out


a = numpy.random.normal(size=100000)
b = numpy.random.normal(size=100000)

#print(mysum(a,b))


