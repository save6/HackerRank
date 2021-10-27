# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

for _ in range(int(input())):
    S = input()
    tmp = re.sub(r'(?<=\s)&&(?=\s)',"and",S)
    print(re.sub(r'(?<=\s)\|\|(?=\s)','or',tmp))
