def solution(number):
    # int(number)%9
    # 파이썬에서는 보안상 이유로 문자열 -> 숫자 변환에 자릿수 제한 O
    # 기본 4300자 <- 그래서 지금 범위를 벗어나서 안 됨
    sol = 0
    
    for num in number:
        sol += int(num)
    return  sol%9