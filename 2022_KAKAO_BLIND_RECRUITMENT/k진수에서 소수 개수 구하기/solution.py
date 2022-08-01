import math


def isPrimeNum(x):
    if x == 1:
        return False

    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


def convert(num, base):
    temp = "0123456789"
    q, r = divmod(num, base)

    if q == 0:
        return temp[r]
    else:
        return convert(q, base) + temp[r]


def solution(n, k):
    answer = 0

    test = convert(n, k)  # k진법으로 바꾼 문자열
    print(test)
    test = test.split('0')
    test = list(filter(None, test))

    for t in test:
        if isPrimeNum(int(t)):
            answer += 1

    return answer

# 1. n을 k진수로 바꾼 후 해당 문자열을 0을 기준으로 나눈후 filter를 통해 빈 문자를 없애준다.
# 2. 해당 숫자가 소수면 카운트를 하고 총 카운트 개수를 출력한다.