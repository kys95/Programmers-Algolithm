def solution(distance, rocks, n):
    answer = 0
    left, right = 0, distance  # 거리의 최솟값, 최댓값

    rocks.sort()  # 이분탐색하기 위해 오름차순 정렬
    # mid를 각 바위 사이 거리의 최솟값이라고 가정, 각 바위사이 거리를 비교하며 바위 제거,바위 제거횟수가 n보다 크거나 작다면 left, right 조정
    while left <= right:
        mid = (left + right) // 2
        std = 0  # 바위 기준점
        del_rocks = 0  # 제거하는 바위 갯수

        for rock in rocks:
            if rock - std < mid:  # 가정한 거리 최솟값보다 작을 경우 바위 제거
                del_rocks += 1
            else:
                std = rock  # 기준점 변경
            if del_rocks > n:  # 제거한 바위갯수가 n보다 클 경우
                break

        if del_rocks <= n:  # 제거한 바위갯수가 n보다 작거나 같을 경우 가정한 거리의 최솟값이 작은 것으므로 큰 쪽으로 늘린다
            answer = mid
            left = mid + 1
        else:  # 가정한 거리의 최솟값이 큰 값이므로 작은쪽으로 줄인다
            right = mid - 1

    return answer