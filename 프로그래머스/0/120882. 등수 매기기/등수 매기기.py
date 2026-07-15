def solution(score):
    lst = []
    answer = []
    for math, eng in score:
        lst.append((math+eng)/2)
    sorted_lst = sorted(lst, reverse=True)
    for x in lst:
        answer.append(sorted_lst.index(x) + 1)
    return answer