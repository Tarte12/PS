def solution(my_string):
    remove = "aeiou"
    res = my_string
    for alp in my_string:
        if alp in remove:
            res = res.replace(alp, "")
    return res