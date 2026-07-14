def solution(dots):
    lx =  [d[0] for d in dots] #모든 x 좌표 리스트
    ly =  [d[1] for d in dots] #모든 y 좌표 리스트
    return (max(lx)-min(lx))*(max(ly)-min(ly))