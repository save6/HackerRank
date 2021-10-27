import numpy

n,m = map(int,input().split())

arr = [input().split() for _ in range(n)]

my_array = numpy.array(arr,int)

print(numpy.max(numpy.min(my_array, axis = 1)))
    

