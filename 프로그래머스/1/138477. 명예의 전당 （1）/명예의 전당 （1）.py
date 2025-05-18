def solution(k, score) :
    lst = []
    result = []
    for idx, i in enumerate(score) :
        if idx < k :
            lst.append(i)   
            lst.sort(reverse=True)
        else :
            if lst[-1] < i :
                lst[-1] = i
                lst.sort(reverse=True)   
        result.append(lst[-1])

    return result