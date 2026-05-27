def solution(A, B) :
    lst_a = sorted(A)
    lst_b = sorted(B, reverse=True)
    sum = 0
    for a, b in zip(lst_a, lst_b) :
        sum += a*b
    return sum