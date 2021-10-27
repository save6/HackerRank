# Enter your code here. Read input from STDIN. Print output to STDOUT
x,k = map ( int , input().split())
s = input()
if eval(s) == k:
    print("True")
else :
    print("False")
