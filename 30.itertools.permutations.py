# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations

if __name__ == '__main__':
    S, k = input().split()

    [print("".join(p)) for p in list(permutations(sorted(S),int(k)))]
