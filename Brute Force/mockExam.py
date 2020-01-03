supo_1 = [1, 2, 3, 4, 5]
supo_2 = [2, 1, 2, 3, 2, 4, 2, 5]
supo_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
def solution(answers):
    answer = []
    results = [0, 0, 0]
    for i in range(len(answers)):
        if answers[i] == supo_1[i % len(supo_1)]:
            results[0] += 1
        if answers[i] == supo_2[i % len(supo_2)]:
            results[1] += 1
        if answers[i] == supo_3[i % len(supo_3)]:
            results[2] += 1
    maxValue = max(results)
    answer = [i + 1 for i, j in enumerate(results) if j == maxValue]
    return answer