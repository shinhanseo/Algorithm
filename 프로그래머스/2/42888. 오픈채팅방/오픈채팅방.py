def solution(record):
    dic = {}
    answer = []
    result = []
    for i in record :
        state = i[0] 
        if state == 'E' :
            state, user, name = i.split()
            dic[user] = name
            result.append([state,user])
        elif state == 'L' :
            state, user = i.split()
            result.append([state,user])
        else :
            state, user, name = i.split()
            dic[user] = name 
    for state, user in result :
        if(state == "Enter") :
            answer.append(f"{dic[user]}님이 들어왔습니다.")
        else :
            answer.append(f"{dic[user]}님이 나갔습니다.")
    return answer