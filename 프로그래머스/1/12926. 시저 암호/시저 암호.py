def solution(s, n):
    answer = ''
    for alp in s:
        # 1. 공백 처리
        if alp == " ":
            answer += alp
        # 2. 대문자 처리 (아스키코드가 대소문자가 분리되어 있음)
        elif alp.isupper():
            answer += chr((ord(alp) - ord('A') + n) % 26 + ord('A'))
        # 3. 소문자 처리
        elif alp.islower():
            answer += chr((ord(alp) - ord('a') + n) % 26 + ord('a'))
    return answer