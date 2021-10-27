# Enter your code here. Read input from STDIN. Print output to STDOU
from collections import Counter

K = int(input())
rooms = Counter(input().split())

print(rooms.most_common()[-1][0])
