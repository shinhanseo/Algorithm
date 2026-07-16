from collections import Counter

def solution(topping):
    answer = 0

    left = set()
    right = Counter(topping)

    for topping_type in topping[:-1]:
        left.add(topping_type)

        right[topping_type] -= 1

        if right[topping_type] == 0:
            del right[topping_type]

        if len(left) == len(right):
            answer += 1

    return answer