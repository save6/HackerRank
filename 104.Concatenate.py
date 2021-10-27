import numpy

n,m,p = input().split()

array1 = numpy.array([input().split() for _ in range(int(n))],int)
array2 = numpy.array([input().split() for _ in range(int(m))],int)

print(numpy.concatenate((array1, array2)))

