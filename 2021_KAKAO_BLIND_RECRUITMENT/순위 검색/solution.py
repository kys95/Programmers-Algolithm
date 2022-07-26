from itertools import combinations
from bisect import bisect_left


def solution(info, query):
    answer = []
    info_dic = {}

    for i in range(len(info)):
        info_data = info[i].split()
        info_key = info_data[:-1]  # info 조건
        info_val = info_data[-1]  # info 점수

        for n in range(5):
            for c in combinations(info_key, n):
                temp = ''.join(c)
                if temp in info_dic:
                    info_dic[temp].append(int(info_val))
                else:
                    info_dic[temp] = [int(info_val)]

    for k in info_dic:
        info_dic[k].sort()

    for i in range(len(query)):
        query_data = query[i].split()
        query_key = query_data[:-1]
        query_val = query_data[-1]

        while 'and' in query_key:
            query_key.remove('and')
        while '-' in query_key:
            query_key.remove('-')
        query_key = ''.join(query_key)

        if query_key in info_dic:
            num = bisect_left(info_dic[query_key], int(query_val))
            answer.append(len(info_dic[query_key]) - num)

        else:
            answer.append(0)

    return answer

1. query의 정보에 따라 info와 일대일 비교를 하면 효율성에서 시간초과가 난다! -> 완전탐색이 아닌 다른 방법을 이용하자!
2. query의 '-'를 고려하여 주어진 info에서 만들 수 있는 조합을 모두 생각한다. ex) java, javabackend, backend...
3. 점수를 제외한 나머지 조건들(언어,직군,경력,소울푸드)을 key, 점수를 value로 하여 모든 조합을 구하고 딕셔너리형 info_dic를 만든다.
4. 해당 키를 가진 점수들을 오름차순 정렬한다.
5. query에서 'and'와 '-'를 제외한 문자열을 합쳐 키로 삼아 해당 키가 info_dic에 없으면 0을, 있다면 이진탐색을 통해 개수를 파악하여 해당
   개수를 answer에 담는다.
6. 최종적으로 answer를 반환한다.