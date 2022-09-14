"""
# 1번 풀이
def solution(n):
    s=[0,1]
    ans=0
    for i in range(2,n+1):
        ans=sum(s[-2:])
        s.append(ans)
    return ans%1234567"""

# 2번 풀이
def solution(n):
    a,b=0,1
    for i in range(n):
        a,b=b,a+b
    return a

n=3
print(solution(n))
