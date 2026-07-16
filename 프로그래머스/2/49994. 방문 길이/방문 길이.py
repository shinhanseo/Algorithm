def solution(dirs):
    roads = set()
    x, y = 0, 0

    for direction in dirs:
        nx, ny = x, y

        if direction == 'U':
            ny += 1
        elif direction == 'D':
            ny -= 1
        elif direction == 'L':
            nx -= 1
        elif direction == 'R':
            nx += 1

        if not (-5 <= nx <= 5 and -5 <= ny <= 5):
            continue

        roads.add((x, y, nx, ny))
        roads.add((nx, ny, x, y))

        x, y = nx, ny

    return len(roads) // 2