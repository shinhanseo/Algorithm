import sys

N = int(sys.stdin.readline())
lst = []
state = 0

for _ in range(N) :
  val = int(sys.stdin.readline())

  while(1) :
    if(val == 0 or val == 1) :
      lst.append(2)
      break
    for i in range(2,int(val**0.5)+1) :
      if(val % i == 0) :
        state = 1
        break
    
    if(state == 0) :
      lst.append(val)
      break
    else :
      state = 0
      val += 1

for i in lst :
  print(i)




