# from itertools import permutations

# def solution(k, dungeons):
#     answer = -1

#     choices = list(permutations([x for x in range(len(dungeons))], len(dungeons)))
#     for choice in choices:
#         std = k
#         result = 0
#         for c in choice:
#             if std >= dungeons[c][0]:
#                 std -= dungeons[c][1]
#                 result += 1
#             else:
#                 break
#         answer = max(answer, result)
#     return answer


answer = 0
N = 0
visited = []

def dfs(k, cnt, dungeons):
    global answer
    if cnt > answer:
        answer = cnt

    for j in range(N):
        if k >= dungeons[j][0] and not visited[j]:
            visited[j] = 1
            dfs(k - dungeons[j][1], cnt + 1, dungeons)
            visited[j] = 0


def solution(k, dungeons):
    global N, visited
    N = len(dungeons)
    visited = [0] * N
    dfs(k, 0, dungeons)
    return answer