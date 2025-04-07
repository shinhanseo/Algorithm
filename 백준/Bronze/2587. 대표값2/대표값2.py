lst = []
sum = 0
for i in range(5) :
  lst.append(int(input()))

lst.sort()

for i in lst :
  sum += i
  avg = sum // 5

print(avg)
print(lst[2])