def solution(polynomial):
    lst = list(map(str, polynomial.split()))
    lst_x = []
    lst_n = []
    
    for x in lst:
        if 'x' in x:
            if x == 'x':
                lst_x.append(1)
            else:
                lst_x.append(int(x[:-1]))
        elif "+" in x:
            continue
        else:
            lst_n.append(int(x))
            
    x_sum = sum(lst_x)
    n_sum = sum(lst_n)

    if n_sum == 0:
        return 'x' if x_sum == 1 else f"{x_sum}x"
        
    elif x_sum == 0:
        return str(n_sum)
        
    else:
        x_str = 'x' if x_sum == 1 else f"{x_sum}x"
        return f"{x_str} + {n_sum}"