def solution(id_list, report, k) :
    dic = {name : 0 for name in id_list}
    email = {name : [] for name in id_list}
    result = []
    for lst in set(report) :
        name, rep = lst.split(' ')
        dic[rep] += 1
        email[name].append(rep)
    lst = [key for key, val in dic.items() if val >= k]
    for name in id_list :
        sum = 0
        for n in lst :
            if n in email[name] :
                sum +=1
        result.append(sum)

    return result