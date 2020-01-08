import heapq
def solution(genres, plays):
    answer = []
    clsfy = {}
    for i in range(len(genres)):
        if genres[i] in clsfy:
            heapq.heappush(clsfy[genres[i]], (-plays[i], i))
        else:
            clsfy[genres[i]] = []
            heapq.heappush(clsfy[genres[i]], (-plays[i], i))
    ans_heap = []
    for i in clsfy:
        temp = [0, []]
        temp_h = heapq.heappop(clsfy[i])
        temp[0] += temp_h[0]
        temp[1].append(temp_h[1])
        if len(clsfy[i]) > 0:
            temp_h = heapq.heappop(clsfy[i])
            temp[0] += temp_h[0]
            temp[1].append(temp_h[1])
        heapq.heappush(ans_heap, temp)
    while heapq:
        answer += heapq.heappop(ans_heap)[1]
    return answer