"""def solution(a, b):
    if a > b: a, b = b, a
    answer=0
    for i in range(a,b+1):
        answer+=i
    return answer

a=5
b=3
print(solution(a,b))"""

def solution2(a,b):

    return sum(range(min(a,b),max(a,b)+1))

a=5
b=3
print(solution2(a,b))