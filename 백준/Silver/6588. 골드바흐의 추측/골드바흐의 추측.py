import sys

prime = [False] * 1000001
for i in range(2, 1000001) :
  state = 0
  for j in range(2, int(i**0.5) + 1) :
    if(i % j == 0) : 
      state = 1
      break

  if(state == 0) :
    prime[i] = True

while(1) :
  n = int(sys.stdin.readline())
  if(n==0): break

  prime_state=1
  for i in range(2, n//2 + 1) :
    if prime[i] and prime[n-i] :
      print(f"{n} = {i} + {n-i}")
      prime_state=0
      break
  
  if prime_state :
    print("Goldbach's conjecture is wrong.")