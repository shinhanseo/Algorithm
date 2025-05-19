def solution(keymap, targets) :
    result = []
    for target in targets :
        sum = 0
        for t in target :
            idx = []
            for key in keymap :
                if t in key :
                    idx.append(key.index(t)+1)
            if idx :
                sum += min(idx) 
            else :
                sum = -1
                break
        result.append(sum)
    return result