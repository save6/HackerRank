# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

p = r'(?<=[qwrtypsdfghjklzxcvbnm])([aeiou]{2,})[qwrtypsdfghjklzxcvbnm]'

m = re.findall(p,input(),flags=re.I)

if m:
    print(*[n for n in m],sep="\n")
else:
    print("-1")
