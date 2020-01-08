def solution(clothes):
    answer = 1
    kinds = {}
    for cloth in clothes:
        if cloth[1] in kinds:
            kinds[cloth[1]] += 1
        else:
            kinds[cloth[1]] = 1
    values = kinds.values()
    for value in values:
        answer *= value + 1
    answer -= 1
    return answer