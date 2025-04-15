import sys

c = sys.stdin.readline().strip()
word = [0] * 26

for i in c :
  word[ord(i)-97] += 1

print(*word)