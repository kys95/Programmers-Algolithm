from collections import deque


def solution(cacheSize, cities):
    answer = 0
    cache = deque()
    size = 0

    if cacheSize == 0:
        answer = 5 * len(cities)
        return answer

    for city in cities:
        city = city.lower()

        if city in cache:
            cache.remove(city)
            cache.append(city)
            answer += 1
        else:
            if size == cacheSize:
                cache.popleft()
                cache.append(city)
                answer += 5
            else:
                cache.append(city)
                size += 1
                answer += 5

    return answer

# def solution(cacheSize, cities):
#     import collections
#     cache = collections.deque(maxlen=cacheSize)
#     time = 0
#     for i in cities:
#         s = i.lower()
#         if s in cache:
#             cache.remove(s)
#             cache.append(s)
#             time += 1
#         else:
#             cache.append(s)
#             time += 5
#     return time

# 1. 캐시의 형태가 선입선출이므로 자료구조 큐의 형태를 띄고있다. -> deque 이용하자!
# 2. cacheSize가 0이 아니라면 캐시에 존재하는 도시와 일치하면 실행시간을 1로 줄일 수 있다. -> 0이면 실행시간 5 * 도시길이로 바로 리턴해주자.
# 3. for문으로 도시이름을 비교하여(소문자로 바꿈) 캐시에 도시가 존재하면 캐시에 존재하는 해당 도시를 삭제하고 다시 삽입한다.(실행시간 1추가) -> LRU 원칙이므로
#
# 4. 캐시에 도시가 존재하지 않는다면 캐시가 가득찼을 경우, 캐시에 가장 먼저들어온 도시를 삭제하고 해당 도시를 삽입한다(실행시간 5추가)
#    캐시에 공간이 있을 경우, 캐시에 해당 도시를 삽입한다(실행시간 5추가)
# 5. 최종적으로 실행시간을 출력한다.