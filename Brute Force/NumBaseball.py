from itertools import permutations
def solution(baseball):
    answer = 0
    nums = list(permutations(list(map(str, range(1, 10))), 3))
    temp = []
    for trial in baseball:
        for num in nums:
            balls = 0
            strikes = 0
            if num[0] in str(trial[0]):
                balls += 1
            if num[1] in str(trial[0]):
                balls += 1
            if num[2] in str(trial[0]):
                balls += 1
            if num[0] == str(trial[0])[0]:
                strikes += 1
                balls -= 1
            if num[1] == str(trial[0])[1]:
                strikes += 1
                balls -= 1
            if num[2] == str(trial[0])[2]:
                strikes += 1
                balls -= 1
            if strikes == trial[1] and balls == trial[2]:
                temp.append(num)
        nums = temp
        temp = []
    answer = len(nums)
    return answer