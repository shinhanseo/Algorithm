def solution(citations):
    answer = 0
    
    for i in range(1, len(citations)+1) :
        count = 0
        for citation in citations :
            if i <= citation :
                count += 1
            
            if count >= i :
                answer += 1
                break
    
    
    return answer   