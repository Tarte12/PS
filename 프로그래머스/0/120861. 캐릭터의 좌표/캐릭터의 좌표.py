def solution(keyinput, board):
    c = [0, 0]

    for key in keyinput:
        match key:
            case "up":
                c[1] += 1
            case "down":
                c[1] -= 1
            case "left":
                c[0] -= 1
            case "right":
                c[0] += 1
            
        limit_x = board[0] // 2
        c[0] = max(-limit_x, min(c[0], limit_x))
        limit_y = board[1] //2
        c[1] = max(-limit_y, min(c[1], limit_y))
        
    return c
