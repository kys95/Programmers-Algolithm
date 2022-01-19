import heapq

def solution(scoville, K):
    answer = 0
    heap = []
    for food in scoville:
        heapq.heappush(heap, food)

    while len(heap) > 1:
        first = heapq.heappop(heap)
        second = heapq.heappop(heap)
        if first >= K:
            return answer
        new = first + (second * 2)
        answer += 1
        heapq.heappush(heap, new)

    if heapq.heappop(heap) < K:
        return -1
    else:
        return answer