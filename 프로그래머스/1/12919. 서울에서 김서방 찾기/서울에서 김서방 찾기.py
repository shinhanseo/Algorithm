def solution(seoul):
    idx = 0
    for name in seoul :
        if name == "Kim" :
            break
        idx += 1
    return f"김서방은 {idx}에 있다"