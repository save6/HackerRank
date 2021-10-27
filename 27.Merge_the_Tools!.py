def merge_the_tools(string, k):
    t = []
    u = [""]*int(len(string)/k)
    
    for i in range(0,len(string),k):
        t.append(string[i:i+k])
    
    for i in range(len(t)):
        for j in range(len(t[i])):
            if t[i][j:j+1] not in u[i]:
                u[i] = u[i] + t[i][j:j+1]
            
    for s in u:
        print(s)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)