def solution(n, w, num) :
    box = []
    box_n = 1
    line_n = 1
    state = 0 
    height = n//w if n%w == 0 else n//w + 1
    cnt = 1
    for _ in range(height) :    
        line = []
        for _ in range(w) :
            if line_n%2 == 1 :
                line.append(box_n)
            else :
                line.insert(0,box_n)
           
            if box_n >= n :
                state = 1

            if state :
                box_n = 0
            else :
                box_n += 1

        box.append(line)
        line_n += 1
    
    for i in range(len(box)):         # 행 인덱스
        for j in range(len(box[0])):  # 열 인덱스
            if box[i][j] == num:
                row = i
                col = j
                break

    for i in range(row+1, len(box)) :
        if box[i][col] != 0 :
            cnt += 1
    
    return cnt