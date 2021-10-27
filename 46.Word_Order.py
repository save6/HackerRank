# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict

if __name__=='__main__':
    items = OrderedDict()
    
    for i in range(int(input())):
        key = input()
        if key in items:
            items[key] += 1
        else:
            items[key] = 1
    
    print(len(items))
    print(*[v for v in items.values()])
