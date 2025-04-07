num = int(input())

def is_prime(num) :
  state = 0
  if(num == 2) :
    return True
  else :
    for i in range(2, num) :
      if(num % i == 0) :
        state = 1
    
    if(state == 1) :
      return False 
    else :
      return True
  
def get_minprime(num) :
  lst = []
  for i in range(2, num+1) :
    if(num % i == 0) :
      if(is_prime(i)) :
        lst.append(i)
      else :
        continue

  return min(lst)

while(1) :
  if(num == 1):
    break
  else :    
    if(is_prime(num) == False) :
      min_prime = get_minprime(num)
      print(f"{min_prime}")
      num //= min_prime
    else :
      print(f"{num}")
      break
  