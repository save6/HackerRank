if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr_list = list(arr)
    
    max = -100
    result = -100
    
    for i in range(n):
        if arr_list[i] > max :
            max = arr_list[i]
            
    for i in range(n):
        if arr_list[i] > result and max > arr_list[i]:
            result = arr_list[i]
    
    print(result)
