def solution(n, m):
    a,b=n,m
    while(m):
        n,m=m,n%m
    li=[n,(a*b)//n]
    return li
n=2
m=5
print(solution(n,m))