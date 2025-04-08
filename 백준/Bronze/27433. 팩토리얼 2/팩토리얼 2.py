import sys

def fac(N) :
  if(N<=1) :
    return 1

  return N * fac(N-1) 

N = int(sys.stdin.readline())
print(fac(N))
