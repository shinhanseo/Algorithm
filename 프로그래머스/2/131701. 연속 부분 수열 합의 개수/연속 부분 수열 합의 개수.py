def solution(elements):
    s = set()
    n = len(elements)

    for length in range(1, n + 1):
        for _ in range(n):
            s.add(sum(elements[:length]))
            elements.append(elements.pop(0))

    return len(s)