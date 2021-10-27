# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

if __name__=='__main__':
    
    for _ in range(int(input())):
        try:
            p = re.compile(r"" + input())
            print("True")
        except re.error:
            print("False")
