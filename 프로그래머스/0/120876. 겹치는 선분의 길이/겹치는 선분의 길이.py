def solution(lines):
    dic = {}
    for line in lines:
        start, end = line[0], line[1]
      
        for i in range(start, end):
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
        
    answer = 0
    
    for count in dic.values():
        if count >= 2:
            answer += 1
    return answer