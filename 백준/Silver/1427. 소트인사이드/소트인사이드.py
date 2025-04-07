N = input()
len_N = len(N)
lst = []

for i in range(len_N) :
  lst.append(int(N[i]))

lst.sort(reverse=True)

for i in lst :
  print(i, end="")