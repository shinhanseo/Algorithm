def solution(k, dungeons):
    answer = 0
    visited = [False] * len(dungeons)

    def dfs(fatigue, count):
        nonlocal answer

        # 지금까지 탐험한 최대 던전 수 저장
        answer = max(answer, count)

        for i in range(len(dungeons)):
            required = dungeons[i][0]  # 최소 필요 피로도
            cost = dungeons[i][1]      # 소모 피로도

            # 방문하지 않았고, 현재 피로도로 입장할 수 있다면
            if not visited[i] and fatigue >= required:
                visited[i] = True

                # 해당 던전을 탐험한 뒤 다음 던전 탐색
                dfs(fatigue - cost, count + 1)

                # 다른 순서를 확인하기 위해 방문 기록 되돌리기
                visited[i] = False

    dfs(k, 0)

    return answer