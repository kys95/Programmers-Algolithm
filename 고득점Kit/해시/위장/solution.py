# def solution(clothes):

#     dic = {}
#     for cloth in clothes:
#         if cloth[1] not in dic:
#             dic[cloth[1]] = 0
#         dic[cloth[1]] += 1

#     answer = 1
#     for i in dic.values():
#         answer *= (i + 1)

#     return answer - 1

def solution(clothes):
    from collections import Counter
    from functools import reduce
    cnt = Counter([kind for name, kind in clothes])

    answer = reduce(lambda x, y: x * (y + 1), cnt.values(), 1) - 1
    return answer