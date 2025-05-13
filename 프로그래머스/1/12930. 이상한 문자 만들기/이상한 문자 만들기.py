def solution(n) :
    lst = [x for x in n.split(' ')]
    result = []
    for i in lst :
        word = ''
        for idx, ch in enumerate(i) :
            if idx%2 == 0 :
                word += ch.upper()
            else :
                word += ch.lower()
        result.append(word)

    return ' '.join(result)