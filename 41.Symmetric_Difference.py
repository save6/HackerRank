# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__=='__main__':
    M = int(input())
    set_m = set(map(int,input().split()))
    N = int(input())
    set_n = set(map(int,input().split()))
    
    print(*sorted((set_m - set_n) | (set_n - set_m)),sep='\n')
    
    
