import numpy

def mysum_lists(a, b):
	out = []
	
	ashape = a.shape
	bshape = b.shape
	assert ashape[1] == bshape[0], (ashape, bshape)
	out = numpy.zeros((ashape[0], bshape[1]))
	
	for i in range(ashape[0]):
		for k in range(bshape[1]):
			rowsum = 0
			for j in range(bshape[0]):
				rowsum += a[i,j] * b[j,k]
			out[i,k] = rowsum
			
	return out

def mysum_reshaped(a, b):
	ashape = a.shape
	bshape = b.shape
	A = a.reshape((ashape[0], ashape[1], 1))
	B = b.reshape((1, bshape[0], bshape[1]))
	return (A * B).sum(axis=1)

def mysum_numpy(a, b):
	out = numpy.dot(a, b)
	return out


def mysum_einsum(a, b):
	out = numpy.einsum('ij,jk->ik', a, b)
	return out



a = numpy.random.normal(size=(1000,200))
b = numpy.random.normal(size=(200,3000))

#print(mysum(a,b))


