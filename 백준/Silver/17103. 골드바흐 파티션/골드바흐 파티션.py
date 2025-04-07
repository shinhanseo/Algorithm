import sys

N = int(sys.stdin.readline())

prime = [False] * 1000001
for i in range(2, 1000001) :
  state = 0
  for j in range(2, int(i**0.5) + 1) :
    if(i % j == 0) : 
      state = 1
      break

  if(state == 0) :
    prime[i] = True

for _ in range(N) :
  num = int(sys.stdin.readline())
  cnt = 0
  for j in range(2, num//2+1) :
    if prime[j] and prime[num-j] :
      cnt += 1
  
  print(cnt)

 
     




