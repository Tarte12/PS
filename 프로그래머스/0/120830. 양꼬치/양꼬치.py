def solution(n, k):
    service = n//10 
    drink = k - service
    return n*12000 + drink*2000