def solution(n):
    answer = 0
    for num in range(1, n+1):
        x = 0
        for i in range(1, num+1):
            if num%i == 0:
                x+= 1
        if x >= 3:
            answer += 1
    return answer