def solution(dartResult):
    i = -1
    scores = [0] * 3
    flag = False
    for data in dartResult:
        if data.isdigit():
            if flag == True:
                scores[i] = 10
            else:
                i += 1
                scores[i] = int(data)
            flag = True
            continue


        elif data == 'D':
            scores[i] = scores[i] ** 2
        elif data == 'T':
            scores[i] = scores[i] ** 3
        elif data == '*':
            if i == 0:
                scores[i] = scores[i] * 2
            else:
                scores[i - 1] = scores[i - 1] * 2
                scores[i] = scores[i] * 2

        elif data == '#':
            scores[i] = scores[i] * -1

        flag = False

    return sum(scores)


# 1. 3회차의 다트 게임의 점수를 각각 구해 최종적으로 합한 것을 출력하는 방향으로 하자.
# 2. 다트 게임이 총 3번이므로 scores 배열에 미리 0으로 초기해 놓는다.
# 3. 숫자를 기준으로 다트 게임이 시작되므로 입력값이 숫자인지 아닌지 확인하고 숫자일 경우에 scores 배열에 넣어 갱신한다.
#    단, 10일 경우가 있으므로 flag를 설정하여 숫자가 연속으로 나올 경우 10으로 갱신한다.
# 4. 입력값이 숫자가 아닌경우 주어진 조건대로 구현한다.
# 5. scores의 총합을 최종적으로 출력한다.
