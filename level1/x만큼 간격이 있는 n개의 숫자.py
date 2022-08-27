def solution(x, n):
    a=x
    answer = []
    for i in range(n):
        answer.append(x)
        x+=a
    return answer

x=4
n=3
print(solution(x,n))


def solution(x,n):
    return list(range(x,x*n+1,x))

x=4
n=3
print(solution(x,n))

def solution(x,n):
    return [i*x+x for i in range(n)]

x=4
n=3
print(solution(x,n))