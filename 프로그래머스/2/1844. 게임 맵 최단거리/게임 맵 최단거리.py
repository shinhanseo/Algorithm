from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])

    queue = deque([(0, 0)])

    # 상, 하, 좌, 우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 맵 범위 안이고, 아직 방문하지 않은 길인 경우
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1:
                maps[nx][ny] = maps[x][y] + 1
                queue.append((nx, ny))

    # 목적지에 도달하지 못한 경우
    if maps[n - 1][m - 1] == 1:
        return -1

    return maps[n - 1][m - 1]