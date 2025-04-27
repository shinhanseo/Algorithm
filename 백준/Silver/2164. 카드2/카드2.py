import sys
from collections import deque

N = int(sys.stdin.readline())
card = deque(range(1, N+1))
cnt = 0

while len(card) > 1:
    cnt += 1
    if cnt % 2:
        card.popleft()
    else:
        card.append(card.popleft())

print(*card)
