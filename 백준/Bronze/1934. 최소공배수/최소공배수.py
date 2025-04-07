import sys, math

T = int(sys.stdin.readline())
#lst = [list(map(int, sys.stdin.readline().split())) for _ in range(T)]
for _ in range(T) :
  a, b = map(int, sys.stdin.readline().split())
  print(math.lcm(a,b))