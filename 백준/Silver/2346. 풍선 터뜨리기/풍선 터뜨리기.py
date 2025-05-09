import sys

N = int(sys.stdin.readline())
papers = list(map(int, sys.stdin.readline().split()))

# 풍선 리스트: (번호, 이동 수)
balloons = [(i + 1, papers[i]) for i in range(N)]

result = []
index = 0  # 시작 위치

while balloons:
    num, move = balloons.pop(index)
    result.append(num)

    if not balloons:
        break

    if move > 0:
        index = (index + (move - 1)) % len(balloons)
    else:
        index = (index + move) % len(balloons)

print(*result)
