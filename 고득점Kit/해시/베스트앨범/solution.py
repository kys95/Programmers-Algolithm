def solution(genres, plays):
    answer = []
    dic = {}  # 장르별 노래재생 횟수
    d = {}  # 장르별 [(고유번호, 노래재생횟수)]
    idx = -1

    for genre, play in zip(genres, plays):
        idx += 1
        if genre not in dic:
            dic[genre] = 0
        dic[genre] += play

        if genre not in d:
            d[genre] = [(idx, play)]
            continue
        d[genre] += [(idx, play)]
    dic = sorted(dic.items(), key=lambda x: x[1], reverse=True)

    for genre, play in dic:  # 속한 노래가 많이 재생된 장르 먼저 수록
        print(genre, play)
        d[genre] = sorted(d[genre], key=lambda x: (-x[1], x[
            0]))  # 장르 내에서 재생된 노래 먼저 수록, 재생횟수가 같                                                                      다면 고유 번호가 낮은 노래 먼저 수록

        answer += [idx for (idx, play) in d[genre][:2]]

    return answer