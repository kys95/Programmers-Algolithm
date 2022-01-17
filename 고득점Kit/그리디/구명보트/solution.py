def solution(people, limit):
    answer = 0
    people.sort()
    bf = 0
    af = len(people) - 1

    while bf <= af:
        answer += 1
        if people[bf] + people[af] <= limit:
            bf += 1
        af -= 1

    return answer