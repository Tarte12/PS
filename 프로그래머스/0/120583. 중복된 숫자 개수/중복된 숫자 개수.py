def solution(array, n):
    res = 0
    for x in array:
        if x == n:
            res += 1
    return res