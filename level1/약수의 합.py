"""def solution(n):
    ans=0
    for i in range(1,n+1):
        if n%i==0:
            ans+=i
    return ans
n=5
print(solution(n))"""

def solution2(n):
    return sum([i for i in range(1,n+1) if n % i == 0])

n=12
print(solution2(n))

def solution3(n):
    return n + sum([i for i in range(1,(n//2)+1) if n%i == 0])