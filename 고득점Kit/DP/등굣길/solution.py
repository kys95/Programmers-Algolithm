# def solution(m, n, puddles):
#     dp = [[1] * m for _ in range(n)]      #1로 초기화

#     for x, y in puddles:
#         dp[y - 1][x - 1] = 0     #우물인 곳은 0으로

#     for i in range(n):
#         for j in range(m):
#             if dp[i][j] == 0:   #우물
#                 continue

#             if i == 0 and j == 0:
#                 continue

#             if i == 0:          #위쪽벽
#                 if dp[i][j - 1] == 0:
#                     dp[i][j] = 0
#                     continue

#             elif j == 0:        #왼쪽벽
#                 if dp[i - 1][j] == 0:
#                     dp[i][j] = 0
#                     continue

#             elif dp[i - 1][j] == 0 and dp[i][j - 1] == 0: #왼쪽&위쪽이 우물
#                 dp[i][j] = 0
#                 continue

#             elif dp[i - 1][j] == 0: #위쪽만 우물
#                 dp[i][j] = dp[i][j - 1]
#                 continue

#             elif dp[i][j - 1] == 0: #왼쪽만 우물
#                 dp[i][j] = dp[i - 1][j]
#                 continue

#             else:
#                 dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
#                 continue

#     return dp[n - 1][m - 1] % 1000000007

# def solution(m, n, puddles):
#     dp = [[0] * (m + 1) for _ in range(n + 1)]

#     if puddles != [[]]:
#         for x, y in puddles:    #웅덩이
#             dp[y][x] = -1

#     dp[1][1] = 1                #집

#     for i in range(1, n + 1):
#         for j in range(1, m + 1):

#             if i == 1 and j == 1: #집은 무조건 1
#                 continue
#             if dp[i][j] == -1:    #웅덩이인 곳은 0으로
#                 dp[i][j] = 0
#                 continue
#             dp[i][j] = (dp[i - 1][j] + dp[i][j - 1]) % 1000000007

#     return dp[n][m]

def solution(m, n, puddles):
    info = dict([((2, 1), 1), ((1, 2), 1)])
    for puddle in puddles:
        info[tuple(puddle)] = 0

    def func(m, n):
        if m < 1 or n < 1:
            return 0
        if (m, n) in info:
            return info[(m, n)]
        return info.setdefault((m, n), func(m - 1, n) + func(m, n - 1))

    return func(m, n) % 1000000007