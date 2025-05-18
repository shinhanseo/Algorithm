def solution(number, limit, power) :
    sum = 0
    for num in range(1, number+1) :
        cnt = 0
        for i in range(1, int(num ** 0.5) + 1):
            if num % i == 0:
                cnt += 2 if i != num // i else 1
        
        if cnt > limit :
            sum += power
        else :
            sum += cnt
    return sum