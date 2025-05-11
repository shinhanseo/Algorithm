def solution(n, words) :
    last_word = words[0][-1]
    turn = 1
    people = 1
    used_word = [words[0]]
    state = 0
    for i in words[1:] :
        people = (people % n) + 1

        if people == 1 :
            turn += 1

        if last_word != i[0] :
            state = 1
            break
        elif i in used_word :
            state = 1
            break
        used_word.append(i)    
        last_word = i[-1]

    if state :
        return [people, turn]
    else :
        return [0,0]