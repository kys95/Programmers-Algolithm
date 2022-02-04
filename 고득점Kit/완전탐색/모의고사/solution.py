# def find(person, answers):
#     cnt = 0     # 각 수포자 별 맞춘 점수
#     for i in range(len(answers)):
#         if answers[i] == person[i % len(person)]:
#             cnt += 1
#     return cnt

# def solution(answers):
#     answer = []
#     people = [[1,2,3,4,5],[2,1,2,3,2,4,2,5],[3,3,1,1,2,2,4,4,5,5]]  # 수포자 3인방
#     std = 1    # 가장 많이 맞춘 점수기준
#     for i in range(len(people)):
#         cnt = find(people[i], answers)
#         if cnt > std:
#             std = cnt
#             answer = [i + 1]
#         elif cnt == std:
#             answer.append(i + 1)
#     return answer


def solution(answers):
    pattern1 = [1,2,3,4,5]
    pattern2 = [2,1,2,3,2,4,2,5]
    pattern3 = [3,3,1,1,2,2,4,4,5,5]
    score = [0, 0, 0]
    result = []

    for idx, answer in enumerate(answers):
        if answer == pattern1[idx%len(pattern1)]:
            score[0] += 1
        if answer == pattern2[idx%len(pattern2)]:
            score[1] += 1
        if answer == pattern3[idx%len(pattern3)]:
            score[2] += 1

    for idx, s in enumerate(score):
        if s == max(score):
            result.append(idx+1)

    return result