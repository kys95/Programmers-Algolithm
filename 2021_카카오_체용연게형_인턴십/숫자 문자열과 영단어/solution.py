def solution(s):
    answer = ""

    nums = {"zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8,
            "nine": 9}
    std = ""

    for x in s:

        if std in nums:
            answer += str(nums[std])
            std = ""

        if x.isdigit():  # 숫자라면
            answer += x

        else:  # 문자라면

            std += x

    if std:
        answer += str(nums[std])

    return int(answer)