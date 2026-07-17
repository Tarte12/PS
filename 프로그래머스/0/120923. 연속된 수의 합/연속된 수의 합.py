def solution(num, total):
    # 연속된 수의 시작 숫자를 수학적으로 바로 계산
    start = (total - sum(range(num))) // num
    
    # 시작 숫자부터 num개의 연속된 배열을 만들어 반환
    return [start + i for i in range(num)]