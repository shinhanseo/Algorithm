import sys

n = int(sys.stdin.readline())
result = 1
for i in range(1, n+1) :
  result *= i
num = str(result)
cnt = 0

for i in num[::-1] :
  if(i=='0') :
    cnt += 1
  else :
    break

print(cnt)