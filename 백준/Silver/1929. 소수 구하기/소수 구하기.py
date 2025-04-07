import sys

M, N = map(int, sys.stdin.readline().split())
state = 0

for val in range(M, N+1) :
  if(val == 0 or val == 1) :
    continue
  
  for i in range(2, int(val**0.5 + 1)) :
    if(val % i == 0) :
      state = 1
      break
  if(state == 0) :
    print(val)
  else :
    state = 0
      