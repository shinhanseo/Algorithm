N, K = map(int, input().split())
lst = []
cnt = 0

for i in range(1, N+1) :
  if(N % i == 0) :
    lst.append(i)
    cnt += 1

if(cnt < K) :
  print("0")
else :
  print(lst[K-1])