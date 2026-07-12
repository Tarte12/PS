def solution(s1, s2):
    x = min(s1, s2)
    y = max(s1, s2)
    answer = 0
    for i in x:
        if i in y:
            answer += 1
    return answer