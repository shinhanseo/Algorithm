import sys

while True:
    string = sys.stdin.readline().rstrip()
    if string == '.':
        break

    stack = []
    valid = True

    for ch in string:
        if ch == '(' or ch == '[':
            stack.append(ch)
        elif ch == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                valid = False
                break  # <- 이거는 유지해도 됨 (괄호 불일치니까 종료)
        elif ch == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                valid = False
                break  # <- 여기도 마찬가지

    if valid and not stack:
        print("yes")
    else:
        print("no")
