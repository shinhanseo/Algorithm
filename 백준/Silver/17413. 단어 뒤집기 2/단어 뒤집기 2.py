import sys

text = sys.stdin.readline().strip()
result = []
stack = []
in_tag = False

for char in text:
    if char == '<':
        # 스택에 모아둔 단어 먼저 뒤집어서 출력
        while stack:
            result.append(stack.pop())
        in_tag = True
        result.append(char)

    elif char == '>':
        in_tag = False
        result.append(char)

    elif in_tag:
        result.append(char)

    elif char == ' ':
        # 단어 경계
        while stack:
            result.append(stack.pop())
        result.append(' ')
        
    else:
        stack.append(char)

# 마지막에 남은 스택 처리
while stack:
    result.append(stack.pop())

print(''.join(result))
