"""def solution(s):
    s=list(s)
    answer=''.join(map(str,sorted(s,reverse=True)))
    return answer"""

def solution(s):
    answer=''.join(sorted(s,reverse=True))
    return answer
s='Zbcdefg'
print(solution(s))