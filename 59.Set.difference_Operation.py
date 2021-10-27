# Enter your code here. Read input from STDIN. Print output to STDOUT

E,english = int(input()),set(input().split())
F,french = int(input()),set(input().split())

print(len(english - french))
