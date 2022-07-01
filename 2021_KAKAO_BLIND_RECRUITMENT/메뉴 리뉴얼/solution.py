from itertools import combinations

def solution(orders, course):
    answer = []
    for k in course:
        candidates = {}
        for menu_li in orders:
            for li in combinations(menu_li, k):
                res = ''.join(sorted(li))
                if res in candidates:
                    candidates[res] += 1
                else:
                    candidates[res] = 1
        candidates2 = sorted(candidates.items(), key=lambda x: x[1], reverse=True)
        for i in range(len(candidates2)):
            if i == 0:
                if candidates2[i][1] >= 2:
                    answer.append(candidates2[i][0])
                else:
                    break
            else:
                if candidates2[i][1] >= 2 and candidates2[i][1] == candidates2[i - 1][1]:
                    answer.append(candidates2[i][0])
                else:
                    break

    return sorted(answer)

# from itertools import combinations
# from collections import Counter
# def solution(orders, course):
#     answer = []
#     for k in course:
#         candidates = []
#         for menu_li in orders:
#             for li in combinations(menu_li, k):
#                 res = ''.join(sorted(li))
#                 candidates.append(res)
#         sorted_candidates = Counter(candidates).most_common()
#         answer += [menu for menu, cnt in sorted_candidates if cnt > 1 and cnt == sorted_candidates[0][1]]
#     return sorted(answer)