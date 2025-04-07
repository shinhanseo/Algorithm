import sys

N, M = map(int, sys.stdin.readline().split())
N_lst = set(map(int, sys.stdin.readline().split()))
M_lst = set(map(int, sys.stdin.readline().split()))

lst = list(N_lst & M_lst)

for i in lst :
  N_lst.remove(i)
  M_lst.remove(i)

print(len(list(N_lst)) + len(list(M_lst)))
