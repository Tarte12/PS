def solution(phone_number):
    answer = ''
    numbers = phone_number[-4:]
    stars = len(phone_number)-4
    answer = '*'*stars + numbers
    return answer