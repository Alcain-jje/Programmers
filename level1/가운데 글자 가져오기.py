
def solution(s):
    i=len(s) % 2
    if len(s) % 2 == 0:
        i=len(s)//2
        answer=s[i-1:i+1]
    elif len(s) % 2 != 0:
        i = len(s) // 2
        answer=s[i]
    #answer = ''

    return answer


s='qwer'
print(solution(s))