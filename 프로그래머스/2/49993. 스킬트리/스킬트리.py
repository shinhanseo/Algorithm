def solution(skill, skill_trees):
    answer = 0
    s_lst = [x for x in skill]
    
    for st in skill_trees :
        idx = 0
        state = True
        for s in st :
            if s in s_lst :
                if s == s_lst[idx] :
                    if idx < len(s_lst) - 1 :
                        idx += 1
                        
                else :
                    state = False
                    break
        
        if state :
            answer += 1
            
    
    
    return answer