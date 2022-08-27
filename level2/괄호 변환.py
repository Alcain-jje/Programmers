def solution(p):
    stack=[]
    dic={'(':0,')':0}
    for i in p:
        if i =="(":
            stack.append("(")
            dic["("]+=1
        else:
            if stack:
                stack.pop()
            dic[")"]+=1
    if len(stack)==0 and dic["("]==dic[")"]:
        return str(p)
    else:
        return solution2(p)

def solution2(l):
    global strr
    for i in range(2,len(l)+1,2):
        u,v=l[0:i],l[i:]
        stack = []
        dic = {'(': 0, ')': 0}
        for i in u:
            if i == "(":
                stack.append("(")
                dic["("] += 1
            elif i == ")":
                if stack:
                    stack.pop()
                dic[")"] += 1
        if len(stack) == 0 and dic["("] == dic[")"]:
            return str(u) + solution2(v)
        elif len(stack) != 0 and dic["("] == dic[")"]:
            ss = ""
            for i in u[1:-1]:
                if i == '(':
                    ss += ')'
                else:
                    ss += '('
            strr = '(' + str(solution(v)) + ')' + ss
            return strr
        else:
            continue






#li="(()())()"
#li="()))((()"

#li="())))((("
li=")()(()"
print(solution(li))

"""
def correct(u):
    answer = ''
    stack=[]
    dic={'(':0,')':0}
    for i in u:
        if i =="(":
            stack.append("(")
            dic["("]+=1
        elif i == ")":
            if stack:
                stack.pop()
            dic[")"]+=1
    if len(stack)==0 and dic["("]==dic[")"]:
        return True
    elif len(stack) != 0 and dic["("] == dic[")"]:
        return 's'
    else:
        return False"""