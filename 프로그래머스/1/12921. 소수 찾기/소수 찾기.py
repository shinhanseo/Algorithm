def solution(n) :
    result = []
    for num in range(2, n+1) :
        state = True
        for i in range(2, int(num**0.5)+1) :
            if num%i == 0 :
                state = False
                break
        if state :
            result.append(num)
    
    return len(result)