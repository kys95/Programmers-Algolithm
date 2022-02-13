def solution(money):
    # 첫 번째 집 터는 경우(마지막 집은 못털음)
    dp = [0] * (len(money) - 1)
    dp[0] = money[0]
    dp[1] = dp[0]

    for i in range(2, len(money) - 1):
        dp[i] = max(dp[i - 1], dp[i - 2] + money[i])

    answer = dp[-1]

    # 첫 번째 집 안터는 경우
    dp = [0] * len(money)
    dp[1] = money[1]

    for i in range(2, len(money)):
        dp[i] = max(dp[i - 1], dp[i - 2] + money[i])

    answer = max(answer, dp[-1])

    return answer