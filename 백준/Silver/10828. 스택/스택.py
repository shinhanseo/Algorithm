import sys

N = int(sys.stdin.readline())
stack = []
for _ in range(N):
    order = sys.stdin.readline().strip()  # 개행 문자 제거

    if order.startswith("push"):
        stack.append(int(order.split()[1]))
    elif order == "pop":
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif order == "size":
        print(len(stack))
    elif order == "empty":
        print(0 if stack else 1)
    elif order == "top":
        if stack:
            print(stack[-1])
        else:
            print(-1)
