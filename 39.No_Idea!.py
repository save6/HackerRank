# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__=='__main__':
    _ = input()
    answer = list(input().split())
    list_A = set(input().split())
    list_B = set(input().split())
    happiness = 0
    for a in answer:
        if a in list_A:
            happiness += 1
        if a in list_B:
            happiness -= 1
    print(happiness)
