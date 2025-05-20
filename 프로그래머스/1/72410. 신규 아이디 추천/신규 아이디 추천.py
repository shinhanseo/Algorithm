def solution(new_id) :
    result = ""
    for ch in new_id :  # 1단계
        if ch.isupper() :
            result += ch.lower()
            continue
        result += ch
    new_id = result
    result = ""

    for ch in new_id : # 2단계
        if ch.isalpha() or ch.isdigit() or ch == '-' or ch == '_' or ch == '.' :
            result += ch
    new_id = result
    result = ""

    prev = ""
    for ch in new_id : # 3단계
        if ch == '.' and prev == '.' :
            continue
        result += ch
        prev = ch
    new_id = result
    result = ""

    for idx, ch in enumerate(new_id) : # 4단계
        if (ch == '.' and idx == 0 ) or (ch == '.' and idx == len(new_id)-1) :
            continue
        result += ch
    new_id = result

    if new_id == "" :
        new_id = 'a'

    if len(new_id) >= 16 : 
        new_id = result[:15]
        if new_id[-1] == '.' :
            new_id = result[:14]
    
    if len(new_id) <= 2 :
        while len(new_id) <= 2 :
            new_id += new_id[-1]
    
    return new_id