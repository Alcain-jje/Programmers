"""def solution(progresses, speeds):
    answer=[]
    while progresses:
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
        cnt=0
        while progresses and progresses[0] >=100:
            progresses.pop(0)
            speeds.pop(0)
            cnt+=1
        if cnt > 0:
            answer.append(cnt)
    return answer"""


"""def solution(progresses, speeds):
    answer=[]
    while progresses:
        for i in range(len(progresses)):
            progresses[i]+=speeds[i]
        cnt=0
        while progresses and progresses[0] >=100:
            cnt+=1
            progresses.pop(0)
            speeds.pop(0)
        if cnt>0:
            answer.append(cnt)
    return answer"""


def solution(progresses, speeds):
    Q=[]
    for p, s in zip(progresses, speeds):
        if len(Q)==0 or Q[-1][0]< - ((p-100)//s):
            Q.append([-((p-100)//s),1])
        else:
            Q[-1][1]+=1
    return [q[1] for q in Q]


progresses=[95, 90, 99, 99, 80, 99]
speeds=[1, 1, 1, 1, 1, 1]
print(solution(progresses,speeds))

"""import math
def solution(progresses, speeds):
    dic={}
    lenn=len(progresses)
    for i in range(lenn):
        dic[i]=speeds[i]
        progresses[i]=100-progresses[i]
    for i in range(lenn):
        progresses[i]=math.ceil(progresses[i]/dic[i])
    progresses.append(0)
    answer = []
    ans=1
    for i in range(lenn):
        if i == lenn-1:
            answer.append(ans)
        elif progresses[i]-progresses[i+1]>=0:
            ans+=1
        else:
            answer.append(ans)
            ans=1
    #and i + 1 not in visited
    #and i+1 in visited
    return answer"""


#progresses=[93,30,35]
#speeds=[1,30,5]



"""
    answer = []
    start=0
    end=1
    ans=1

while True:
    if end > lenn - 1:
        break
    elif (progresses[start] >= progresses[end] or progresses[start] == progresses[-1]) and end == lenn - 1:
        ans += 1
        answer.append(ans)
        break
    elif progresses[start] >= progresses[end]:
        ans += 1
        end += 1
    else:
        start = end
        end = start + 1
        answer.append(ans)
        ans = 1
    print(start, end)
return answer"""