def solution(a, b, n) :
    sum = 0
    while n >= a :
        sum += b*(n//a)
        n = b*(n//a) + n%a
    return sum