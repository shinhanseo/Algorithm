import sys

N, M = map(int, sys.stdin.readline().split())
lst = list(sys.stdin.readline().strip() for _ in range(N))
test = list(sys.stdin.readline().strip() for _ in range(M))

dic = {}
cnt = 1

for i in lst :
  dic[i] = cnt
  cnt += 1

for t in test :
  if(t.isdigit()) :
    print(lst[int(t)-1])
  else :
    print(dic[t])