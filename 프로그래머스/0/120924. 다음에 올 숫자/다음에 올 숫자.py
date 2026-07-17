def solution(common):
    # 등차 수열
    if common[1] - common[0] == common[2] - common[1]:
        return common[-1] + (common[1] - common[0])
    else:
        return common[-1]*(common[1]//common[0])
