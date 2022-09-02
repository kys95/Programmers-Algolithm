def solution(gems):
    n = len(gems)
    kind = len(set(gems))
    answer = [0, n - 1]
    dic = {gems[0]: 1}
    l, r = 0, 0

    while l < n and r < n:
        if len(dic) != kind:
            r += 1
            if r == n:
                break
            dic[gems[r]] = dic.get(gems[r], 0) + 1

        else:
            if (r - l + 1) < (answer[1] - answer[0] + 1):
                answer = [l, r]
            if dic[gems[l]] == 1:
                del dic[gems[l]]
            else:
                dic[gems[l]] -= 1
            l += 1
    answer[0] += 1
    answer[1] += 1

    return answer

# 1. 딕셔너리를 이용해서 dic[보석이름] : 빈도수를 정의한다.
# 2. 왼쪽 포인터 l, 오른쪽 포인터 r을 모두 1번 진열대에 위치시키고 보석 개수를 충족시킬때 까지 r을 오른쪽으로 옮긴다.
# 3. 만일, 보석 개수가 충족된다면 r-l+1 즉, 연장선상의 보석 개수를 비교하여 작다면 갱신해준다. 그리고 l을 오른쪽으로 옮긴다.
# 4. 2~3은 gems의 개수보다 작을때 까지 반복한다.