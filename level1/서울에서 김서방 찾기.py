def solution(seoul):
    i=seoul.index('Kim')
    answer = f'김서방은 {i}에 있다'
    return answer

seoul = ['Jane','Kim']
print(solution(seoul))

def solution(seoul):
    answer=''
    return ('김서방은 %d에 있다' %seoul.index('Kim'))
seoul = ['Jane','Kim']
print(solution(seoul))