# Enter your code here. Read input from STDIN. Print output to STDOUT

palindromic = {1,2,3,4,5,6,7,8,9,11,22,33,44,55,66,77,88,99}
_ , nums = input(), list(map(int,input().split()))

if all((n > 0) for n in nums) and any([(n in palindromic) for n in nums]):
    print("True")

else:
    print("False")
