while(1) :
  num = int(input())
  lst = []
  sum = 0

  if(num == -1) : 
    break

  for i in range(1,num) :
    if(num % i == 0) :
      lst.append(i)
      sum += i

  if(sum == num) :
    print(f"{num} =", end="")
    for i in lst :
      if(lst[-1] == i) :
        print(f" {i}", end="")
      else :
        print(f" {i} +", end="")
    
    print("")

  else :
    print(f"{num} is NOT perfect.")
  
