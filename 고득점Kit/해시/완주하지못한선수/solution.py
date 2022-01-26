# def solution(participant, completion):
#     participant.sort()
#     completion.sort()

#     for i in range(len(completion)):
#         if participant[i] != completion[i]:
#             return participant[i]

#     return participant[-1]

# def solution(participant, completion):
#     answer = ''
#     temp = 0
#     dic = {}
#     for part in participant:
#         dic[hash(part)] = part

#         temp += hash(part)
#     for com in completion:
#         temp -= hash(com)
#     answer = dic[temp]

#     return answer

from collections import Counter


def solution(participant, completion):
    answer = Counter(participant) - Counter(completion)
    return list(answer.keys())[0]