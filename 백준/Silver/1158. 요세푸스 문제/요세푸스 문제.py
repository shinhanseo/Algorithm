import sys

def jose(n, k) :
  people = list(range(1, n+1))
  result = []
  idx = 0
  while len(people) > 0 :
    idx = (idx + k -1) % len(people)
    result.append(people.pop(idx))
  return result

N, K = map(int, sys.stdin.readline().split())
lst = jose(N, K)
print("<", end="")
for i in lst :
  if(i != lst[-1]) :
    print(f"{i},", end=" ")
  else :
     print(i, end="")
print(">")






  