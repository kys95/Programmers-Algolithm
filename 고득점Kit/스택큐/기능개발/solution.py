# from collections import deque
# import math
# def solution(progresses, speeds):
#     answer = []
#     queue = deque()
#     num = len(progresses)
#     for i in range(num):
#         queue.append(math.ceil((100-progresses[i])/speeds[i]))

#     cnt = 1
#     now = queue.popleft()
#     while queue:
#         next_prog = queue.popleft()
#         if now < next_prog:             # 다음 기능이 더 오래걸림
#             answer.append(cnt)
#             now = next_prog
#             cnt = 1
#         else:
#             cnt += 1
#     if len(progresses) > 1:
#         answer.append(cnt)
#         return answer
#     else:
#         return [1]

from math import ceil


def solution(progresses, speeds):
    daysLeft = list(map(lambda x: (ceil((100 - progresses[x]) / speeds[x])), range(len(progresses))))
    count = 1
    retList = []

    for i in range(len(daysLeft)):
        try:
            if daysLeft[i] < daysLeft[i + 1]:
                retList.append(count)
                count = 1
            else:
                daysLeft[i + 1] = daysLeft[i]
                count += 1
        except IndexError:
            retList.append(count)

    return retList