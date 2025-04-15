import sys

word = sys.stdin.readline()
result = []
for i in word :
  if(i.isupper()) :    
    if((ord(i) + 13) > 90) :
      change = chr(ord('A') + (13 - (91-ord(i))))
    else : 
      change =  chr(ord(i) + 13)

  elif(i.islower()) :
    if((ord(i) + 13) > 122) :
      change = chr(ord('a') + (13 - (123-ord(i))))
    else : 
      change =  chr(ord(i) + 13)
  else :
    change = i

  result.append(change)

for i in result :
  print(i, end="")

