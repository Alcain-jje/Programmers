"""
#반만 맞은 풀이
def solution(expression):
    ans=-1e9
    dic = {'plus': '+', 'minus': '-', 'gob': '*'}
    sitt=['plus','minus','gob']
    for i in sitt:
        strr=expression.split(dic[i])
        if dic[i] == '+':
            ans=max(dfs('plus','gob',strr,dic),dfs('plus','minus',strr,dic),ans)
        elif dic[i] == '-':
            ans = max(dfs('minus', 'gob', strr,dic), dfs('minus', 'plus', strr,dic), ans)
        else:
            ans = max(dfs('gob', 'plus', strr,dic), dfs('gob', 'minus', strr,dic), ans)

    return ans

def dfs(cal1,cal2,a,dic):
    li = []
    print(a)
    for j in a:
        if dic[cal2] in j:
            li.append(str(eval(j)))
        else:
            ii = j.split(dic[cal1])
            #print(ii)
            li.append(eval("".join(map(str, ii))))

    ans = str(li[0])
    for i in range(1, len(li)):
        ans += dic[cal1]
        ans += str(li[i])
    answer=eval(ans)

    return abs(answer)

expression="100-200*300-500+20"
#expression="50*6-3*2"
#expression="177-661*999*99-133+221+334+555-166-144-551-166*166-166*166-133*88*55-11*4+55*888*454*12+11-66+444*99"
print(solution(expression))

for e in expression.split("-"):
    print(e)"""

def calc(rank,n,expression):
    if n==2:
        return str(eval(expression))
    if rank[n] == '*':
        res=eval('*'.join([calc(rank,n+1,e) for e in expression.split('*')]))
    if rank[n] == '+':
        res = eval('+'.join([calc(rank, n + 1, e) for e in expression.split('+')]))
    if rank[n] == '-':
        res = eval('-'.join([calc(rank, n + 1, e) for e in expression.split('-')]))
    return str(res)

def solution(expression):
    answer=0
    ranked=[('*', '-', '+'),
        ('*', '+', '-'),
        ('+', '*', '-'),
        ('+', '-', '*'),
        ('-', '*', '+'),
        ('-', '+', '*')]
    for rank in ranked:
        res=int(calc(rank,0,expression))
        answer=max(answer,abs(res))
    return answer


strr ="100-200*300-500+20"
print(solution(strr))

"""anss=""
las=['100-200*300-500', '20']
for j in las:
    if '*' in j:
        asd=j.split('*')
        for k in asd:
            print(eval(k))"""

"""
strr ="100-200*300-500+20"
a=strr.split("-")
print(a)

str1='plus'
str2='minus'
str3='gob'

dic={'plus':'+','minus':'-','gob':'*'}


#dfs
li=[]
for j in a:
    if dic[str1] in j:
        li.append(str(eval(j)))
    else:
        ii=j.split(dic[str1])
        li.append(eval("".join(map(str,ii))))
print(li)
ans=str(li[0])

for i in range(1,len(li)):
    ans+=dic[str2]
    ans+=str(li[i])
print(eval(ans))
"""


"""ada='-'
ans=0
for i in range(len(li)):
    if i == 0:
        ans+=eval("".join(map(str,li[i])))
    else:
        ans-=eval("".join(map(str,li[i])))

print(ans)"""
"""num=int(eval(a[0]))

for i in range(1,len(a)):
    #print(eval(i))
    num *= eval(a[i])
print(num)"""



"""kk=0
for i in a:
    print(eval(i))
    num+=eval(i)
"""