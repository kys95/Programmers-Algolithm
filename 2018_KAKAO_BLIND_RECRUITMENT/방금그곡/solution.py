import math

def solution(m, musicinfos):
    answer = []
    m = m.replace('C#', 'c').replace('D#', 'd').replace('F#', 'f').replace('G#', 'g').replace('A#', 'a')

    for info in musicinfos:
        start, end, name, melody = info.split(',')
        hour, minute = map(int, start.split(':'))
        start = hour * 60 + minute

        hour, minute = map(int, end.split(':'))
        end = hour * 60 + minute
        duration = end - start

        melody = melody.replace('C#', 'c').replace('D#', 'd').replace('F#', 'f').replace('G#', 'g').replace('A#', 'a')
        melody *= math.ceil(duration / len(melody))
        melody = melody[:duration]

        if m in melody:
            answer.append((duration, -start, name))

    if answer:
        answer = sorted(answer, key=lambda x: (x[0], x[1]))
        return answer[-1][2]
    return "(None)"


# 1. #을 포함한 문자열을 소문자로 replace하여 전처리를 해준다.
# 2. 시작시간과 종료 시간 사이의 악보를 구하고 m이 여기 포함되는지 확인한다.