def solution(s) :
    cnt = 0
    turn = 0
    while s != '1' : 
        result = ""
        one = ""
        for i in s :
            if i == '1' :
                one += '1'
            else :
                cnt += 1

        length = len(one)
        while length > 0 :
            result = str(length%2) + result
            length //= 2
        turn += 1
        s = result

    return [turn, cnt]