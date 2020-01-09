def solution(heights):
    answer = []
    s = []
    idx = 1
    for h in heights:
        isReceived = False
        while s:
            if s[-1][1] > h:
                answer.append(s[-1][0])
                s.append((idx, h))
                isReceived = True
                break
            s.pop(-1)
        if not isReceived:
            answer.append(0)
            s.append((idx, h))
        idx += 1
    return answer