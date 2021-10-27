# Enter your code here. Read input from STDIN. Print output to STDOUT
N,X = map(int,input().split())
subject = list()

for _ in range(X):
    subject.append(list(map(float,input().split())))

print(*[sum(r)/X for r in zip(*subject)], sep="\n")
    
