def solution(babbling):
    lst = ["aya", "ye", "woo", "ma"]
    count = 0
    for bab in babbling:
        for word in lst:
            bab = bab.replace(word, " ")
        if bab.strip() == "":
            count += 1
            
    return count