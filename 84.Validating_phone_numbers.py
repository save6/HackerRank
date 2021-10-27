# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

for _ in range(int(input())):
    
    if re.match(r'[789][0-9]{9}$',input().strip()):
        print("YES")
    else:
        print("NO")
        
