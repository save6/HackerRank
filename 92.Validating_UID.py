# Enter your code here. Read input from STDIN. Print output to STDOUT

import re

p1 = re.compile(r'[0-9a-zA-Z]{10}$')
p2 = re.compile(r'[A-Z]')
p3 = re.compile(r'[0-9]')


for _ in range(int(input())):
    s = input()
    
    uniq_s = "".join(set(s))
    if len(uniq_s) == 10:
        if p1.match(s):
            a2 = p2.findall(s)
            if len(a2) >= 2:
                a3 = p3.findall(s)
                if len(a3) >= 3:
                    print("Valid")
                else:
                    print("Invalid")
            else:
                print("Invalid")    
        else:
            print("Invalid")
    else:
        print("Invalid")
    
