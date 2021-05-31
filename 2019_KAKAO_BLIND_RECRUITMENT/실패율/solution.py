def solution(N, stages):
    answer = []
    # 스테이지 도전한 사용자 수
    users = len(stages)

    # 각 스테이지마다 확인
    for stage in range(1, N + 1):
        # 해당 스테이지에 도달했으나 아직 클리어하지 못한 플레이어 수
        count = stages.count(stage)
        # 실패율 계산
        if users == 0:
            failure_rate = 0
        else:
            failure_rate = count / users
        # (스테이지, 실패율) 삽입
        answer.append((stage, failure_rate))
        # 사용자 수 계산
        users -= count
    # 실패율 기준으로 내림차순 정렬
    answer = sorted(answer, key=lambda x: -x[1])
    # 원소를 스테이지로만 초기화
    answer = [i[0] for i in answer]

    return answer