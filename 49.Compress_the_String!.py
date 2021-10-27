# Enter your code here. Read input from STDIN. Print output to STDOUT
import itertools

if __name__=='__main__':
    print(*[(len(list(g)),int(k)) for k, g in itertools.groupby(input())])
        
