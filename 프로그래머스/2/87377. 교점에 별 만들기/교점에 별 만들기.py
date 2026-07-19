def solution(line):
    pos = []
    n = len(line)
    
    # min은 매우 큰 값, max는 매우 작은 값으로 초기화
    x_min = y_min = float('inf')
    x_max = y_max = float('-inf')
    
    for i in range(n):
        a, b, e = line[i]
        for j in range(i + 1, n):
            c, d, f = line[j]
            
            # 평행 또는 일치 확인
            if a * d == b * c:
                continue
                
            x = (b * f - e * d) / (a * d - b * c)
            y = (e * c - a * f) / (a * d - b * c)
            
            # 정수 교점인지 확인
            if x == int(x) and y == int(y):
                x = int(x)
                y = int(y)
                pos.append([x, y])
                
                if x < x_min: x_min = x
                if x > x_max: x_max = x
                if y < y_min: y_min = y
                if y > y_max: y_max = y
                
    x_len = x_max - x_min + 1
    y_len = y_max - y_min + 1
    
    # 격자판 생성
    coord = [['.'] * x_len for _ in range(y_len)]
    
    # 별 찍기
    for star_x, star_y in pos:
        nx = star_x - x_min
        ny = y_max - star_y  # y축은 max_y에서 빼주기
        coord[ny][nx] = '*'
        
    return ["".join(res) for res in coord]