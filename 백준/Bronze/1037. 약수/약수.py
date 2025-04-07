import sys

num = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))

if(len(lst) == 1) :
  print(lst[0] * lst[0])
else :
  print(max(lst) * min(lst))