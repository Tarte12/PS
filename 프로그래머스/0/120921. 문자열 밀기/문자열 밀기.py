def solution(A, B):
    if A == B:
        return 0
    for i in range(1, len(A)+1):
        move = A[-i:] + A[:-i]
        if move == B:
            return i
    return -1