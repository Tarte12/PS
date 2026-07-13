from collections import Counter

def solution(s):
    answer = ''
    counter = Counter(s)
    
    for char, count in counter.items():
        if count == 1:
            answer += char
    # sorted() -> 문자열을 집어넣으면 쪼개서 리스트로 반환
    # sort() -> 리스트로 변환해서 sort() 쓰고 다시 합쳐야 함
    # "".join() <- 다시 합치는 용도
    return "".join(sorted(answer))