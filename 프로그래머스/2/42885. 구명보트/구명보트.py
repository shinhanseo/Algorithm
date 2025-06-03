def solution(people, limit):
    people.sort()
    cnt = 0
    i = 0
    j = len(people) - 1
    while i <= j:
        if people[i] + people[j] <= limit:
            i += 1  # 가벼운 사람 태움
        j -= 1  # 무거운 사람 태움
        cnt += 1  # 보트 하나 사용
    return cnt

print(solution([70, 50, 80, 50], 100))  # 결과: 3
def solution(people, limit):
    people.sort()
    cnt = 0
    i = 0
    j = len(people) - 1
    while i <= j:
        if people[i] + people[j] <= limit:
            i += 1  # 가벼운 사람 태움
        j -= 1  # 무거운 사람 태움
        cnt += 1  # 보트 하나 사용
    return cnt

print(solution([70, 50, 80, 50], 100))  # 결과: 3
