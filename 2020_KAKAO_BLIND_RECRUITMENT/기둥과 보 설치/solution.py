def possible(answer):
    for x, y, type in answer:
        if type == 0:  # 기둥
            if y == 0 or (x - 1, y, 1) in answer or (x, y, 1) in answer or (x, y - 1, 0) in answer:
                continue
            return False
        else:  # 보
            if (x, y - 1, 0) in answer or (x + 1, y - 1, 0) in answer or (
                    (x - 1, y, 1) in answer and (x + 1, y, 1) in answer):
                continue
            return False
    return True


def solution(n, build_frame):
    answer = set()
    for frame in build_frame:
        x, y, a, b = frame
        if b == 1:  # 설치
            answer.add((x, y, a))
            if possible(answer) == False:
                answer.remove((x, y, a))
        else:  # 삭제
            answer.remove((x, y, a))
            if possible(answer) == False:
                answer.add((x, y, a))
    answer = list(answer)
    return sorted(answer)