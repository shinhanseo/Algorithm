def solution(n) :
    answer = []
    result = ""
    for i in str(n) :
        answer.append(i)

    answer.sort(reverse=True)
    for i in answer :
        result += i

    return int(result)