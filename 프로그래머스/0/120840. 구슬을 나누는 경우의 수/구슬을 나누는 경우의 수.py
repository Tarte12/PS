def solution(balls, share):
    x = 1
    y = 1
    z = 1
    for num in range(1, balls+1):
        x *= num
    for num in range(1, share+1):
        y *= num
    n = balls-share
    for num in range(1, n+1):
        z *= num
    return x//(y*z)