import sys

def fac(N) :
  result = 1
  for i in range(1, N+1) :
    result *= i

  return result

N, K = map(int, sys.stdin.readline().split())

print(fac(N) // (fac(N-K) * fac(K)))

