def canFill(row, col):
    for i in range(row):
        if Board[i][col]:
            return False
    return True

def find(row, col, h, w):
    emptyCnt = 0
    lastValue = -1

    for r in range(row, row+h):
        for c in range(col, col+w):
            if Board[r][c] == 0:
                if canFill(r, c) == False:
                    return False
                emptyCnt += 1

                if emptyCnt > 2:
                    return False
            else:
                if lastValue == -1:
                    lastValue = Board[r][c]
                elif lastValue != Board[r][c]:
                    return False
    for r in range(row, row+h):
        for c in range(col, col+w):
            Board[r][c] = 0
    return True

Board = []
def solution(board):
    global Board
    Board = board
    n = len(board)
    answer = 0
    while True:
        cnt = 0
        for i in range(n):
            for j in range(n):
                if i <= n-2 and j <= n-3 and find(i, j, 2, 3):
                    cnt += 1
                elif i <= n-3 and j <= n-2 and find(i, j, 3, 2):
                    cnt += 1
        answer += cnt
        if cnt == 0:
            break
    return answer

# 1.주어진 문제에서 12가지의 블록의 종류가 존재한다. 모두 2x3 또는 3x2 모형으로 표현될 수 있다.
#    따라서 블록판의 모든 행과 열을 2x3 칸 또는 3x2 칸으로 돌면서 해당 블록이 지워질 수 있는지 확인한다.
# 2.모든 행과 열을 지나가면서 3x2, 2x3 모형의 크기로 돌면서 확인하는데 일단 블록을 제거할 수 있으면 count +1 해준다.
#    또한 블록을 제거할 수 있으면 board[row][col]값을 모두 0으로 바꿔줘서 지워버린다.
#    또한 모든 행과 열을 돌고 생성된 count값을 answer에 더해준다.
#    또한 모든 행과 열을 돌고 어떤 블록이 지워진 후에야 다른 블록이 지워질 수 있는 경우가 있으므로 무한 반복문인 while 문을 사용해서 모든 행과열을 계속 돌아준다.
#    또한 모든 행과열을 다 돈 후에 count값 즉, 지울 수 있는 블록의 갯수가 0이라면 더 이상 확인할 필요가 없으므로 break문을 통해서 무한루프문을 빠져나온 후 answer 값을 출력해준다.
#    또한 모든 행과 열을 확인하는 부분에서 <= 의 크기 제한이 있는 이유는 2x3 구간과 3x2 부분을 해당 주어진 블록판의 범위를 넘지 않으면서 확인해야하기 때문이다.
# 3.또한 3x2, 2x3 부분에서 해당 블록을 지울 수 있는지 확인하기 위해서 find, canFill 함수를 사용한다.
#    find 함수를 통해서 일단 3x2 또는 2x3 해당 부분이 블록을 지울 수 있는지 확인한다.
#    일단,  해당 부분이 빈 경우(블록이 안 들어있는 경우) canFill 함수를 통해서 새로운 블록이 내려와서 채워질 수 있는지 확인하고 채워질 수 없다면 블록을 지울 수 없다고 반환한다.
#    또한 새로운 블록을 채울 수 있다면 emptyCnt 를 +1 해준다.
#    하지만 해당 부분을 돌면서 emptyCnt가 2를 넘으면 False를 반환한다.
#    왜냐하면 해당 블록을 새로 채워서 지우기 위해서는 2칸의 새로운 블록이 필요하기 때문이다.
# 4.canFill 함수를 통해서 해당 칸에 새로운 블록이 위에서 부터 내려와서 쌓아질 수 있을 지 확인한다.