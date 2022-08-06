from itertools import combinations


def solution(relation):
    answer = 0
    row = len(relation)
    col = len(relation[0])

    combi = []
    for i in range(1, col + 1):
        combi.extend(combinations(range(col), i))

    unique = []
    for c in combi:

        tmp = set(tuple(r[i] for i in c) for r in relation)

        if len(tmp) == row:
            flag = True

            for x in unique:
                if set(x).issubset(set(c)):
                    flag = False
                    break

            if flag:
                unique.append(c)
                answer += 1

    return answer

# 1. combinations를 이용하여 columns의 가능한 모든 인덱스 조합을 구한다.
# 2. 조합을 대상으로 유일성을 검사 -> 최소성을 검사해서 나온 값들을 unique 리스트에 넣어 길이를 출력한다.
# 3. 유일성을 검사하는 아이디어는 조합의 인덱스 조합을 릴레이션 item에 해당하는 속성 값을 추출해서 tuple에 담아 리스트로 모아둔 값이 row의
#    길이와 같은지 체크한다.(중복성 체크)
# 4. 최소성을 검사하는 아이디어는 유일성을 검사하고 나온 튜플 set들을 set의 부분집합인지 찾는 메소드인 issubset()을 사용해서 아닌 경우들만
#    unique 리스트에 넣는다.
