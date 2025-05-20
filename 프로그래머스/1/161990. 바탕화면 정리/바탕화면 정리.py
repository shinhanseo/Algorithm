def solution(wallpaper) :
    row = []
    col = []
    for idx, i in enumerate(wallpaper) :
        if '#' in i : 
            row.append(idx)
            for idx2, j in enumerate(i) :
                if j == '#' :
                    col.append(idx2)
    result = [min(row), min(col), max(row)+1, max(col)+1]
    return result