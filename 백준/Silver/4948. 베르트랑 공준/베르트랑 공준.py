import sys

lst = []

while(1) :
  n = int(sys.stdin.readline())
  if(n==0) :
    break
  cnt = 0
  state = 0
  for i in range(n+1, 2*n+1) :
    if(i==0 or i==1) :
      continue

    for j in range(2, int(i**0.5+1)) :
      if(i % j == 0) :
        state = 1
        break
    
    if(state == 1) :
      state = 0
    else :
      cnt += 1

  print(cnt)