def solution(s):
    length = len(s)
    result = ""
    if length%2 == 0 :
        idx = length // 2
        for i in range(idx-1, idx+1) :
            result += s[i]
    else :
        idx = length // 2
        result = s[idx]
        
    return result