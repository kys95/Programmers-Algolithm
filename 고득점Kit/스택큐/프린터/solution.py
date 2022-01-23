from collections import deque


# import heapq
# def solution(priorities, location):

#     maxHeap = []
#     queue = deque()
#     for idx, priority in enumerate(priorities):
#         queue.append((idx, priority))
#         heapq.heappush(maxHeap,-priority)              # 최대힙 이용
#     cnt = 1
#     while True:
#         nowIdx, nowPri = queue.popleft()
#         std = -heapq.heappop(maxHeap)                  # 기준 = 최댓값

#         if nowPri == std:
#             if nowIdx == location:
#                 return cnt
#             cnt += 1

#         else:
#             queue.append((nowIdx, nowPri))
#             heapq.heappush(maxHeap,-std)


def solution(priorities, location):
    queue = deque()
    for idx, priority in enumerate(priorities):
        queue.append((idx, priority))
    answer = 0
    while True:
        cur = queue.popleft()
        if any(cur[1] < q[1] for q in queue):
            queue.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer