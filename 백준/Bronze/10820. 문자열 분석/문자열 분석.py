import sys

for line in sys.stdin:
    up = 0
    down = 0
    num = 0
    gap = 0

    for i in line.rstrip('\n'):
        if i.isupper():
            up += 1
        elif i.islower():
            down += 1
        elif i.isdigit():
            num += 1
        elif i == ' ':
            gap += 1

    print(f"{down} {up} {num} {gap}")
