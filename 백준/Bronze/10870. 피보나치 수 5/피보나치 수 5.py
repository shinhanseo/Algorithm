import sys

def pibo(n) :
  if(n==0) :
    return 0
  elif(n==1) :
    return 1
  
  return pibo(n-1) + pibo(n-2)

N = int(sys.stdin.readline())
print(pibo(N))


