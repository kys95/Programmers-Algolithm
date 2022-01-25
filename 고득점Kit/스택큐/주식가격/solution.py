# from collections import deque
# def solution(prices):
#     answer = []
#     queue = deque(prices)
#     while queue:
#         cnt = 0
#         price = queue.popleft()
#         for q in queue:
#             cnt += 1
#             if q < price:   # 가격 떨어짐
#                 break
#         answer.append(cnt)
#     return answer

def solution(prices):
    length = len(prices)

    # answer을 max값으로 초기화
    answer = [i for i in range(length - 1, -1, -1)]

    # 주식 가격이 떨어질 경우 찾기
    stack = [0]
    for i in range(1, length):
        while stack and prices[stack[-1]] > prices[i]:
            j = stack.pop()
            answer[j] = i - j
        stack.append(i)
    return answer