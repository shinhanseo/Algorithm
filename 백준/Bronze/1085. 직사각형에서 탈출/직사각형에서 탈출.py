x, y, w, h = map(int, input().split())
lst = []

lst.append(abs(w-x))
lst.append(abs(y-h))
lst.append(x)
lst.append(y)

print(min(lst))

