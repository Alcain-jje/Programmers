"""def solution(p):
    if not p:
        return ""
    u,v = seperate(p)

    if isBalanced(u):
        return u + solution(v)
    # 4번
    else:
        answer = '('
        answer += solution(v)
        answer += ')'

        for i in u[1:-1]:
            if i == '(':
                answer += ')'
            else:
                answer += '('
        return answer

# 문자열을 u와 v로 분리하는 함수
def seperate(p):
    left_count = 0
    right_count = 0
    for idx, i in enumerate(p):
        if i == '(':
            left_count += 1
        elif i == ')':
            right_count += 1
        # 더이상 나눠질 수 없는 올바른 괄호문자열 찾음
        if left_count == right_count:
            return p[:idx + 1], p[idx + 1:] # u,v


def isBalanced(u):
    stack = []
    for i in u:
        if i == '(':
            stack.append(i)
        else:
            if not stack:
                return False
            stack.pop()
    return True"""



def solution(p):
    if p =="": return p
    r=True; c=0
    for i in range(len(p)):
        if p[i] == '(': c-=1
        else: c+=1
        if c>0: r=False
        if c==0:
            if r:
                return p[:i+1]+solution(p[i+1:])
            else:
                #return '(' + solution(p[i + 1:]) + ')' + ''.join(list(map(lambda x: '(' if x == ')' else ')', p[1:i])))
                return '('+solution(p[i+1:])+')'+''.join(list(map(lambda x:'('if x==')' else ')',p[1:i])))
li="()))((()"
print(solution(li))