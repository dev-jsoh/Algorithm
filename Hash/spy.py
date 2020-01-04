import itertools

def solution(clothes):
    answer = 0
    kinds = {}
    for cloth in clothes:
        if cloth[1] in kinds:
            kinds[cloth[1]] += 1
        else:
            kinds[cloth[1]] = 1
    values = kinds.values()
    for i in range(1, len(values) + 1):
        combinations = list(itertools.combinations(values, i))
        for combination in combinations:
            temp = 1
            for val in combination:
                temp *= val
            answer += temp
    return answer

 