from itertools import permutations

def check(choice, banned_id):
    for i in range(len(banned_id)):
        if len(choice[i]) != len(banned_id[i]):
            return False
        for j in range(len(banned_id[i])):
            if banned_id[i][j] == '*':
                continue
            elif banned_id[i][j] == choice[i][j]:
                continue
            else:
                return False
    return True


def solution(user_id, banned_id):
    answer = []

    for choice in permutations(user_id, len(banned_id)):
        if check(choice, banned_id):
            if set(choice) not in answer:
                answer.append(set(choice))

    return len(answer)


# 1. 응모자 크기가 8이하이므로 완전탐색을 사용할 수 있다.
# 2. permutations를 사용해 ban 리스트길이만큼 경우의 수를 뽑는다
# 3-1. 각 경우의 수를 일대일 비교한다.
# 3-2. 해당되면 answer에 있으면 넘어가고 없으면 그 경우의 수를 넣는다.
# 4. answer의 길이를 반환한다.