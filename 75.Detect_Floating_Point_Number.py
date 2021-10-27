# Enter your code here. Read input from STDIN. Print output to STDOUT

for _ in range(int(input())):
    n = input()
    try:
        int(n.split('.')[1])
        n = float(n)
        print("True")
    except:
        print("False")
