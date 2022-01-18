import heapq


def solution(routes):
    heap = []
    for route in routes:
        heapq.heappush(heap, route)
    start, end = heapq.heappop(heap)
    answer = 1
    while heap:
        bf, af = heapq.heappop(heap)
        if start <= bf <= end:
            start = bf
            if end > af:
                end = af
        else:
            start, end = bf, af
            answer += 1
    return answer

# def solution(routes):
#     routes = sorted(routes, key=lambda x: x[1])
#     last_camera = -30001
#
#     answer = 0
# 
#     for route in routes:
#         if last_camera < route[0]:
#             answer += 1
#             last_camera = route[1]
#
#     return answer