from collections import defaultdict, deque
from itertools import permutations
from copy import deepcopy


def ctrl_move(new_board, r, c, k, t):
    cr, cc = r, c
    while True:
        nr = cr + k
        nc = cc + t
        if not (0 <= nr < 4 and 0 <= nc < 4):
            return cr, cc
        if new_board[nr][nc] != 0:
            return nr, nc
        cr = nr
        cc = nc


def bfs(new_board, start, end):
    r, c = start
    find_r, find_c = end
    queue = deque()
    queue.append((r, c, 0))
    visited = [[0] * 4 for _ in range(4)]
    move = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    while queue:
        r, c, temp = queue.popleft()
        if visited[r][c]: continue
        visited[r][c] = 1
        if r == find_r and c == find_c:
            return temp
        for k, t in move:
            cr = k + r
            cc = c + t
            if 0 <= cr < 4 and 0 <= cc < 4:
                queue.append((cr, cc, temp + 1))
            cr, cc = ctrl_move(new_board, r, c, k, t)
            queue.append((cr, cc, temp + 1))
    return -1


INF = int(1e9)


def solution(board, r, c):
    answer = INF
    location = defaultdict(list)
    nums = []
    for i in range(4):
        for j in range(4):
            if board[i][j] != 0:
                if board[i][j] not in nums: nums.append(board[i][j])
                location[board[i][j]].append((i, j))

    for choices in list(permutations(nums, len(nums))):
        new_board = deepcopy(board)
        cnt = 0
        nr, nc = r, c
        for choice in choices:
            left = bfs(new_board, (nr, nc), location[choice][0])
            right = bfs(new_board, (nr, nc), location[choice][1])

            if left < right:
                cnt += left
                cnt += bfs(new_board, location[choice][0], location[choice][1])
                nr, nc = location[choice][1]
            else:
                cnt += right
                cnt += bfs(new_board, location[choice][1], location[choice][0])
                nr, nc = location[choice][0]

            new_board[location[choice][0][0]][location[choice][0][1]] = 0  # 카드 지우기
            new_board[location[choice][1][0]][location[choice][1][1]] = 0  # 카드 지우기
            cnt += 2  # enter
        answer = min(answer, cnt)

    return answer


# 1. 모든 순열에 대해서 생각해 줘야한다. 1, 2, 3번 카드가 있다면 1-2-3, 1-3-2, 2-1-3, 2-3-1, 3-2-1, 3-1-2 이렇게 모든 순서로 방문하는 비용을 더해줘야 한다.
# 2. 모든 순열에 대해서 고려해주기 위해서 iteratools의 permutation을 사용한다.
# 3. 모든 순열에 대해 돌면서, 순서대로 카드를 지워 나간다.
#  1번 카드를 지우는 최소 비용 = 현재 위치에서 가까운 1번 카드로 이동 + 1번 카드 지우고 + 다른 1번 카드로 이동 + 카드 지우기
# 4. bfs를 이용해 시작 좌표부터 끝 좌표까지 이동하는데 드는 최소 비용을 return하는 함수를 만든다.
