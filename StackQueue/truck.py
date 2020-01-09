def solution(bridge_length, weight, truck_weights):
    answer = 0
    q = []
    now = 0
    while truck_weights:
        if weight - now >= truck_weights[0]:
            answer += 1
            now += truck_weights[0]
            q.append([truck_weights.pop(0), 0])
            q = list(map(lambda x: [x[0], x[1] + 1], q))
        else:
            answer += bridge_length - q[0][1]
            q = list(map(lambda x: [x[0], x[1] + (bridge_length - q[0][1])], q))

        if q[0][1] == bridge_length:
            now -= q.pop(0)[0]
    answer += bridge_length - q[-1][1] + 1
    return answer