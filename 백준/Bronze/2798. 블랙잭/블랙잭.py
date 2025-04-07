N, M = map(int , input().split())
lst = (list(map(int, input().split())))
sum = 0
result = []

for i in range(N) :
  for j in range(i+1, N) :
    for k in range(j+1, N) :
      sum = lst[i] + lst[j] + lst[k]
      if(M >= sum) :
        result.append(sum)

print(max(result))

