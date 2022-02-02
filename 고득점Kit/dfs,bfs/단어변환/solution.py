from collections import deque

def bfs(begin, target, words):
    queue = deque()
    queue.append((begin, 0))
    visited = [False] * len(words)

    while queue:
        word, cnt = queue.popleft()
        if word == target:
            return cnt
        for i in range(len(words)):
            num = 0
            if not visited[i]:  # 선택하지 않은 단어 중
                for j in range(len(word)):  # 단어 알파벳 비교
                    if word[j] != words[i][j]:
                        num += 1
                if num == 1:
                    queue.append((words[i], cnt + 1))
                    visited[i] = True

    return 0


def solution(begin, target, words):
    answer = bfs(begin, target, words)
    return answer