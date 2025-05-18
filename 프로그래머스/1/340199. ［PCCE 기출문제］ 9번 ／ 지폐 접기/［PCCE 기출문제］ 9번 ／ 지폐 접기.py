def solution(wallet, bill) :
    cnt = 0
    while True :
        if (wallet[0] >= bill[0] and wallet[1] >= bill[1]) or (wallet[1] >= bill[0] and wallet[0] >= bill[1]) :
            break
        else :
            bill[bill.index(max(bill))] = max(bill) // 2
            cnt += 1
    return cnt