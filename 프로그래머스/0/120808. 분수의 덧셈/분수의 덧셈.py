import math

def solution(numer1, denom1, numer2, denom2):
    answer = []
    answer.append(numer1*denom2 + numer2*denom1)
    answer.append(denom1*denom2)
    g = math.gcd(answer[0], answer[1])
    answer[0] = answer[0]/g
    answer[1] = answer[1]/g
    
    return answer