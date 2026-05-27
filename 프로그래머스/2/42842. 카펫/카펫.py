def solution(brown, yellow) :
    lst = []
    for i in range(1, int(yellow**0.5)+1) :
        if yellow % i == 0 :
            lst.append([yellow//i, i])
    for i in lst :
        if brown == (i[0] + i[1]) * 2 + 4 :
            return [i[0]+2, i[1]+2]