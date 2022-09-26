from typing import Tuple

moves = [(0, 1), (-1, 0), (1, 0), (0, -1)]


def game(board, aloc, bloc, ) -> Tuple[bool, int]:
    game_results = []

    if board[bloc[0]][bloc[1]] == 0:
        return True, 0
    if board[aloc[0]][aloc[1]] == 0:
        return False, 0

    for move in moves:
        next_aloc = (aloc[0] + move[0], aloc[1] + move[1])
        try:
            if next_aloc[0] < 0 or next_aloc[1] < 0:
                raise IndexError
            next_board = board[next_aloc[0]][next_aloc[1]]
        except IndexError:
            continue

        if next_board == 1:
            board[aloc[0]][aloc[1]] = 0
            win, game_length = game(board, bloc, next_aloc)
            board[aloc[0]][aloc[1]] = 1
            game_results.append((not win, game_length + 1))

    if len(game_results) == 0:
        return False, 0  # 움직일 곳이 없으므로 패배
    elif any(r[0] for r in game_results):
        return True, min(r[1] for r in game_results if r[0])  # 이길 수 있다면 가장 빨리 이기는 쪽으로
    else:
        return False, max(r[1] for r in game_results)  # 이길 수 없다면 가장 오래 버티는 쪽으로


def solution(board, aloc, bloc):
    return game(board, aloc, bloc)[1]


# 1. minmax tree를 사용한다.
# 2. game(board, aloc, bloc) 함수는 두가지 값을 반환 하는데 (Tuple[bool, int])
#   첫번째는 이번 차례에 aloc가 이길 수 있는지 여부
#   두번째는 이길 수 있다면 최소 길이 (가능한 빨리 이기는 쪽) 이길 수 없다면 최대 길이를 반환 한다 (가능한 오래 버티는쪽).
# 3. next_aloc는 aloc가 다음번에 이동할 칸의 위치이고, 이때 game(board, bloc, next_aloc) 반환 값을 이용해 최적의 플레이를 하도록 한다.