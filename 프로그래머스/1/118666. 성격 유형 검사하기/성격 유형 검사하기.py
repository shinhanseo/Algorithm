def solution(survey, choices) :
    result = ""
    dic = {"R" : 0, "T" : 0, "C" : 0, "F" : 0, "J" : 0, "M" : 0, "A" : 0, "N" : 0,}
    point = [3,2,1,0,1,2,3]
    for s, num in zip(survey,choices) :
        if num > 4 :
            dic[s[1]] += point[num-1]
        else :
            dic[s[0]] += point[num-1]

    for i in range(0, len(list(dic.items())), 2) :
        lst = list(dic.items())[i:i+2]
        if lst[0][1] >= lst [1][1] :
            result += lst[0][0]
        else :
            result += lst[1][0]
    return result