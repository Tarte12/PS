def solution(n, control):
    for txt in control:
        match txt:
            case "w":
                n += 1
            case "s":
                n -= 1
            case "d":
                n += 10
            case "a":
                n -= 10
    return n