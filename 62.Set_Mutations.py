# Enter your code here. Read input from STDIN. Print output to STDOUT

_, setA = input(),set(map(int,input().split()))

for _ in range(int(input())):
    cmd,_ = input().split()
    setB = set(map(int,input().split()))
    getattr(setA,cmd)(setB)
    
print(sum(setA))
