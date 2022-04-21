# from copy import deepcopy
# from itertools import permutations

# def calc(array, choice):
#     arr = deepcopy(array)

#     for op in choice:
#         stack = []
#         while len(arr) != 0:
#             tmp = arr.pop(0)

#             if tmp == op:
#                 stack.append(str(eval(stack.pop() + op + arr.pop(0))))
#             else:
#                 stack.append(tmp)
#         arr = stack

#     return abs(int(arr[0]))

# def solution(expression):
#     answer = 0

#     choices = list(permutations(['+','-','*']))

#     exp = ''
#     array = []
#     for data in expression:
#         if data.isdigit():
#             exp += data

#         else:
#             array.append(exp)
#             array.append(data)
#             exp = ''
#     array.append(exp)


#     for choice in choices:
#         answer = max(answer, calc(array, choice))

#     return answer

# import re
# from itertools import permutations

# def solution(expression):
#     #1
#     op = [x for x in ['*','+','-'] if x in expression]
#     op = [list(y) for y in permutations(op)]
#     ex = re.split(r'(\D)',expression)

#     print('op',op, 'ex', ex)

#     #2
#     result = 0
#     for x in op:
#         _ex = ex[:]
#         for y in x:
#             while y in _ex:
#                 tmp = _ex.index(y)
#                 _ex[tmp-1] = str(eval(_ex[tmp-1]+_ex[tmp]+_ex[tmp+1]))
#                 _ex = _ex[:tmp]+_ex[tmp+2:]

#         print("_ex[-1]", _ex[-1])
#         result = max(result, abs(int(_ex[0])))
#         print("_ex", _ex, "ex", ex)

#     #3
#     return result


from itertools import permutations


def calc(priority, n, expression):
    if n == 2:
        return str(eval(expression))
    if priority[n] == '*':
        res = eval('*'.join([calc(priority, n + 1, e) for e in expression.split('*')]))

    if priority[n] == '+':
        res = eval('+'.join([calc(priority, n + 1, e) for e in expression.split('+')]))
    if priority[n] == '-':
        res = eval('-'.join([calc(priority, n + 1, e) for e in expression.split('-')]))
    return str(res)


def solution(expression):
    answer = 0
    priorities = (list(permutations(['*', '-', '+'], 3)))
    for priority in priorities:
        res = int(calc(priority, 0, expression))
        answer = max(answer, abs(res))

    return answer