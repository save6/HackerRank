def count_substring(string, sub_string):
    c = 0
    counter = 0
    for i in range(0, len(string)):
        c = i
        for j in range(0, len(sub_string)):
            if string[c] == sub_string[j]:
                if c + 1 < len(string):
                    c += 1
                if j == len(sub_string) - 1:
                    counter += 1
            else :
                break
       
    return counter

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)