def solution(n):
    return hanoi(n,1,3,[])
def hanoi(n,a,b,ans):
    if n==0:
        return
    hanoi(n-1,a,6-(a+b),ans)
    print(ans)
    ans.append([a,b])
    hanoi(n-1,6-(a+b),b,ans)

    return ans

n=2
print(solution(n))