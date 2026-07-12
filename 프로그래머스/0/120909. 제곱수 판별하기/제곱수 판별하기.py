def solution(n):
    root = int(n ** 0.5)
    
    if root ** 2 == n:
        return 1
    else:
        return 2