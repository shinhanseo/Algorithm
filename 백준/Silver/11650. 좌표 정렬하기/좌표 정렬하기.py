import sys

N = int(sys.stdin.readline())  # N 값 입력
lst = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]  # 각 줄의 정수를 리스트로 변환

lst.sort()
for i in range(N) :
  for j in range(2) :
    print(f"{lst[i][j]} ", end="")
  print("")