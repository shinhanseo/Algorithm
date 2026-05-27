def solution(progresses, speeds):
    answer = []

    while progresses:
        for i in range(len(progresses)):
            progresses[i] += speeds[i]

        count = 0
        for p in progresses:
            if p >= 100:
                count += 1
            else:
                break

        if count > 0:
            answer.append(count)
            progresses = progresses[count:]
            speeds = speeds[count:]

    return answer