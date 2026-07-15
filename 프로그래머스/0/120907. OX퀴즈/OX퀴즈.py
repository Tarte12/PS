def solution(quiz):
    answer = []
    k = []
    for s in quiz:
        k = list(map(str, s.split()))
        if k[1] == '+':
            if int(k[0]) + int(k[2]) == int(k[4]):
                answer.append("O")
            else:
                answer.append("X")
        else:
            if int(k[0]) - int(k[2]) == int(k[4]):
                answer.append("O")
            else:
                answer.append("X")
    return answer