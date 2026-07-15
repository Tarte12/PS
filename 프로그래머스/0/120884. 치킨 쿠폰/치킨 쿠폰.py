def solution(chicken):
    answer = 0  # 최종 서비스 치킨 수를 누적할 변수
    cupon = chicken  # 처음 시작할 때는 주문한 치킨 수만큼 쿠폰이 있습니다.
    
    while cupon >= 10:
        new_service = cupon // 10  # 새로 주문하는 서비스 치킨
        answer += new_service       # 누적 합산
        
        # 남은 쿠폰 = (서비스 치킨을 바꾸고 남은 쿠폰) + (서비스 치킨으로 새로 받은 쿠폰)
        cupon = (cupon % 10) + new_service 
        
    return answer