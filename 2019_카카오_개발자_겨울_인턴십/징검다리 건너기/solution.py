def solution(stones, k):
    l, r = 1, 200000000
    while l <= r:
        mid = (l + r) // 2
        cnt = 0
        for stone in stones:
            if stone - mid <= 0:
                cnt += 1
            else:
                cnt = 0
            if cnt >= k:
                break
        if cnt >= k:
            r = mid - 1
        else:
            l = mid + 1

    return l


# 1. 완전탐색을 이용할 경우 시간초과 -> stones 배열 각 원소들의 값은 1 이상 200,000,000 이하인 자연수이기 때문이다.
# 2. 징검다리를 건널 수 있는 친구들의 최솟값과 최댓값 1, 200,000,000를 l, r로 설정한다. -> 이분탐색
# 3. l이 r이하일 때까지 반복하여 중간값 mid를 활용하여 stones의 원소를 탐색한다.
# 3-1. 각 원소에서 mid를 빼어 0이하이면 cnt+1하고 이상이면 0으로 초기화한다.
# 3-2. 만일 cnt가 k이상일 경우 break를 통해 나오고 r을 mid - 1로 갱신한다. -> 친구들의 수를 줄여야 하기 때문
# 3-3. cnt가 k보다 작을 경우, 친구들의 수를 늘려야 하기 때문에 l을 mid + 1로 갱신한다.
# 4. 최종 l을 리턴한다.