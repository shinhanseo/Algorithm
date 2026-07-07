def solution(num_list):
    answer = []
    num1 = 0
    num2 = 0
    for n in num_list :
        if n%2 == 0 :
            num1 += 1
        else :
            num2 += 1
    return [num1, num2]