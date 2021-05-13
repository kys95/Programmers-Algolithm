from collections import deque
# 로봇다음 위치확인
def get_next_pos(board, pos):
    # 현재 위치를 리스트형으로 변환
    now = list(pos)
    # 두 쌍의 x,y좌표
    now1_x = now[0][0]
    now1_y = now[0][1]
    now2_x = now[1][0]
    now2_y = now[1][1]
    # 다음 위치 반환 리스트
    next = []
    # 상, 하, 좌, 우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for i in range(4):
        nx_1 = now1_x + dx[i]
        ny_1 = now1_y + dy[i]
        nx_2 = now2_x + dx[i]
        ny_2 = now2_y + dy[i]
        # 이동하고자 하는 위치가 모두 비어있다면
        if board[nx_1][ny_1] == 0 and board[nx_2][ny_2] == 0:
            next.append({(nx_1, ny_1), (nx_2, ny_2)})

            # 로봇이 가로로 놓여 있다면
    if now1_x == now2_x:
        for i in [-1, 1]:
            if board[now1_x + i][now1_y] == 0 and board[now2_x + i][now2_y] == 0:
                next.append({(now1_x, now1_y), (now1_x + i, now1_y)})
                next.append({(now2_x, now2_y), (now2_x + i, now2_y)})
    # 현재 로봇이 세로로 있다면
    elif now1_y == now2_y:
        for i in [-1, 1]:
            if board[now1_x][now1_y + i] == 0 and board[now2_x][now2_y + i] == 0:
                next.append({(now1_x, now1_y), (now1_x, now1_y + i)})
                next.append({(now2_x, now2_y), (now2_x, now2_y + i)})
    return next


def solution(board):
    n = len(board)
    # 경계조건 확인 편하게 하기 위해 새로운 보드 생성
    new_board = [[1] * (n + 2) for _ in range(n + 2)]
    for i in range(n):
        for j in range(n):
            new_board[i + 1][j + 1] = board[i][j]
    # bfs 알고리즘
    q = deque()
    # 로봇 초기위치 초기화
    pos = {(1, 1), (1, 2)}
    # 방문리스트
    visited = []
    visited.append(pos)
    # 로봇이동 비용
    cost = 0
    q.append((pos, cost))

    while q:
        pos, cost = q.popleft()
        # 목적지 도착
        if (n, n) in pos:
            return cost
        # 현재의 위치에서 다음 위치로 갈 수 있는 경우
        for next_pos in get_next_pos(new_board, pos):
            # 방문하지 않은 경우
            if next_pos not in visited:
                q.append((next_pos, cost + 1))
                # 방문처리
                visited.append(next_pos)