# Enter your code here. Read input from STDIN. Print output to STDOUT

S = sorted(input())
upper = list()
lower = list()
odd = list()
even = list()

for s in S:
    if s.isupper():
        upper.append(s)
    elif s.islower():
        lower.append(s)
    elif s.isdecimal() and int(s) % 2 == 0:
        even.append(s)
    elif s.isdecimal() and int(s) % 2 == 1:
        odd.append(s)

print(*lower,*upper,*odd,*even,sep="")
