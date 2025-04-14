import sys

n = int(sys.stdin.readline())
deque = []

for _ in range(n) :
  order = sys.stdin.readline().rstrip()
  o = order.split()
  if(o[0] == "push_front") :
    deque.insert(0, o[1])
  elif(o[0] == "push_back") :
    deque.append(o[1])
  elif(o[0] == "pop_front") :
    if(len(deque) == 0) :
      print("-1")
    else :
      print(deque.pop(0))
  elif(o[0] == "pop_back") :
    if(len(deque) == 0) :
      print("-1")
    else :
      print(deque.pop(-1))
  elif(o[0] == "size") :
    print(len(deque))
  elif(o[0] == "empty") :
    if(len(deque) == 0) :
      print("1")
    else :
      print("0")
  elif(o[0] == "front") :
    if(len(deque) == 0) :
      print("-1")
    else :
      print(deque[0])
  else :
    if(len(deque) == 0) :
      print("-1")
    else :
      print(deque[-1])


