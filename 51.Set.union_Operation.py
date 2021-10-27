# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())
english = set(input().split())
s = int(input())
french = set(input().split())

print(len(english | french))
