def solution(my_string):
    my_string = list(map(str, my_string.split()))
    stack = []
    sign = 1
    for x in my_string:
        if x.isdigit():
            stack.append(int(x)*sign)
        elif x == '+':
            sign = 1
        elif x == '-':
            sign = -1
        
    return sum(stack)
