import sys
def gcd(a,b) :
  while b > 0 :
    a, b = b, a % b
  return a

N = int(sys.stdin.readline())
tree = []
tree_dif = []
sum = 0

for _ in range(N) :
  tree.append(int(sys.stdin.readline()))

for i in range(len(tree) - 1) :
  tree_dif.append(tree[i+1]-tree[i])

num = gcd(tree_dif[0], tree_dif[1])
for i in range(2, len(tree_dif)) :
  num = gcd(num, tree_dif[i])

for i in range(len(tree_dif)) :
  sum += (tree_dif[i] // num) - 1

print(sum)
  
