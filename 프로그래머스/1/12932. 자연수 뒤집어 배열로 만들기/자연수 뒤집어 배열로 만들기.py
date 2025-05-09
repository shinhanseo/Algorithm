def solution(n):
    num_str = str(n)
    answer = []
    for i in num_str[::-1] :
        answer.append(int(i))
    return answer
