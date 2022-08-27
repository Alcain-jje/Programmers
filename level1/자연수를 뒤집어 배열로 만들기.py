"""def solution(n):
    ans=list(str(n))
    answer=[]
    for i in ans:
        answer.append(int(i))
    return answer[::-1]

n=12345
print(solution(n))"""

# 풀이 2
def solution(n):
    #return list(map(int,reversed(str(n))))
    #return list(map(int, list(str(n))[::-1]))
    return [int(i) for i in str(n)][::-1]
n=12345
print(solution(n))