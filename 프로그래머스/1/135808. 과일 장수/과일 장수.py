def solution(k, m, score):
    sort_score = sorted(score, reverse=True)
    idx = 0
    sum = 0
    answer = []
    for i in range(len(sort_score)//m) :
        answer.append(list(sort_score[i] for i in range(idx, idx+m)))
        idx += m
    for i in range(len(answer)) :
        sum += min(answer[i]) * m
    
    return sum