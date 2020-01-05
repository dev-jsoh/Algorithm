from itertools import permutations

def solution(numbers):
    answer = 0
    number_list = list(numbers)
    nums = []
    for i in range(1, len(number_list) + 1):
        temps = list(permutations(number_list, i))
        for temp in temps:
            num = 0
            for j in range(1, i + 1):
                num += int(temp[j - 1]) * pow(10, i - j)
            print(num)
            if num in nums:
                break
            else:
                nums.append(num)
            isPrime = True
            
            if num == 1:
                isPrime = False
            for k in range(2, round(pow(num, 0.5)) + 1):
                if num % k == 0:
                    isPrime = False
                    break
            if isPrime:
                answer += 1
    return answer