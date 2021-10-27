# Enter your code here. Read input from STDIN. Print output to STDOUT
A = set(input().split())
B = set()
for _ in range(int(input())):
    B.update(set(input().split()))

print(A>=B)
