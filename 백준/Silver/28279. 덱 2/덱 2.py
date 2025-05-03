import sys
from collections import deque

N = int(sys.stdin.readline())
deck = deque()

for _ in range(N):
    order = sys.stdin.readline().split()

    if order[0] == '1':
        deck.appendleft(int(order[1]))
    elif order[0] == '2':
        deck.append(int(order[1]))
    elif order[0] == '3':
        print(deck.popleft() if deck else -1)
    elif order[0] == '4':
        print(deck.pop() if deck else -1)
    elif order[0] == '5':
        print(len(deck))
    elif order[0] == '6':
        print(0 if deck else 1)
    elif order[0] == '7':
        print(deck[0] if deck else -1)
    elif order[0] == '8':
        print(deck[-1] if deck else -1)
