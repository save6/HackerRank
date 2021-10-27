# Enter your code here. Read input from STDIN. Print output to STDOUT
n,english = int(input()), set(input().split())
b,french = int(input()),set(input().split())

print(len(english & french))
