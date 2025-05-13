def solution(phone_number):
    result = []
    answer = ""
    for i in phone_number :
        result.append(i)

    for i in range(len(phone_number[0:-4])) :
        result[i] = '*'

    for i in result :
        answer += i

    return answer