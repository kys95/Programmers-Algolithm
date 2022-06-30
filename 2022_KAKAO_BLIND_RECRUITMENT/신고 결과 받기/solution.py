def solution(id_list, report, k):
    user = dict()
    cnt = dict()
    for id in id_list:
        user[id] = set()
        cnt[id] = 0

    for data in report:
        a, b = data.split()
        if b in user[a]:
            continue
        else:
            user[a].add(b)
            cnt[b] += 1

    answer = []
    for id in id_list:
        result = 0
        for u in user[id]:
            if cnt[u] >= k:
                result += 1
        answer.append(result)

    return answer

# def solution(id_list, report, k):
#     answer = [0] * len(id_list)
#     reports = {x : 0 for x in id_list}

#     for r in set(report):
#         reports[r.split()[1]] += 1

#     for r in set(report):
#         if reports[r.split()[1]] >= k:
#             answer[id_list.index(r.split()[0])] += 1

#     return answer


# def solution(id_list, report, k):
#     answer = {x : 0 for x in id_list}
#     user = {x : 0 for x in id_list}

#     for r in set(report):
#         user[r.split()[1]] += 1

#     for r in set(report):
#         if user[r.split()[1]] >= k:
#             answer[r.split()[0]] += 1

#     result = []
#     for id in id_list:
#         result.append(answer[id])

#     return result