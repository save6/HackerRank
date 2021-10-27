# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter

if __name__ == '__main__':
    N = int(input())
    shoeSize = list(map(int, input().split()))
    shoeSize = Counter(shoeSize)
    customers = []
    earned = 0
    
    while 1:
        try:
            val = list(map(int,input().split()))
            if len(val) > 1:
                customers.append(val)
        except EOFError:
            break
    
    for size, price in customers:
        if size in shoeSize and shoeSize[size] != 0:
            earned += price
            shoeSize[size] -= 1
    
    print(earned)
