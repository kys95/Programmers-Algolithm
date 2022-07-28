def convert(num, base):
    temp = "0123456789ABCDEF"
    q, r = divmod(num, base)

    if q == 0:
        return temp[r]
    else:
        return convert(q, base) + temp[r]


def solution(n, t, m, p):
    answer = ''
    test = ''

    for i in range(m * t):
        test += convert(i, n)

    while len(answer) < t:
        answer += test[p - 1]
        p += m

    return answer

1. 0에서부터 목표하는 숫자까지 n진법으로 변환해서 문자열 리스트에 저장해둔다.
   -> 목표하는 숫자의 최대 range는 게임 참가 인원(m), 미리 구해놓을 수(t) 만큼만 확보해놓으면 그 안에서 처리할 수 있다. 0~8까지 구한다고
      했을 때, 2진수가 되면 0~1000 이렇게 늘어나니까 이보다 적게 필요하기도 함. 최대가 m*t.
2. 변환한 리스트에서 튜브 순서에 해당하는 인덱스 값의 원소들만 뽑아오면 정답
   -> 튜브 순서는 주어졌고, 리스트니까 인덱스는 (튜브 순서 - 1). 이 후 사람 수(m)만큼 인덱스를 증가시키면 튜브 순서에 해당하는 인덱스 값이다.
      미리 구해놓을 수의 갯수만큼 출력이 되면 종료하면 된다.
