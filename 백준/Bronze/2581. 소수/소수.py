M = int(input())
N = int(input())
lst = []
sum = 0

for i in range(M, N+1) :

  if (i==1) :
    continue
  elif (i==2) :
    lst.append(i)
    sum += i
  else :

    state = 0
    
    for j in range(2, int(i ** 0.5) + 1) :
      if(i % j == 0) :
        state = 1
    
    if(state == 0) :
      lst.append(i)
      sum += i

if(len(lst) != 0) :
  print(f"{sum}")
  print(f"{min(lst)}")
else :
  print("-1")    
    
