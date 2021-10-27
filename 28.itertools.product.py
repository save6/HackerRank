# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product

if __name__=='__main__':
    A = map(int, input().split())
    B = map(int, input().split())
    
    result = ""
    for t in list(product(A,B)):
        result += str(t) + " "
    
    print(result)
