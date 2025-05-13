def solution(array, commads) :
    result = []
    for x in commads :
        ijk = [c for c in x]
        lst = sorted(array[ijk[0]-1:ijk[1]])
        result.append(lst[ijk[2]-1])
    return result