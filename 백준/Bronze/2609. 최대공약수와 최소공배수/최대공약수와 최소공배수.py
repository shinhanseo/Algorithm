import sys
def gcd(a, b):
  mod = 0
  while b > 0 :
    a, b = b, a % b

  return a

a, b = map(int, sys.stdin.readline().split())
print(gcd(a,b), end=" ")
print((a*b)//gcd(a,b))



