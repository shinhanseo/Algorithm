def solution(n) :
    cnt = 0
    for i in range(1, n+1) :
        sum = 0 
        for j in range(i, n+1) :
            sum += j 
            if sum > n :
                break
            elif sum == n :
                cnt +=1
                break
    return cnt