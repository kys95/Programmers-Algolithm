import math

def solution(brown, yellow):
    answer = []

    # 약수 찾기
    for i in range(1, int(math.sqrt(yellow)) + 1):
        if yellow % i == 0:  # 약수
            if brown + yellow == (i + 2) * (yellow // i + 2):
                answer = [yellow // i + 2, i + 2]
                break
    return answer