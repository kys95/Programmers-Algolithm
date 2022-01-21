import heapq


def solution(jobs):
    start, end, num = -1, 0, 0
    answer = 0
    heap = []

    while num < len(jobs):
        for job in jobs:
            if start < job[0] <= end:
                heapq.heappush(heap, [job[1], job[0]])
        if len(heap) > 0:
            cost, current = heapq.heappop(heap)
            start = end
            end += cost
            answer += (end - current)
            num += 1
        else:
            end += 1
    return int(answer // len(jobs))