import sys

def cal(a, b, o) :
  if o == '+' : return a+b
  elif o =='-' : return a-b
  elif o =='*' : return a*b
  else : return a/b

n = int(sys.stdin.readline())
order = sys.stdin.readline().strip()
num = []
num_dic = {}
stack = []

for _ in range(n) :
  num.append(int(sys.stdin.readline()))

for i, j in zip(range(65, 65+n), num) :
  num_dic[chr(i)] = j

for i in order :
  if i != '+' and i != '-' and i != '*' and i != '/' :
    stack.append(num_dic[i])
  else :
    a = stack.pop(-1)
    b = stack.pop(-1)
    num = cal(b, a, i)
    stack.append(num)

print("%.2f" % stack[0])


