"""
Johannes Buchner (C) 2019

Student session
"""


import numpy
import sys

def myavg_compute(filename):
	"""
	This computes a linear regression of 2d data in filename
	
	returns mean and std
	"""
	print("dealing with filename '%s' ..." % filename)
	
	data = numpy.loadtxt(filename)

	mu = data.mean()
	s = data.std()

	print(mu, s)

	numpy.savetxt("%s_mean.txt" % filename, [mu, s])
	return mu, s

print("__name__ is : ", __name__)

if __name__ == '__main__':

	print(sys.argv)

	filenames = sys.argv[1:]


	from joblib import Parallel, delayed

	Parallel(n_jobs=-1)([delayed(myavg_compute)(filename) for filename in filenames])




