def solution(i, j, k):
    res = 0
    for x in range(i, j+1):
        x = str(x)
        for s in x:
            if s == str(k):
                res += 1
    return res