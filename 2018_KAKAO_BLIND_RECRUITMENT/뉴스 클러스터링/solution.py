from collections import Counter

def solution(str1, str2):
    str1_low = str1.lower()
    str2_low = str2.lower()

    str1_lst = []
    str2_lst = []

    for i in range(len(str1_low) - 1):
        if str1_low[i].isalpha() and str1_low[i + 1].isalpha():
            str1_lst.append(str1_low[i] + str1_low[i + 1])
    for j in range(len(str2_low) - 1):
        if str2_low[j].isalpha() and str2_low[j + 1].isalpha():
            str2_lst.append(str2_low[j] + str2_low[j + 1])

    Counter1 = Counter(str1_lst)
    Counter2 = Counter(str2_lst)

    inter = list((Counter1 & Counter2).elements())
    union = list((Counter1 | Counter2).elements())

    if len(union) == 0 and len(inter) == 0:
        return 65536
    else:
        return int(len(inter) / len(union) * 65536)


1. 조건에서 대문자와 소문자의 차이는 무시하고 오로지 영문자로 이루어진 조합의 경우에만 자카드 유사도에 사용 -> str1, str2 매게변수 전처리
   (리스트 형태로)
2. 전처리된 리스트 형태의 str1_lst와 str2_lst를 각각 Counter객체로 변환
3. elements() 메서드를 사용하여 원소값만 추출한다.
4. 교집합과 합집합을 구하고 자카도 유사도를 계산한다.