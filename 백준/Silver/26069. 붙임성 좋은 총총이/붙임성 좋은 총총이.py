import sys

N = int(sys.stdin.readline())
name = set()
name.add("ChongChong")

for _ in range(N) :
  A, B = sys.stdin.readline().split()
  if(A in name or B in name) :
    name.add(A)
    name.add(B)

print(len(name))