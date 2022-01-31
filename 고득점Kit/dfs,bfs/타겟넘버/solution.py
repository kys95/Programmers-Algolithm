def dfs(idx, number, target, numbers):
    limit = len(numbers)
    if idx == limit:
        if number == target:
            global answer
            answer += 1
        return
    else:
        dfs(idx + 1, number + numbers[idx], target, numbers)
        dfs(idx + 1, number - numbers[idx], target, numbers)


def solution(numbers, target):
    global answer
    answer = 0

    dfs(0, 0, target, numbers)
    return answer