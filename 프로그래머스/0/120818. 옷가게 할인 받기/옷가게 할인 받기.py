def solution(price):
    match price:
        case p if p >= 500000:
            return price* 80 // 100
        case p if p >= 300000:
            return price* 90 // 100
        case p if p >= 100000:
            return price* 95 // 100
        case _:
            return price
    
