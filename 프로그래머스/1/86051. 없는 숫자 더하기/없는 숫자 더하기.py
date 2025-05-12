def solution(numbers) :
    result = 0
    arr = [1,2,3,4,5,6,7,8,9]
    for num in numbers :
        if num in arr :
            arr.remove(num)

    for i in arr :
        result += i
    
    return result