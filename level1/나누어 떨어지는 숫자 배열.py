# 1번 풀이
def solution(arr, divisor):
    answer = [i for i in arr if i % divisor == 0]
    if not answer:
        answer.append(-1)
    answer.sort()
    return answer

arr=[2, 36, 1, 3]
divisor=1
print(solution(arr,divisor))

# 2번 풀이
def solution(arr, divisor): return sorted([n for n in arr if n%divisor == 0]) or [-1]
"""
def solution(arr, divisor):
    answer = []
    for i in arr:
        if i % divisor == 0:
            answer.append(i)
    if not answer:
        answer.append(-1)
    answer.sort()
    return answer"""