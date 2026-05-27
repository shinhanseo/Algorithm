def solution(n):
    dp = [0] * (n + 1)
    dp[0] = 1  # 0칸에 도달하는 방법은 1가지 (시작점)
    dp[1] = 1  # 1칸에 도달하는 방법은 1가지

    for i in range(2, n + 1):
        dp[i] = (dp[i-1] + dp[i-2]) % 1234567

    return dp[n]
