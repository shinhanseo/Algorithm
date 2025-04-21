import sys

input = sys.stdin.readline

N, M = map(int, input().split())
num_lst = list(map(int, input().split()))

# 누적 합 배열 생성 (인덱스 0은 0으로 두고 시작)
prefix_sum = [0] * (N + 1)
for i in range(1, N + 1):
    prefix_sum[i] = prefix_sum[i - 1] + num_lst[i - 1]

# 구간 합 출력
for _ in range(M):
    i, j = map(int, input().split())
    print(prefix_sum[j] - prefix_sum[i - 1])
