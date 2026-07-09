def solution(intStrs, k, s, l):
    answer = []
    
    for strs in intStrs:
        ans = int(strs[s:s+l])
        if ans > k:
            answer.append(ans)
    
    return answer