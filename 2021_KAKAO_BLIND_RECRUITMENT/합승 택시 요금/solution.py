# def solution(n, s, a, b, fares):
#     INF = int(1e9)
#     answer = INF

#     graph = [[INF for _ in range(n + 1)] for _ in range(n + 1)]
#     for n1,n2,c in fares:
#         graph[n1][n2] = c
#         graph[n2][n1] = c

#     for i in range(1, n + 1):
#         for j in range(1, n + 1):
#             if i == j:
#                 graph[i][j] = 0

#     for k in range(1, n + 1):
#         for i in range(1, n + 1):
#             for j in range(1, n + 1):
#                 graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

#     for k in range(1, n + 1):
#         answer = min(answer, graph[s][k] + graph[k][a] + graph[k][b])

#     return answer

import heapq

def solution(n, s, a, b, fares):
    def dijkstra(start):
        res = [float('INF') for _ in range(n + 1)]
        res[start] = 0
        q = []
        heapq.heappush(q, (res[start], start))
        while q:
            result_x, x = heapq.heappop(q)
            for fu, fw in graph[x]:
                if res[fu] > result_x + fw:
                    res[fu] = result_x + fw
                    heapq.heappush(q, ([res[fu], fu]))
        return res

    ans = 200000001
    graph = [[] for _ in range(n + 1)]
    for i, j, c in fares:
        graph[i].append((j, c))
        graph[j].append((i, c))

    dist = [[]]
    for i in range(1, n + 1):
        dist.append(dijkstra(i))
    print(dist)
    for i in range(1, n + 1):
        ans = min(ans, dist[s][i] + dist[i][a] + dist[i][b])
    return ans

1. 그래프탐색의 완전탐색인 플로이드-와샬을 이용하자
2. fares에 있는 지점들 사이의 택시요금 cost를 갱신해주고 플로이드 와샬함수를 실행한다.
3. 플로이드 와샬함수: k를 1부터 n번 지점까지 돌면서 i에서 k를 거쳐 j까지 가는 cost를 갱신해준다.
4. i를 A와 B가 같이가는 지점이라고 가정하고, 1부터 n까지 반복문을 돌며 s에서 i까지의 비용 + i에서 a까지의 비용 +i에서 b까지의 비용을 구해
   ans와 비교해 작은 값을 ans에 넣어준다. 모든 지점을 다 확인하 뒤 ans를 return해준다.
5. 다른 방법으로 다익스트라 방법을 이용한다.