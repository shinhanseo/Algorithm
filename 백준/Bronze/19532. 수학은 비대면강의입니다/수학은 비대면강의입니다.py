def find_xy(lst) :
  a1, b1, c1, a2, b2, c2 = lst
  x = (c1 * b2 - c2 * b1) / (a1 * b2 - a2 * b1)
  y = (a1 * c2 - a2 * c1) / (a1 * b2 - a2 * b1)

  print(f"{int(x)} {int(y)}")

lst = list(map(int, input().split()))
find_xy(lst)