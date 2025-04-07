import sys

N = int(sys.stdin.readline())
lst = [int(sys.stdin.readline()) for _ in range(N)]

# 평균 계산
avg = round(sum(lst) / N)

# 중앙값
s_lst = sorted(lst)
mid = s_lst[N // 2]

# 최빈값 계산
dic = {}
max_lst = []
max_num = 0

for i in lst:
    dic[i] = dic.get(i, 0) + 1

for key, val in dic.items():
    if val > max_num:
        max_num = val
        max_lst = [key]
    elif val == max_num:
        max_lst.append(key)

max_lst.sort()
mode = max_lst[0] if len(max_lst) == 1 else max_lst[1]

# 범위
range_val = max(lst) - min(lst)

# 출력
print(avg)
print(mid)
print(mode)
print(range_val)
