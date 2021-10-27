if __name__ == '__main__':

    records = []
    scores = []

    for _ in range(int(input())):
        name = input()
        score = float(input())
        scores.append(score)
        records.append([name,score])
    
    scores.sort()
    result_score = 0.0
    result_name = []
    
    for s in scores:
        if result_score == 0.0:
            result_score = s
        elif result_score < s:
            result_score = s
            break
    
    for record in records:
        if result_score == record[1]:
            result_name.append(record[0])
    
    result_name.sort()
            
    for name in result_name:
        print(name)
    
