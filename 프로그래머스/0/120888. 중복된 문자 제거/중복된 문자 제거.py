def solution(my_string):
    answer = ''
    alp = []
    for i in my_string:
        if not i in alp:
            alp.append(i)
            answer += i
        else:
            continue
    return answer