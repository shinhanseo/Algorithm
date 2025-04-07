while(1) :
  lst = []
  sum = 0
  a, b, c = map(int , input().split())

  if(a==0 and b==0 and c==0) :
    break

  lst.append(a)
  lst.append(b)
  lst.append(c)

  max = 0
  max_len  = a

  for i in lst :
    sum += i
    if(max < lst.count(i)) :
      max = lst.count(i)
    if(max_len < i) :
      max_len = i
  
  sum -= max_len

  if(max_len < sum):
    if(max == 1) :
      print("Scalene")
    elif(max == 2) :
      print("Isosceles")
    else :
      print("Equilateral")
  else :
    print("Invalid")

           
