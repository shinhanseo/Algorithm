num, val = map(int, input().split())
rest = 0
quo = num
result = []

while quo >= val:
    rest = quo % val
    quo = quo // val

    if rest < 10:
        result.append(str(rest))
    else:
        result.append(chr(rest + 55))

# 마지막 나머지를 처리
if quo < 10:
    result.append(str(quo))
else:
    result.append(chr(quo + 55))

# 결과 뒤집기
result.reverse()

# 출력
for i in result:
    print(i, end="")
