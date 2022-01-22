import heapq
def solution(operations):
    min_heap = []
    max_heap = []
    cnt = 0
    for operation in operations:
        oper, num = operation.split()
        if oper == 'I':     # 삽입
            heapq.heappush(min_heap,int(num))
            heapq.heappush(max_heap,-int(num))
            cnt += 1
        else:               # 삭제
            if cnt == 0:
                continue
            else:
                if '-' in num:  # 최솟값 삭제
                    heapq.heappop(min_heap)
                else:
                    heapq.heappop(max_heap)
                cnt -= 1
                if cnt == 0:
                    min_heap = []
                    max_heap = []

    return [-heapq.heappop(max_heap),heapq.heappop(min_heap)] if cnt > 0 else [0,0]