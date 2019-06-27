
import numpy
import sys

print(sys.argv)

i = int(sys.argv[1])
j = int(sys.argv[2])

a = numpy.random.normal(size=i * j)

print("output_%d_%d.txt" % (i, j))
print("output_{}_{}.txt".format(i, j))

info = {
	"firstvalue": i,
	"secondvalue": j,
}
print(info)

#print("output_%(firstvalue)d_%(secondvalue)d_%(firstvalue).5f.txt" % info)

numpy.savetxt("output_%d_%d.txt" % (i, j), a)



