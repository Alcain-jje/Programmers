import math

"""
# 풀이 1
def lcm(a,b):
    return (a*b)//math.gcd(a,b)
def solution(arr):
    answer = 0
    for i in range(len(arr)):
        if i==0:
            answer=lcm(arr[i],arr[i+1])
        else:
            answer=lcm(arr[i],answer)
    return answer"""


# 풀이 2
def solution(arr):
    answer=arr[0]
    for n in arr:
        answer = n * answer // math.gcd(n,answer)

    return answer
arr=[2,6,8,14]
print(solution(arr))

# 풀이 3
from functools import reduce
def nlcm(num):
    return reduce(lambda a, b : a * b // math.gcd(a, b), num,1)
print(nlcm(arr))