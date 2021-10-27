# Enter your code here. Read input from STDIN. Print output to STDOUT

def fx(list, m):
    return sum([pow(i,2) for i in list]) % m

from itertools import product

K,M = map(int, input().split())
N = [list(map(int,input().split()))[1:] for _ in range(K)]

print(max([fx(p,M) for p in product(*N)]))
