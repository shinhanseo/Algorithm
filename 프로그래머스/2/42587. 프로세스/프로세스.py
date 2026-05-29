def solution(priorities, location):
    answer = 0
    
    dq = []
    for idx, p in enumerate(priorities) :
        dq.append([idx, p])
    
    while len(dq) != 0 :
        del_lst = dq.pop(0)
        if any(val[1] > del_lst[1] for val in dq) :
            dq.append(del_lst)
        else :
            answer += 1
            
            if del_lst[0] == location :
                break
    
    return answer
   