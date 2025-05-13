def solution(arr):
    min = arr[0]
    if len(arr) == 1 :
        return -1
    
    for num in arr[1:] :
        if num < min :
            min = num
    
    arr.remove(min)

    return arr