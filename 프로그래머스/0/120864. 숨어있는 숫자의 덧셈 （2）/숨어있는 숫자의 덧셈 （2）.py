def solution(my_string):
    # 숫자가 아니면 공백으로 채운 새로운 문자열 만들기
    s = ''.join(c if c.isdigit() else ' ' for c in my_string)
    
    # 공백 기준으로 쪼개서 숫자들만 다 더하기
    return sum(int(num) for num in s.split())