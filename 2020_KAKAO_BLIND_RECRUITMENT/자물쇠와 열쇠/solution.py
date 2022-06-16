def rotate(arr):
    m = len(arr)

    result = [[0 for _ in range(m)] for _ in range(m)]
    for i in range(m):
        for j in range(m):
            result[j][m - i - 1] = arr[i][j]
    return result


def check(arr):
    n = len(arr) // 3
    for i in range(n):
        for j in range(n):
            if arr[n + i][n + j] != 1:
                return False
    return True


def solution(key, lock):
    n = len(lock)
    m = len(key)
    new_lock = [[0 for _ in range(3 * n)] for _ in range(3 * n)]
    for i in range(n):
        for j in range(n):
            new_lock[n + i][n + j] = lock[i][j]
    print(new_lock)
    for _ in range(4):
        key = rotate(key)  # 키 회전

        for i in range(2 * n):
            for j in range(2 * n):
                for x in range(m):
                    for y in range(m):
                        new_lock[i + x][j + y] += key[x][y]

                if check(new_lock) == True:
                    return True

                for x in range(m):
                    for y in range(m):
                        new_lock[i + x][j + y] -= key[x][y]

    return False