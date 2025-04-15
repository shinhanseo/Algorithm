import sys

word = sys.stdin.readline().strip()
lst = []
s_lst = []

for i in range(len(word)) :
  lst.append(word[i:])

s_lst = sorted(lst)

for i in s_lst :
  print(i)

