# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import namedtuple

if __name__=='__main__':
    N = int(input())
    Student = namedtuple('Student',input().split())
    sum = 0
    for i in range(N):
        a = input().split()
        sum += int(Student(a[0],a[1],a[2],a[3]).MARKS)
    
    print(f'{sum/N:.2f}')
