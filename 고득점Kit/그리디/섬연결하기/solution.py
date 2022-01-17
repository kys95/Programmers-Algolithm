def solution(n, costs):
    answer = 0
    costs.sort(key=lambda x: x[2])
    line = set([costs[0][0]])

    while len(line) != n:
        for cost in costs:
            if cost[0] in line and cost[1] in line:
                continue
            elif cost[0] in line or cost[1] in line:
                answer += cost[2]
                line.update([cost[0], cost[1]])
                break
    return answer