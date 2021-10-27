# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

cssList = list()

for _ in range(int(input())):
    cssList.append(input())

css = "".join(cssList)

result = re.findall(r'(#[0-9a-fA-F]{3}(?=[;,)]))|(#[0-9a-fA-F]{6}(?=[;,)]))',css)

for r in result:
    if r[0] != "":
        print(r[0])
    if r[1] != "":
        print(r[1])
