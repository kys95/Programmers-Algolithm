import math
from itertools import permutations

def is_prime_number(x):
    # 2부터 x의 제곱근까지의 모든 수를 확인하며
    for i in range(2, int(math.sqrt(x)) + 1):
        # x가 해당 수로 나누어떨어진다면
        if x % i == 0:
            return False  # 소수가 아님
    return True  # 소수임

def solution(numbers):
    answer = 0
    datas = set()

    for i in range(len(numbers)):
        cases = list((permutations(numbers, i + 1)))
        for case in cases:
            datas.add(int(''.join(case)))

    datas -= set(range(0, 2))  # 0,1이 들어있을 경우 제외

    # 소수 판별
    for data in datas:
        if is_prime_number(data):
            answer += 1

    return answer