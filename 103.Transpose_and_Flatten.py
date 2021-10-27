import numpy

n,m = input().split()
array = []

for _ in range(int(n)):
    array.append(input().split())
    
my_array = numpy.array(array,int)

print(numpy.transpose(my_array))
print(my_array.flatten())
    

