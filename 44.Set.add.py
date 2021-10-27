# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__=='__main__':
    country = set()
    for _ in range(int(input())):
        country.add(input())
    
    print(len(country))
