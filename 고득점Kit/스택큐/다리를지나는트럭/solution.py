def solution(bridge_length, weight, truck_weights):
    time = 0
    bridge = [0] * bridge_length
    bridge_weight = 0  # 다리 위에 있는 트럭들의 무게
    while bridge:
        time += 1
        bridge_weight -= bridge.pop(0)
        if truck_weights:
            if bridge_weight + truck_weights[0] <= weight:
                bridge_weight += truck_weights[0]
                bridge.append(truck_weights.pop(0))
            else:
                bridge.append(0)

    return time