from collections import deque
def solution(board):
    INF = int(1e9)
    n = len(board)
    answer = INF
    dd=[0, 1, 2, 3]
    dy=[0, 1, 0, -1]
    dx=[1, 0, -1, 0]
    dist=[[[INF for _ in range(len(board[0]))] for _ in range(len(board))] for _ in range(4)]
    q=deque()
    q.append([0, 0, 0, 0])
    q.append([0, 0, 0, 1])
    while q:
        y, x, cost, d=q.popleft()
        for i in range(4):
            ny=y+dy[i]
            nx=x+dx[i]
            if 0<=ny<n and 0<=nx<n and board[ny][nx]==0:
                n_cost=cost+1
                if d!=dd[i]:
                    n_cost+=5
                if dist[dd[i]][ny][nx]>n_cost:
                    dist[dd[i]][ny][nx]=n_cost
                    if ny==n-1 and nx==n-1:
                        continue
                    q.append([ny, nx, n_cost, dd[i]])
    for i in range(4):
        answer=min(answer, dist[i][n-1][n-1])
    answer*=100
    return answer


# 1. 3차원 리스트를 사용하여 마지막 인덱스에 방향을 저장하여 처리한다. 방향을 0은 오른쪽, 1은 아래쪽, 2는 왼쪽, 3은 위쪽으로 설정한다.
# 2. BFS+DP를 통하여 매 반복마다 비용을 1씩 증가시키고, 만약 추출한 d와 다음에 올 d가 다를 경우 5를 더 증가시켜준다.
# 3. 이 과정을 끝내면 dist에 모든 인덱스까지의 비용이 저장되는데 [n-1][n-1]에 해당하는 최솟값을 찾아 100을 곱하여 반환한다.