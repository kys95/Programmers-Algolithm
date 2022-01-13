def solution(array, commands):
    answer = []
    for i,j,k in commands:
        data = array[i-1:j]
        data.sort()
        answer.append(data[k-1])
    return answer