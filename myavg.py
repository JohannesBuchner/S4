
import numpy
import sys

print(sys.argv)

filename = sys.argv[1]

data = numpy.loadtxt(filename)

mu = data.mean()
s = data.std()

print(mu, s)

numpy.savetxt("%s_mean.txt" % filename, [mu, s])



