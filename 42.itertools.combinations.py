# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations

if __name__=='__main__':
    S,k = input().split()
    
    for i in range(1,int(k)+1):
        for t in combinations(sorted(S),i):
            print("".join(t))
