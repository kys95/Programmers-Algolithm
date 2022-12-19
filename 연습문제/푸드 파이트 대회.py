from itertools import chain
def solution(food):
    stack = []
    for i in range(1, len(food)):
        for _ in range(food[i] // 2):
            stack.append(i)
    return ''.join(map(str, chain(stack, [0], stack[::-1])))