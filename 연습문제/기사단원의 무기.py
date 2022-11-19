import math

def getNum(n):
    cnt = 0
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            cnt += 1
            if i * i < n:
                cnt += 1
    return cnt

def solution(number, limit, power):
    answer = 0

    for i in range(1, number + 1):
        result = getNum(i)

        if result <= limit:
            answer += result
        else:
            answer += power
    return answer