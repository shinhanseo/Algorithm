num = int(input())
lst = list(map(int, input().split()))
cnt = 0

for i in lst :
  if(i == 1) :
    continue

  elif(i == 2) :
    cnt+=1
    continue
  
  else :
    state = 0

    for j in range(2, i) :
      if(i % j == 0) :
        state = 1
    
    if(state == 0) :
      cnt += 1

print(cnt)