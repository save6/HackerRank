def make_rangoli_row(alpha_index,row_index):
    alpha = []
    counter = 0
    for i in range(0,row_index * 2 + 1):
        alpha.append(chr(97 + alpha_index - counter))
        
        if i < row_index:
            counter+=1
        else :
            counter-=1
    
    return "-".join(alpha)    

def print_rangoli(size):
    
    width = size + (size -1) + (size * 2 - 2)
    
    for h in range(size):
        print(make_rangoli_row(size -1,h).center(width,"-"))
    
    for h in range(size-1)[::-1]:
        print(make_rangoli_row(size -1,h).center(width,"-"))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)