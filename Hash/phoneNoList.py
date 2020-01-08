def solution(phone_book):
    answer = True
    answer = clsfy(phone_book)
    return answer

def clsfy(nums):
    tmp = [[] for _ in range(10)]
    for i in nums:
        tmp[int(i[0])].append(i[1:])
    nxt = []
    for i in tmp:
        if len(i) >= 2:
            nxt.append(i)
    if len(nxt) == 0:
        return True
    for n in nxt:
        if '' in n:
            return False
        else:
            return clsfy(n)

