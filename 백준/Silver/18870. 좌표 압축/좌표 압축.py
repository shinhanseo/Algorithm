import sys

N = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))

s = sorted(set(lst))
dic = {value : idx for idx, value in enumerate(s)}

for i in lst :
  print(dic[i], end=" ")