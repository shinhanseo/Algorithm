def solution(k, tangerine) :
    dic = {key : 0 for key in set(tangerine)}
    for i in tangerine :
        dic[i] += 1
    s_dic = dict(sorted(dic.items(), key = lambda x : x[1], reverse=True))
    cnt =  0
    for key, value in s_dic.items() :
        k -= value 
        cnt += 1
        if k <= 0 :
            break
    return cnt