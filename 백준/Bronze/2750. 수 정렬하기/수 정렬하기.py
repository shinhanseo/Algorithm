num = int(input())
lst = []
for i in range(num) :
  lst.append(int(input()))

lst.sort()

for i in lst :
  print(i)