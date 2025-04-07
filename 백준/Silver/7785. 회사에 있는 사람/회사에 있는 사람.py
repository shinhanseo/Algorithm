import sys

N = int(sys.stdin.readline())
dic = {}
lst = []
for _ in range(N) :
  name, log = sys.stdin.readline().split()
  dic[name] = log

for key, val in dic.items() :
  if(val == 'enter') :
    lst.append(key)

lst.sort(reverse=True)

for i in lst :
  print(i)