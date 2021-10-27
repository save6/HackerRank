# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque

if __name__=='__main__':
    d = deque()
    for _ in range(int(input())):
        command, *args = input().split()
        getattr(d, command)(*(int(x) for x in args))
    
    print(*d)
    
