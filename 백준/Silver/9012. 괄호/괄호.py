import sys

N = int(sys.stdin.readline())

result = []

for _ in range(N) :
  stack = []
  lst = list(sys.stdin.readline().strip())
  if(lst[0] == ')') :
    print("NO")
    continue

  for i in lst :
    stack.append(i)
    if((len(stack) >= 2) and (stack[-2] == '(' and stack[-1] == ')')) :
      del stack[-2:]
  
  if(len(stack) == 0) :
    print("YES")
  else :
    print("NO")

