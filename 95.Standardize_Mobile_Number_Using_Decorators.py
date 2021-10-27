def wrapper(f):
    def fun(l):
        result = []
        for i in l:
            tmp = ""
            if len(i) == 12 :
                tmp = "+" + i[0:2] + " " + i[2:7] + " " + i[7:12]
            elif len(i) == 11:
                tmp = "+91" + " " + i[1:6] + " " + i[6:11]
            elif len(i) == 10:
                tmp = "+91" + " " + i[0:5] + " " + i[5:10]
            elif len(i) == 13:
                tmp = i[0:3] + " " + i[3:8] + " " + i[8:13]
            result.append(tmp)
        f(result)
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 


