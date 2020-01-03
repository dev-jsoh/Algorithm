def solution(s):
    answer = len(s)
    answer_str = ''
    for length in range(1, len(s)):
        repS = s[:length]
        repN = 0
        result = ''
        for i in range(length, len(s), length):
            if repS == s[i: i + length]:
                repN += 1
            else:
                if repN:
                    result += str(repN + 1) + repS
                else:
                    result += repS
                repS = s[i: i + length]
                repN = 0
        if repN:
            result += str(repN + 1) + repS
        else:
            result += repS
        if len(result) < answer:
            answer_str = result
            answer = len(result)
    print(answer_str)
    return answer