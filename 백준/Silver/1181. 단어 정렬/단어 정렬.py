import sys

N = int(sys.stdin.readline())
lst = set()

for i in range(N) :
  lst.add(sys.stdin.readline().strip())

sort_lst = sorted(lst, key = lambda x : (len(x), x))

for l in sort_lst :
  print(l)
