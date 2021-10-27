import numpy

n,m = map(int,input().split())
a = [input().split() for _ in range(n)]
b = [input().split() for _ in range(n)]

a = numpy.array(a, int)
b = numpy.array(b, int)

print(numpy.add(a, b))
print(numpy.subtract(a, b))
print(numpy.multiply(a, b))
print(numpy.floor_divide(a, b))
print(numpy.mod(a, b))
print(numpy.power(a, b))
