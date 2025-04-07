import sys

N = int(sys.stdin.readline())
N_lst = list(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline())
M_lst = list(map(int, sys.stdin.readline().split()))

dic1 = {}
for x in N_lst:
    if x in dic1:
        dic1[x] += 1
    else:
        dic1[x] = 1

for element in M_lst:
    if element in dic1:
        print(dic1[element], end=' ')
    else:
        print(0, end=' ')