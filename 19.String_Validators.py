if __name__ == '__main__':
    s = input()
    
    check = [False,False,False,False,False]
    
    for i in range(len(s)):
        if s[i].isalnum():
            check[0] = True
        if s[i].isalpha():
            check[1] = True
        if s[i].isdigit():
            check[2] = True
        if s[i].islower():
            check[3] = True
        if s[i].isupper():
            check[4] = True
    
    for c in check:
        print(c)
