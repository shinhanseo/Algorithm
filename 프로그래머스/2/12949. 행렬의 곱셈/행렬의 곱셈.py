def solution(arr1, arr2) :
    matrix = []
    length = len(arr2[0])
    for lst1 in arr1 :
        tmp = []
        for i in range(length) :
            sum = 0
            for idx, num in enumerate(lst1) :
                sum += (num * arr2[idx][i])
            tmp.append(sum)
        matrix.append(tmp)   
    return matrix