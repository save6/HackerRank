# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque

for _ in range(int(input())):
    n = int(input())
    blocks = deque(map(int, input().split()))
    c = 0
    top = 2**31
    result = "Yes"
    
    while c < n:
        
        left = blocks.popleft()
        c += 1
        
        if c < n:
            right = blocks.pop()
            c += 1
        else:
            right = 0
        
        if left >= right:
            if top >= left:
                top = left
            else:
                result = "No"
                break;
        else:
            if top >= right:
                top = right
            else:
                result = "No"
                break;
    
    print(result)    
        
        

