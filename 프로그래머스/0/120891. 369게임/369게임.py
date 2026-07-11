def solution(order):
    str1 = str(order)
    return str1.count('3') + str1.count('6') + str1.count('9')