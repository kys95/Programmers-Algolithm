from collections import deque

# BFS 풀이
def solution(info, edges):
    graph = [[] for _ in range(len(info))]
    max_sheep = 0
    for edge in edges:
        graph[edge[0]].append(edge[1])
    # 현재위치, 양개수, 늑대개수, 이동 가능한 노드
    q = deque([[0, 1, 0, set()]])
    while q:
        now, sheepCount, wolfCount, nextNode = q.popleft()
        max_sheep = max(max_sheep, sheepCount)
        nextNode.update(graph[now])  # 이 부분에서 for loop를 사용해서 add를 하는게 시간은 더 짧음

        # set의 Union 연산은 O(len(a) + len(b)) , for loop을 사용하면 O(len(graph[now])) 만큼만
        for next in nextNode:

            if info[next]:
                # 늑대일경우
                if sheepCount != wolfCount + 1:
                    q.append([next, sheepCount, wolfCount + 1, nextNode - {next}])

            else:
                q.append([next, sheepCount + 1, wolfCount, nextNode - {next}])

    return max_sheep


# 1. 노드 0에서 1을 거치고 8을 가는 것과 8을 거치고 1을 가는 것이 다른 경우이므로 이동 가능한 노드를 set형으로 두고 bfs를 통해 탐색한다.
# 2. 현재위치, 양개수, 늑대개수, 이동 가능한 노드를 deque에 넣고 각 노드기준으로 이동할 수 있는 노드면 양과 늑대의 개수를 비교하고 양이 더
#    많다면 deque에 도착노드, 양개수 +1, 늑대개수, 이동 가능한 노드를 갱신해주고 삽입힌다.
# 3. 양의 개수 sheepCount는 계속 최대값으로 갱신해준다.
# 4. deque에 노드가 없을 때까지 bfs를 통해 탐색해준다.














