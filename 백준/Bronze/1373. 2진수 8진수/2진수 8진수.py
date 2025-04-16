import sys

num = sys.stdin.readline().strip()
three = ""
lst = []
cnt = 0
if(len(num)%3 != 0) :
  while(len(num)%3 != 0) :
    num = '0' + num

for i in num :
  three += i
  cnt += 1
  if(cnt == 3) :
    lst.append(three)
    cnt = 0
    three = ""

for i in lst :
  sum = 0
  cnt = 0
  for j in i[::-1] :
    sum +=  int(j) * (2**cnt)
    cnt += 1
  
  print(sum, end="")