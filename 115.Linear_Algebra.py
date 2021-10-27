import numpy

N = int(input())
arr = [list(map(float,input().split())) for _ in range(N)]

print(round(numpy.linalg.det(arr),2)) 
