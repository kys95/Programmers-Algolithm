def solution(k, score):
    result = []
    honor = []
    for i in range(len(score)):
        if i > k-1:
            if score[i] > honor[0]:
                honor.append(score[i])
                honor.remove(honor[0])
        else:
            honor.append(score[i])
        honor.sort()
        result.append(honor[0])
    return result