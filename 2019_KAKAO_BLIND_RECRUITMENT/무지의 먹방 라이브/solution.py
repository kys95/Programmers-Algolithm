import heapq


def solution(food_times, k):
    if sum(food_times) <= k:
        return -1

    q = []
    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i + 1))

    previous = 0
    total = 0

    n = len(food_times)
    while total + (q[0][0] - previous) * n <= k:
        now = heapq.heappop(q)[0]
        total += (now - previous) * n
        n -= 1
        previous = now

    result = sorted(q, key=lambda x: x[1])

    return result[(k - total) % n][1]