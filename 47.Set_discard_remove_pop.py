n = int(input())
s = set(map(int, input().split()))

for _ in range(int(input())):
    data = input().split()
    
    if data[0] == "pop":
        try:
            s.pop()
        except Exception:
            pass
    elif data[0] == "remove":
        try:
            s.remove(int(data[1]))
        except Exception:
            pass
    elif data[0] == "discard":
        s.discard(int(data[1]))

print(sum(s))
