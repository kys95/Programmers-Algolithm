from bisect import bisect_left, bisect_right


# 키워드별로 매치된 단어 갯수 계산 메서드
def count_by_range(array, right_val, left_val):
    right_index = bisect_right(array, right_val)
    left_index = bisect_left(array, left_val)

    return right_index - left_index


def solution(words, queries):
    answer = []
    # 각 가사 단어 길이를 기준으로 나누어 저장하는 리스트
    length = [[] for _ in range(10001)]
    # 각 가사 단어 길이를 기준으로 뒤집어 저장하기 위한 리스트
    reversed_length = [[] for _ in range(10001)]

    # 단어 길이를 기준으로 리스트 초기화
    for word in words:
        length[len(word)].append(word)
        reversed_length[len(word)].append(word[::-1])

        # 이진 탐색하기 위해 오름차순 정렬
    for i in range(10001):
        length[i] = sorted(length[i])
        reversed_length[i] = sorted(reversed_length[i])

    # 검색 키워드의 ?가 접두사에 있는 경우와 접미사에 있는 경우
    for keyword in queries:
        # ? -> z로 변환
        right = keyword.replace('?', 'z')
        # ? -> a로 변환
        left = keyword.replace('?', 'a')
        # 접두사에 있는 경우
        if keyword[0] == '?':
            result = count_by_range(reversed_length[len(keyword)], right[::-1], left[::-1])
            # 접미사에 있는 경우
        else:
            result = count_by_range(length[len(keyword)], right, left)

        answer.append(result)
    return answer