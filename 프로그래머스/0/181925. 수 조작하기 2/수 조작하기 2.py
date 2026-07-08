def solution(numLog):
    answer = ""
    
    for idx in range(1, len(numLog)):
        num = numLog[idx] - numLog[idx-1]
        match num:
            case 1:
                answer += "w"
            case -1:
                answer += "s"
            case 10:
                answer += "d"
            case -10:
                answer += "a"
    return answer