import sys

N = int(sys.stdin.readline())
cnt = 0
stack = set()

for _ in range(N) :
  talk = sys.stdin.readline().strip()
  if(talk != "ENTER") :
    if talk not in stack :
      cnt += 1
      stack.add(talk)
  else :
      stack.clear()
    

print(cnt)

