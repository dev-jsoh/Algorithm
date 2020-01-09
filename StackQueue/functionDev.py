from math import ceil

def solution(progresses, speeds):
    answer = []
    days = [0 for _ in range(len(progresses))]
    for i in range(len(progresses)):
        days[i] = ceil((100 - progresses[i]) / speeds[i])
    temp = days[0]
    answer = [1]
    for d in days[1:]:
        if temp < d:
            answer.append(1)
            temp = d
        else:
            answer[-1] += 1
    return answer