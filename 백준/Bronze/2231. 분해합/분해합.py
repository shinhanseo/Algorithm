def find_constructor(N) :
  d = len(str(N))
  start =  start = max(1, N - 9 * d)  # 시작점을 최소 1 이상으로 보정
  for i in range(start, N) :
    sum_digit = 0
    for j in range(len(str(i))) :
      sum_digit += int(str(i)[j])
    sum_digit += i

    if(sum_digit == N) :
      return i 
    
  return 0

N = int(input())
c = find_constructor(N)

print(c)
