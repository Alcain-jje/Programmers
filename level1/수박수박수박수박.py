# 내 풀이 1 (리스트)
def solution(n):
    li=['수','박']
    answer=''
    for i in range(n):
        if i % 2 ==0: answer+=li[0]
        else: answer+=li[1]
    return answer
n=4
print(solution(n))

# 내 풀이 2 (딕셔너리)
def solution2(n):
    dic={0:'수',1:'박'}
    answer = ''
    for i in range(n):
        answer+=dic[i%2]
    return answer
n=3
print(solution2(n))

def solution3(n):
    return "수박"*(n//2)+"수"*(n%2)

def solution4(n):
    answer = "수박" *n
    return answer[:n]

def solution5(n):
    return "".join(["수박"[i%2] for i in range(n)])