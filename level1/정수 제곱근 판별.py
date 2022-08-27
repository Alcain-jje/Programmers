"""def solution(n):
    answer=0
    for i in range(1,7400000):
        if i*i==n:
            answer=(i+1)*(i+1)
            break
    if answer == 0:
        answer=-1
    return answer
n=121
print(solution(n))"""

def solution(n):
    answer=n**(1/2)
    if answer % 1 ==0:
        answer= (answer+1)**2
    else:
        answer=-1
    return int(answer)

n=3
print(solution(n))