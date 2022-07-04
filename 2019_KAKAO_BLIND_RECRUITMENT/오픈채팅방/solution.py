def solution(record):
    answer = []
    user = dict()
    order = []

    for re in record:
        if "Leave" in re:
            a, b = re.split()
            order.append((a, b))
        else:
            a, b, c = re.split()
            user[b] = c
            if a == "Enter":
                order.append((a, b))

    for (a, b) in order:
        if a == "Enter":
            answer.append(f"{user[b]}님이 들어왔습니다.")
        else:
            answer.append(f"{user[b]}님이 나갔습니다.")

    return answer