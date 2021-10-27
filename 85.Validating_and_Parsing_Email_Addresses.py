# Enter your code here. Read input from STDIN. Print output to STDOUT
import email.utils
import re

for _ in range(int(input())):
    S = input()
    _,e = email.utils.parseaddr(S)
    if re.match(r'[a-zA-Z][\w\._-]+@[a-zA-Z]+\.[a-zA-Z]{1,3}$',e):
        print(S)
