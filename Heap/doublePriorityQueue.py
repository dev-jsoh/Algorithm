import heapq as hq
def solution(operations):
    answer = []
    cnt = 0
    for o in operations:
        oper = o.split()
        if cnt == 0:
            maxH = []
            minH = []
        if oper[0] == "I":
            cnt += 1
            hq.heappush(maxH, -int(oper[1]))
            hq.heappush(minH, int(oper[1]))
        else:
            if cnt <= 0:
                continue
            cnt -= 1
            if oper[1] == "1":
                hq.heappop(maxH)
            else:
                hq.heappop(minH)
    if cnt <= 0:
        answer = [0, 0]
    else:
        answer = [-hq.heappop(maxH), hq.heappop(minH)]
    return answer
