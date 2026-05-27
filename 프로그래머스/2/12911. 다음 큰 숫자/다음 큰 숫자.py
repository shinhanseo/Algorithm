def change(n) :
    result = ""
    while n > 0 :
        result = str(n%2) + result
        n //= 2
    return result 

def solution(n) :
    cnt = 0
    for i in change(n) :
        if i == '1' :
            cnt += 1
    while True :
        cnt_2 = 0
        n += 1
        for i in change(n) :
            if i == '1' :
                cnt_2 += 1
        if cnt == cnt_2 :
            return n 


