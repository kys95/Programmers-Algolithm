def solution(n, times):
    answer = 0  # 모든 사람이 심사받는데 걸리는 최소의 시간
    left = 1
    right = max(times) * n  # 심사받는 최소시간, 최대시간

    while left <= right:
        mid = (left + right) // 2
        people = 0  # 심사한 사람 수
        for time in times:
            people += (mid // time)

            if people >= n:  # 심사한 사람의 수가 심사받아야 할 수보다 같거나 많은 경우
                break

        if people >= n:  # 심사한 사람 수가 심사받아야 할 사람보다 같거나 큰 경우
            answer = mid
            right = mid - 1

        else:  # 심사한 사람 수가 심사받아야 할 사람보다 적은 경우
            left = mid + 1

    return answer