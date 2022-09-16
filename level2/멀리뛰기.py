#dp 풀이
def solution(n):
    dp=[0]*(n+1)
    dp[1]=1
    if n == 1:
        return 1
    dp[2]=2
    for i in range(3,n+1):
        dp[i]=dp[i-1]+dp[i-2]

    return dp[n]%1234567
n=3
print(solution(n))


#두번째 풀이

def solution(n):
    a=[0,1]
    for i in range(1,n+1):
        a.append(a[-1]+a[-2])
    return a[-1]%1234567


"""
#시간초과
from itertools import permutations
def solution(n):
    a,b=divmod(n,2)
    answer = 0
    for i in range(a+1):
        li=[1]*(n-(2*i))+[2]*i
        com=len(set(permutations(li,len(li))))
        answer+=com
    return answer % 1234567"""