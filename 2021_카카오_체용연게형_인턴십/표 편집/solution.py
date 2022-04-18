def solution(n, k, cmd):
    cur = k
    answer = ['O'] * n
    origin = {i: [i - 1, i + 1] for i in range(n)}
    origin[0][0] = None
    origin[n - 1][1] = None
    stack = []

    for data in cmd:
        if data == 'C':  # 현재 행 삭제
            answer[cur] = 'X'
            prev, next = origin[cur][0], origin[cur][1]
            stack.append((prev, cur, next))

            # 현재 행이 가장 마지막행일 경우
            if next == None:
                cur = origin[cur][0]
                origin[cur][1] = None

            else:
                cur = origin[cur][1]
                if prev == None:  # 현재 행이 가장 첫 행
                    origin[cur][0] = None
                else:
                    origin[prev][1] = next
                    origin[next][0] = prev

        elif data == 'Z':  # 최근 삭제된 행 복구
            prev, now, next = stack.pop()
            answer[now] = 'O'

            if prev == None:
                origin[next][0] = now
            elif next == None:
                origin[prev][1] = now
            else:
                origin[prev][1] = now
                origin[next][0] = now

        else:
            a, b = data.split()
            b = int(b)

            if a == 'U':  # 위
                for _ in range(b):
                    cur = origin[cur][0]

            else:
                for _ in range(b):
                    cur = origin[cur][1]

    return ''.join(answer)