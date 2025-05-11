def solution(x, n):
    num = x
    result = []
    for _ in range(n) :
        result.append(x)
        x += num

    return result
