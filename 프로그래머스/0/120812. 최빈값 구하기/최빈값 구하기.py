from collections import Counter 
def solution(array):
    counter = Counter(array)
    modes = counter.most_common()
    
    if len(modes) == 1:
        return modes[0][0]
    if modes[0][1] == modes[1][1]:
        return -1
    else:
        return modes[0][0]