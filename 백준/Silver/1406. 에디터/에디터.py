import sys

left = list(sys.stdin.readline().strip())
right = []
M = int(sys.stdin.readline())

for _ in range(M) :
  order = sys.stdin.readline().strip()
  if(order.startswith("P")) :
    left.append(order.split()[1])
  
  elif(order == "L") :
    if len(left) != 0 :
      right.append(left.pop())
  
  elif(order == "D") :
    if len(right) != 0 :
      left.append(right.pop())
  
  elif(order == "B") :
    if len(left) != 0 :
      left.pop()

for i in left :
  print(i, end="")
for i in reversed(right) :
  print(i, end="")