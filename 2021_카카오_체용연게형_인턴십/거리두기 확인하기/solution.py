from collections import deque
def bfs(room, x, y, dis):
    queue = deque()
    queue.append((x, y, dis))

    visited = [[False for _ in range(5)] for _ in range(5)]

    while queue:

        x, y, cnt = queue.popleft()
        if cnt >= 2:
            return True
        visited[x][y] = True
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < 5 and 0 <= ny < 5 and visited[nx][ny] == False:

                if room[nx][ny] == 'P':
                    return False

                elif room[nx][ny] == 'X':
                    continue

                else:
                    visited[nx][ny] = True
                    queue.append((nx, ny, cnt + 1))

    return True


def solution(places):
    answer = []

    for room in places:
        flag = True
        for i in range(5):
            if flag == False:
                break
            for j in range(5):
                if room[i][j] == 'P':
                    if bfs(room, i, j, 0) == False:
                        answer.append(0)
                        flag = False
                        break

        if flag == True:
            answer.append(1)

    return answer

# from collections import deque

# def bfs(p):
#     start = []

#     for i in range(5): # 시작점이 되는 P 좌표 구하기
#         for j in range(5):
#             if p[i][j] == 'P':
#                 start.append([i, j])

#     for s in start:
#         queue = deque([s])  # 큐에 초기값
#         visited = [[0]*5 for i in range(5)]   # 방문 처리 리스트
#         distance = [[0]*5 for i in range(5)]  # 경로 길이 리스트
#         visited[s[0]][s[1]] = 1

#         while queue:
#             y, x = queue.popleft()

#             dx = [-1, 1, 0, 0]  # 좌우
#             dy = [0, 0, -1, 1]  # 상하

#             for i in range(4):
#                 nx = x + dx[i]
#                 ny = y + dy[i]

#                 if 0<=nx<5 and 0<=ny<5 and visited[ny][nx] == 0:

#                     if p[ny][nx] == 'O':
#                         queue.append([ny, nx])
#                         visited[ny][nx] = 1
#                         distance[ny][nx] = distance[y][x] + 1

#                     if p[ny][nx] == 'P' and distance[y][x] <= 1:
#                         return 0
#     return 1


# def solution(places):
#     answer = []

#     for i in places:
#         answer.append(bfs(i))

#     return answer


# def check(place):
#     for irow, row in enumerate(place):
#         print(irow, row)
#         for icol, cell in enumerate(row):
#             if cell != 'P':
#                 continue
#             if irow != 4 and place[irow + 1][icol] == 'P':
#                 return 0
#             if icol != 4 and place[irow][icol + 1] == 'P':
#                 return 0
#             if irow < 3 and place[irow + 2][icol] == 'P' and place[irow + 1][icol] != 'X':
#                 return 0
#             if icol < 3 and place[irow][icol + 2] == 'P' and place[irow][icol + 1] != 'X':
#                 return 0
#             if irow != 4 and icol != 4 and place[irow + 1][icol + 1] == 'P' and (place[irow + 1][icol] != 'X' or place[irow][icol + 1] != 'X'):
#                 return 0
#             if irow != 4 and icol != 0 and place[irow + 1][icol - 1] == 'P' and (place[irow + 1][icol] != 'X' or place[irow][icol - 1] != 'X'):
#                 return 0
#     return 1

# def solution(places):
#     return [check(place) for place in places]