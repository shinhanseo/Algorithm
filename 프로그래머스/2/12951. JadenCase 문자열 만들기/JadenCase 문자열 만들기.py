def solution(s) :
    result = ""
    for idx, ch in enumerate(s) :
        if (idx == 0) or (s[idx-1] == ' ' and idx >= 1) :
            if ch.isalpha() :
                result += ch.upper()
            else :
                result += ch
        else :
            if ch == ' ' :
                result += ' '
            else :
                result += ch.lower() 
    return result