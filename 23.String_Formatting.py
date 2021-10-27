def print_formatted(number):
    space = len(bin(number)[2:]) + 1
    
    for i in range(1, number+1):
        print(str(i).rjust(space - 1) + '{:o}'.format(i).rjust(space) + '{:X}'.format(i).rjust(space)+ '{:b}'.format(i).rjust(space))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)