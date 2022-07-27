def solution(msg):
    answer = []
    dic = {}
    for i in range(26):
        dic[chr(65 + i)] = i + 1

    length = 0
    cnt = 27

    while length <= len(msg) - 1:

        temp = 0
        for i in range(1, len(msg) - length + 1):
            if msg[length:length + i] in dic:

                if i == len(msg) - length:
                    answer.append(dic[msg[length:length + i]])
                    temp += 1
                    break
                else:
                    temp += 1


            else:
                answer.append(dic[msg[length:length + i - 1]])

                dic[msg[length:length + i]] = cnt
                cnt += 1

                break
        length += temp
    return answer

1. 단어A~Z를 key로 색인번호 1~26을 value로 하는 딕셔너리형 dic을 초기화하고 주어진 msg를 문자하나씩 비교해본다.
2. 변수 cnt를 27로 두어 새로운 key에 해당하는 value값을 넣도록 한다.
3. ex) K, KA, KAK .. 이렇게 dic에 key가 없는 경우까지 길이를 계속 늘려간다. 만일 KA가 없다면 KA를 key로 cnt를 value로 하고 cnt1+1한다.
4. length가 msg의 마지막 인덱스보다 커질 경우 탐색을 중지하고 answer를 출력한다.