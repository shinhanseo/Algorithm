def solution(want, number, discount):
    answer = 0
    r = 0

    w_dic = {}

    for w, num in zip(want, number):
        w_dic[w] = num

    while r < len(discount) - 9:
        d_dic = {w: 0 for w in want}

        for i in range(r, r + 10):
            if discount[i] in d_dic:
                d_dic[discount[i]] += 1

        if w_dic == d_dic:
            answer += 1

        r += 1

    return answer