def solution(s) :
    stack = []
    for ch in s :
        stack.append(ch)
        if len(stack) > 1 and stack[-1] == stack[-2] :
            stack.pop(-1)
            stack.pop(-1)
    if len(stack) == 0 :
        return 1
    else :
        return 0