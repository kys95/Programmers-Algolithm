from collections import Counter


def solution(nums):
    answer = 0
    counter = Counter(nums)

    return len(counter) if len(nums) // 2 >= len(counter) else len(nums) // 2