def moveBlock(board):
    while True:
        flag = False
        for i in range(len(board) - 1):
            for j in range(len(board[0])):
                if board[i][j] and board[i + 1][j] == []:
                    board[i + 1][j] = board[i][j]
                    board[i][j] = []
                    flag = True

        if flag == False:
            break


def deleteBlock(board):
    visited = set()
    for i in range(len(board) - 1):
        for j in range(len(board[0]) - 1):
            if board[i][j] != []:
                if board[i][j] == board[i][j + 1] == board[i + 1][j] == board[i + 1][j + 1]:
                    visited.add((i, j));
                    visited.add((i, j + 1))
                    visited.add((i + 1, j));
                    visited.add((i + 1, j + 1))

    for x, y in visited:
        board[x][y] = []
    return len(visited)


def solution(m, n, board):
    answer = 0
    for i in range(len(board)):
        board[i] = list(board[i])

    while True:
        cnt = deleteBlock(board)

        if cnt == 0:
            break
        else:
            moveBlock(board)
            answer += cnt

    return answer

# 1. board의 모든 좌표를 탐색하여 2x2형태로 붙은 경우를 있을 때까지 찾는다(최대 30x30이므로 가능) -> 문자열에 접근하기위해 문자를 리스트형태로 치환
# 2. 2x2형태가 붙어있을경우 같이 삭제되므로 중복을 없애기 위해 visited를 set()로 만들어서 해당하는 좌표를 넣어준다.
# 3. 전체를 다 탐색한 후 visited에 있는 좌표들에 빈배열을 넣어주고 visited의 개수를 반환한다.
# 4. 반환값이 0이 아닐 경우 위의 블록부터 아래로 내려준다 -> flag를 두어 전체 블록들이 한번도 옮기지 않을 경우 False, 한번이라도 옮겼으면 True로
#    두어 계속 아래로 내려가게 한다.
# 5. 2x2형태가 붙어있지 않을 때 최종 answer를 반환한다.