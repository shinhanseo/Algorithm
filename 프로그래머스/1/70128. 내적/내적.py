def solution(a, b):
    sum = 0
    for a, b in zip(a, b) :
        sum += a*b
    return sum