def solution(before, after):
    before = list(before)
    after = list(after)
    return 1 if sorted(before) == sorted(after) else 0
