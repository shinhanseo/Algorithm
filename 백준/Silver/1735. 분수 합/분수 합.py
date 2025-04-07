import sys
def gcd(b1,b2) : 
  while b2 > 0 :
    b1, b2 = b2, b1 % b2
  
  return b1

def lcd(b1, b2) :
  return (b1*b2) // gcd(b1, b2)

def getA(a, b) :

  while(1) :
    num = gcd(a,b)
    if(num == 1) :
      break
    a = a // num
    b = b // num
  
  print(f"{a} {b}")

a1, b1 = map(int, sys.stdin.readline().split())
a2, b2 = map(int, sys.stdin.readline().split())

b = lcd(b1, b2)
a = a1 * (b//b1) + a2 * (b//b2)

getA(a, b)
