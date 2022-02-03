from collections import defaultdict

def dfs(start, graph, answer):
    while graph[start]:  # a->b b->c 연결 확인
        dfs(graph[start].pop(0), graph, answer)

    if not graph[start]:
        answer.append(start)
        return

def solution(tickets):
    answer = []
    graph = defaultdict(list)  # [a,b]항공권 리스트

    for start, end in tickets:  # 딕셔너리 형태로 변환
        graph[start].append(end)
    for start, end in graph.items():  # 알파벳 순서로 오름차순 정렬
        graph[start].sort()

    dfs("ICN", graph, answer)  # ICN공항부터 출발

    return answer[::-1]