num = int(input())
x_lst = []
y_lst = []

for i in range(num) :
  x, y = map(int, input().split())
  x_lst.append(x)
  y_lst.append(y)

area = (max(x_lst) - min(x_lst)) * (max(y_lst) - min(y_lst))

print(area)