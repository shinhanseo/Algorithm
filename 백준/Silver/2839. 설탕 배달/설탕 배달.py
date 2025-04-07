N = int(input())

sum = 0
min = 5000

for i in range((N//5) + 1) :
  for j in range((N//3) + 1) :
    sum = 5 * i + 3 * j
    if(sum == N) :
      if(min > (i+j)) :
        min = i + j
      break

if(min == 5000) :
  print("-1")
else :
  print(min)