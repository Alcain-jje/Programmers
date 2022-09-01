"""def solution(s):
    ans = 0
    for i in range(len(s)):
        first = ord(s[i]) - ord('A')
        last = 1 + ord('Z') - ord(s[i])
        if first == 0 or last == 0:
            sol(ans,s[i+1:len(s)])
        elif first < last:
            ans += first
            ans += 1
        else:
            ans += last
            ans += 1
    return ans-1
def sol(ans,s):
    for i in range(len(s)):
        first = ord(s[i]) - ord('A')
        last = 1 + ord('Z') - ord(s[i])
        if first == 0 or last == 0:
            sol(ans, s[i + 1:len(s)])
        elif first < last:
            ans += first
            ans += 1
        else:
            ans += last
            ans += 1
    return ans-1"""

#GGADC
#s[2+1:len(i)]
#ABCDEFGHIJKO
#print(ord('A'))

"""from itertools import permutations as p

INF = int(1e9)
def countChange(alp):
    return min(ord('Z') - ord(alp) + 1, ord(alp) - ord('A'))

def findShortestPath(name,now,next):
    right, left = max(next,now), min(next,now)
    rightDist=right-left
    leftDist=left + len(name) - right
    return min(rightDist,leftDist)

def solution(name):
    answer=INF
    togoPlaces=[i for i in range(len(name)) if name[i] !="A" and i !=0]

    changeCount =0
    for c in name:
        changeCount+=countChange(c)

    cases=p(togoPlaces,len(togoPlaces))
    for case in cases:
        now=0
        result=0

        for next in case:
            dist=findShortestPath(name,now,next)
            result+=dist
            now=next
        answer=min(answer,result+changeCount)
    return answer"""



from itertools import permutations as p

INF = int(1e9)

def count_num(i):
    return min(1 + ord('Z') - ord(i),ord(i) - ord('A'))
def findshort(name,now,next):
    left,right=min(now,next),max(now,next)
    right_num=right-left
    left_num=left+len(name)-right
    return min(right_num,left_num)

def solution(name):
    answer = INF
    li=[i for i in range(len(name)) if name[i] != 'A' and i != 0]
    changeCount=0
    for i in name:
        changeCount+=count_num(i)
    pp=p(li,len(li))
    for j in pp:
        result=0
        now=0
        for next in j:
            dist=findshort(name,now,next)
            result+=dist
            now=next
        answer=min(result+changeCount,answer)
    return answer

s='JEROEN'
print(solution(s))

"""ans=0
for i in s:
    first=ord(i)-ord('A')
    last=1+ord('Z')-ord(i)
    if first == 0 or last == 0:
        pass
    elif first < last:
        ans+=first
        ans += 1
    else:
        ans+=last
        ans += 1

print(ans-1)

print(ord('N')-ord('A'))
print(1+ord('Z')-ord('N'))"""

#9 + 1 + 0 +
#print(9 + 1 + 4 + 1 + 9 + 1 + 12 + 1 +12+1+13)