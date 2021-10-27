# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict

if __name__=='__main__':
    d = defaultdict(list)
    n,m = map(int,input().split())
    
    [d[input()].append(str(i+1)) for i in range(n)]
    
    for i in range(m):
        tmp = input()
        if tmp in d:
            print(" ".join(d[tmp]))
        else:
            print("-1")
