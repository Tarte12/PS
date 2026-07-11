def solution(hp):
    res = 0
    if hp >= 5:
        res += hp//5
        hp = hp%5
    if hp >= 3: 
        res += hp//3
        hp = hp%3
    if hp >= 1:
        res += hp
    return res