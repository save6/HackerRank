# Enter your code here. Read input from STDIN. Print output to STDOUT

def getString(num):
    result = ""
    c = ".|."
    for i in range(num):
        result = result + c
    return result

tmp = input().split()
n,m = int(tmp[0]),int(tmp[1])
c = "WELCOME"

for i in range(0, int((n-1)/2)):
    print(getString(2*i+1).center(m,'-'))

print(c.center(m,'-'))

for i in range(int((n-1)/2), 0, -1):
    print(getString(2*(i-1)+1).center(m,'-'))
