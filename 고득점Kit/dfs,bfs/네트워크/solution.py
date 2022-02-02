# def dfs(i,computers,visited,n):
#     visited[i] = True
#     for j in range(n):                  # 연결된 컴퓨터 찾기
#         if i != j and computers[i][j] == 1:
#             if visited[j] == False:
#                 dfs(j,computers,visited,n)

# def solution(n, computers):
#     answer = 0
#     visited = [False] * n

#     for i in range(n):                  # 모든 컴퓨터를 돌면서 연결된 컴퓨터 찾기
#         if visited[i] == False:         # 방문하지 않은 컴퓨터
#             dfs(i,computers,visited,n)
#             answer += 1

#     return answer
from collections import deque


def bfs(i, computers, visited, n):
    queue = deque()
    queue.append(i)

    while queue:
        now = queue.popleft()
        visited[now] = True
        for j in range(n):
            if now != j and computers[now][j] == 1:
                if visited[j] == False:
                    queue.append(j)


def solution(n, computers):
    answer = 0
    visited = [False] * n

    for i in range(n):
        if visited[i] == False:
            bfs(i, computers, visited, n)
            answer += 1
    return answer