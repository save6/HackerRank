# Enter your code here. Read input from STDIN. Print output to STDOUT
import calendar

if __name__=='__main__':
    month, day, year = map(int, input().split())
    date = {0:"MONDAY",1:"TUESDAY",2:"WEDNESDAY",3:"THURSDAY",4:"FRIDAY",5:"SATURDAY",6:"SUNDAY"}
    print(date[calendar.weekday(year,month,day)])
