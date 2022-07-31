def calc_date(line):
    date, end, time = line.split(" ")
    h = int(end[:2]) * 3600
    m = int(end[3:5]) * 60
    s = int(end[6:8])
    ms = int(end[9:])
    duration_time = int(float(time[:-1]) * 1000)

    start = (h + m + s) * 1000 + ms - duration_time + 1
    end = (h + m + s) * 1000 + ms

    return (start, end)


def throughput(logs, start, end):
    cnt = 0
    for log in logs:

        if log[0] < end and log[1] >= start:
            cnt += 1

    return cnt


def solution(lines):
    answer = 0
    logs = []
    for line in lines:
        start, end = calc_date(line)
        logs.append((start, end))

    for log in logs:
        answer = max(answer, throughput(logs, log[0], log[0] + 1000), throughput(logs, log[1], log[1] + 1000))

    return answer

# 1. 초당 최대 처리량을 구하기 위해서는 배열에 (시작시간, 끝시간)을 넣어 각 시작시간, 끝시간과 겹치는 개수를 찾아야한다.
#    -> 입력받은 lines를 ms로 모두 전처리 과정을 거치고 시작시간과 끝시간을 구해 배열 logs에 넣는다.
# 2. logs의 시작시간, 끝시간을 logs의 원소들과 비교하여 겹치는 개수를 찾아 최대값을 갱신한다.