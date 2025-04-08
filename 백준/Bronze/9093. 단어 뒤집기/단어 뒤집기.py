import sys

n = int(sys.stdin.readline())

for _ in range(n) :
  word = list(sys.stdin.readline().split())
  for i in word :
    re = i[::-1]
    print(re, end=" ")