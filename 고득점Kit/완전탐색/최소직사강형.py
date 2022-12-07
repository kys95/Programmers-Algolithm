def solution(sizes):
    answer = 0
    w = []  #큰 값
    h = []  #작은 값
    for size in sizes:
        if size[0] >= size[1]:
            w.append(size[0])
            h.append(size[1])
        else:
            w.append(size[1])
            h.append(size[0])
    answer = max(w) * max(h)
    return answer