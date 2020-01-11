def solution(priorities, location):
    answer = 0
    spool = [x for x in enumerate(priorities)]
    priorities.sort(reverse=True)
    while True:
        if spool[0][1] == priorities[0]:
            answer += 1
            if spool[0][0] == location:
                break
            else:
                spool.pop(0)
                priorities.pop(0)
        else:
            spool.append(spool.pop(0))         
    return answer
