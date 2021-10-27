# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations

N = int(input())
l = input().split()
K = int(input())

result = list(combinations(l, K))
print(sum([("a" in r) for r in result])/len(result))
