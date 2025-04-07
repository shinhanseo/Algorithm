import sys

N, M = map(int, sys.stdin.readline().split())
lst_S = list(sys.stdin.readline().strip() for _ in range(N))
lst_M = list(sys.stdin.readline().strip() for _ in range(M))

cnt = 0
dic = {}

for i in lst_S :
  dic[i] = 0

for i in lst_M :
  if i in dic :
    cnt+=1

print(cnt)