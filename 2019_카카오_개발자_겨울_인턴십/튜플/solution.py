def solution(s):
    answer = []
    s = s[2:-2]  # "{{&}} 제거"
    s = s.split('},{')
    s = sorted(s, key=len)

    for data in s:
        num = data.split(',')
        for n in num:
            if int(n) not in answer:
                answer.append(int(n))

    return answer

# 1. 입력받는 문자열 s의 앞부분의 "{{" 와 뒷부분의 "}}"를 잘라내면 "},{"를 기준으로 숫자만 남게된다.
# 2. s를 원소의 개수를 기준으로 오름차순 정렬시킨다.
# 3. s의 원소를 탐색하여 answer에 없는 숫자만 삽입한다.
# 4. 최종적으로 answer를 반환한다.