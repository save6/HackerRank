# Enter your code here. Read input from STDIN. Print output to STDOUT

setA,setB = [set(input().split()) for _ in range(4)][1::2]

print(len(setA ^ setB))
