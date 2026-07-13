def solution(array, n):
    # 가장 가까운 수가 여러 개이면 더 작은 수 고르기 위한 정렬
    array.sort()
    
    min_x = 99
    for num in array:
        # 절대값을 구하는 파이썬 내장 함수 abs()
        x = abs(num - n)
        if min_x > x:
            min_x = x
            index_num = num
    
    return index_num