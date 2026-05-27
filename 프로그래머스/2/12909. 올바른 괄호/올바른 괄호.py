def solution(s) :
    stack = []
    for i in s :
        stack.append(i)
        if len(stack) > 1 and (stack[-2] == '(' and stack[-1] == ')') :
            for _ in range(2) :
                stack.pop(-1)
    
    if len(stack) == 0 :
        return True
    else :
        return False