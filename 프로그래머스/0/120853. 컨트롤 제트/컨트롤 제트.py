def solution(s):
    res = 0
    answer = list(map(str, s.split()))
    for i in range(len(answer)):
        if answer[i] == 'Z':
            res -= int(answer[i-1])
        else:
            res += int(answer[i])
    return res