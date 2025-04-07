import sys

N, M = map(int, sys.stdin.readline().split())
N_lst = set(sys.stdin.readline().strip() for _ in range(N))

M_lst = set(sys.stdin.readline().strip() for _ in range(M))

lst = sorted(N_lst & M_lst)

print(len(lst))
for name in lst :
  print(name)