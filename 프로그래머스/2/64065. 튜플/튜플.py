def solution(s):
    answer = []
    
    s = s[2:-2]
    groups = s.split("},{")
    
    groups.sort(key=len)
    
    for group in groups:
        nums = group.split(",")
        
        for num in nums:
            num = int(num)
            if num not in answer:
                answer.append(num)
    
    return answer