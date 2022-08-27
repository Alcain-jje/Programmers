"""def solution(x):
    answer=False
    ans=sum([int(i) for i in str(x)])
    if int(x) % ans== 0:
        answer = True
    return answer
x=13
print(solution(x))"""

"""
def solution(x):
    return x % sum([int(i) for i in str(x)]) == 0

print(solution(12))"""

def solution(x):
    x=str(x)
    a=0
    for i in range(len(x)):
        a+=int(x[i])
    return True if int(x)%a==0 else False

print(solution(12))