# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

if __name__=='__main__':
    AB = int(input())
    BC = int(input())
    
    print(str(int(round(math.degrees(math.atan2(AB,BC)))))+b'\\u00B0'.decode('unicode-escape'))
