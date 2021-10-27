import numpy

N = int(input())

arr1 = numpy.array([input().split() for _ in range(N)],int)
arr2 = numpy.array([input().split() for _ in range(N)],int)

print(numpy.dot(arr1, arr2))

