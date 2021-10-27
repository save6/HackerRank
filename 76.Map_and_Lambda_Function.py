cube = lambda x: pow(x,3)

def fibonacci(n):
    f = list()
    for i in range(n):
        if i == 0:
            f.append(0)
        elif i == 1:
            f.append(1)
        elif i > 1:
            f.append(f[i-1] + f[i-2])
    return f  

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))