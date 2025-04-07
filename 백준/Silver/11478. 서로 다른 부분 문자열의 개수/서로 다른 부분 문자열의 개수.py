import sys

S = sys.stdin.readline().strip()
rangenum = len(S)
jnum = 1
s = set()

for i in range(rangenum) :
  for j in range(jnum, len(S)+1) :
     s.add(S[i:j])
  jnum += 1

print(len(list(s)))