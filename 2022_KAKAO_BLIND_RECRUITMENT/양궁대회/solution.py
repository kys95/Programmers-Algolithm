# from itertools import combinations_with_replacement

# def solution(n, info):
#     answer = []
#     info.reverse()
#     result = 0
#     for data in combinations_with_replacement(range(11), n):

#         temp = [0] * 11
#         score = 0
#         for i in data:
#             temp[i] += 1


#         for i in range(11):
#             if info[i] == 0 and temp[i] == 0:
#                 continue
#             elif temp[i] > info[i]:
#                 score += i

#             else:
#                 score -= i

#         if score > result:
#             temp.reverse()
#             answer = temp
#             result = score
#     if answer:
#         return answer
#     else:
#         return [-1]

from copy import deepcopy

max_diff = 0
answer = []


def dfs(info, shoot, n, i):
    global max_diff, answer
    if i == 11:
        if n != 0:
            shoot[10] = n
        score_diff = calcDiff(info, shoot)
        if score_diff <= 0:
            return
        result = deepcopy(shoot)
        if score_diff > max_diff:
            max_diff = score_diff
            answer = [result]

        if score_diff == max_diff:
            answer.append(result)
        return

    # 점수 먹음
    if info[i] < n:
        shoot.append(info[i] + 1)
        dfs(info, shoot, n - info[i] - 1, i + 1)
        shoot.pop()

    shoot.append(0)
    dfs(info, shoot, n, i + 1)
    shoot.pop()


def calcDiff(info, shoot):
    apeach_score, rion_score = 0, 0
    for i in range(11):
        if info[i] == 0 and shoot[i] == 0:
            continue
        if info[i] >= shoot[i]:
            apeach_score += (10 - i)
        else:
            rion_score += (10 - i)

    return rion_score - apeach_score


def solution(n, info):
    global max_diff, answer
    dfs(info, [], n, 0)

    if answer == []:
        return [-1]
    answer.sort(key=lambda x: x[::-1], reverse=True)
    return answer[0]


# 1. 중복조합, dfs로 풀이할 수 있다.
# 2. 중복조합으로는 10점부터 0점까지(11가지의 경우) 총, 10발의 화살을 쏘는 것이므로 <sub>11</sub>H<sub>10</sub> = 184,756으로 모든
#    경우의 수를 확인하면서 충분히 풀 수 있다.
# 3. dfs로는 10점부터 0점까지 각 점수를 아예 안 맞추거나 어피치보다 1발을 더 맞히는 경우로 각 점수마다 2가지를 완전 탐색하면 된다.
# 4. 만약 1점까지 쏘고도 화살이 남을 경우 남는 화살을 0점에 다 몰아주도록 하여 처리할 수 있다.
# 5. 모든 경우의 수를 살펴보면서 라이언과 어피치의 최대 점수 차이를 구한다.