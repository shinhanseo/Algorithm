def solution(prices):
    answer = [0] * len(prices)
    stack = []

    for current in range(len(prices)):
        while stack and prices[stack[-1]] > prices[current]:
            previous = stack.pop()
            answer[previous] = current - previous

        stack.append(current)

    while stack:
        previous = stack.pop()
        answer[previous] = len(prices) - 1 - previous

    return answer