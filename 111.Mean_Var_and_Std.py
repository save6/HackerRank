import numpy

n, m = map(int,input().split())

arr = [input().split() for _ in range(n)]

my_array = numpy.array(arr,float)

mean = numpy.mean(my_array, axis = 1)
var = numpy.var(my_array,axis = 0)
std = numpy.round(numpy.std(my_array),decimals=11)

print(mean,var,std,sep="\n")
