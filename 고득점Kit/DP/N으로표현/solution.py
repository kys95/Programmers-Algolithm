def solution(N, number):
    if N == number:
        return 1
    dp = [set() for _ in range(8)]
    for idx, data in enumerate(dp, start=1):
        data.add(int(str(N) * idx))

    for i in range(1, 8):
        for j in range(i):
            for num1 in dp[j]:
                for num2 in dp[i - j - 1]:
                    dp[i].add(num1 + num2)
                    dp[i].add(num1 - num2)
                    dp[i].add(num1 * num2)
                    if num2 != 0:
                        dp[i].add(num1 // num2)

        if number in dp[i]:
            answer = i + 1
            break

    else:
        answer = -1

    return answer