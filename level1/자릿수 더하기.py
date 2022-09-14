def solution(n):
    answer=0
    for i in n:
        answer+=int(i)
    return answer

N='123'
print(solution(N))