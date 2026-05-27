def solution(s):
    answer = 0
    for x in range(len(s)) :
        ch = s[x:] + s[:x]
        if check(ch) :
            answer += 1
    
    return answer
        

def check(s):
    stack = []
    
    pairs = {
        ')': '(',
        ']': '[',
        '}': '{'
    }
        
    for c in s :
        if c in '({[' :
            stack.append(c)
        else :
            if len(stack) == 0 or stack[-1] != pairs[c] :
                return False
            
            stack.pop()
    
    return len(stack) == 0