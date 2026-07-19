def solution(n, left, right):
    answer = []

    for index in range(left, right + 1):
        row = index // n
        column = index % n

        answer.append(max(row, column) + 1)

    return answer