def solution(N, number):
    if N == number:
        return 1
    dp = [set() for _ in range(8)]
    for idx, data in enumerate(dp, start=1):
        data.add(int(str(N) * idx))

    for i in range(1, 8):
        for j in range(i):s
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


# 1. 최솟값이 8보다 크면 -1을 return하므로 1개부터 모든 경우의 수를 구할 수 있다.
# 2. N과 number가 동일하면 그대로 1을 return한다.
# 3. 처음에 집합자료형 set()를 이용하여 1개를 이용,2개를이용 ... 8개를 이용하여 만든 숫자들을 담기위해 dp를 초기화한다.
# 4. 그 다음에 각 횟수마다 N을 이어붙일 수 있는 숫자가 다르므로 N, NN, NNN ...와 같이 숫자를 삽입한다.
# 5. 3개를 이용하여 만들 수 있는 숫자는 dp[0]&dp[1], dp[1]&dp[0]이고 4개를 이용하여 만들 수 있는 숫자들은 dp[0]&dp[2], dp[1]&dp[2],
#    dp[2]&dp[0], dp[2]&dp[1]이므로 인덱스를 이용하여 dp에 저장된 숫자들을 이용한다.
# 6. 만일 x개를 이용하여 number와 동일한 숫자를 만들 수 있다면 answer를 x로 초기화 하고 break한다.
# 7. 만일 8보다 크다면 -1을 return한다.