import sys

N = int(sys.stdin.readline())
N_lst = list(sys.stdin.readline().split())


M = int(sys.stdin.readline())
M_lst = list(sys.stdin.readline().split())

dic = {}
for i in M_lst :
  dic[i] = 0

for i in N_lst :
  if i in dic :
    dic[i] = 1

for i in dic :
  print(f"{dic[i]} ", end="")
   

