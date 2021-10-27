def wrap(string, max_width):
    string_list = list(string)
    i = 1
    while max_width * i < len(string):
        string_list.insert(max_width * i + i - 1, "\n")
        i += 1
    return ''.join(string_list)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)