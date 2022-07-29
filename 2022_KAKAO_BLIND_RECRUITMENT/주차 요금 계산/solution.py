import math


def solution(fees, records):
    answer = []

    cars = {}  # {차량번호: [시각,이용시간,내용]}
    for record in records:
        time, num, info = record.split()
        h, m = time.split(":")
        h, m = int(h), int(m)
        t = 60 * h + m
        if num in cars:  # 주차장 이용해본 차량
            if info == 'IN':  # 입차
                cars[num][0] = t
                cars[num][2] = 'IN'
            else:  # 출차
                cars[num][1] += t - cars[num][0]
                cars[num][0] = t
                cars[num][2] = 'OUT'
        else:
            cars[num] = [t, 0, 'IN']
    sortedCar = sorted(cars.items())
    print(sortedCar)
    for data in sortedCar:

        if data[1][2] == 'OUT':
            if data[1][1] <= fees[0]:
                answer.append(fees[1])
            else:
                fee = fees[1] + math.ceil((data[1][1] - fees[0]) / fees[2]) * fees[3]
                answer.append(fee)
        else:
            data[1][1] += (23 * 60 + 59) - data[1][0]
            if data[1][1] <= fees[0]:
                answer.append(fees[1])
            else:
                fee = fees[1] + math.ceil((data[1][1] - fees[0]) / fees[2]) * fees[3]
                answer.append(fee)

    return answer

1. 고유의 차량번호를 가진 차량들에 따라 요금을 계산해야 하므로 차량번호를 key, [시각, 이용시간, 내역]을 value로 하는 dic을 만든다.
2. 처음입차한 차량의 경우 이용시간을 0으로 하고 내역을 'IN'으로 한다. 이후에 출차를 할경우 현재시각과 입차한 시각을 뺀 값을 이용시간에 넣는다.
   내역은 'OUT'으로 변경한다.
3. records순으로 딕셔너리 형 dic에 데이터를 넣은 후 key를 기준으로 정렬을 하고 내역이 'IN'인 경우 23:59에서 시각을 뺀 값을 이용시간에 추가해서
   계산한다.
4. fees 조건대로 요금을 계산하여 넣어준다.