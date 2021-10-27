# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

S = input().strip()
k = input().strip()

pattern = re.compile(k)
m = pattern.search(S)

if not m:
    print("(-1, -1)")

while m:
    print("({0}, {1})".format(m.start(),m.end()-1))
    m = pattern.search(S,m.start() + 1)
