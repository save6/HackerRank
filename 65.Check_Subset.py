# Enter your code here. Read input from STDIN. Print output to STDOUT

for _ in range(int(input())):
    _,setA = input(), set(input().split())
    _,setB = input(), set(input().split())
    
    print(setA <= setB)
