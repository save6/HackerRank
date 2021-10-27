# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict

if __name__=='__main__':
    N = int(input())
    items = OrderedDict()
    for i in range(N):
        item_list = input().split()
        key = " ".join(item_list[0:len(item_list)-1])
        if key in items:
            items[key] += int(item_list[len(item_list)-1])
        else:
            items[key] = int(item_list[len(item_list)-1])
    
    for k, v in items.items():
        print(k + " " + str(v))
