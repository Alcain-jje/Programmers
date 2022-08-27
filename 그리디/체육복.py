# set 활용 solution

"""def solution(n, lost, reserve):
    lost_2=list(set(lost)-set(reserve))
    reserve_2=list(set(reserve)-set(lost))
    ans=[]
    for i in range(len(reserve_2)):
        if reserve_2[i]-1 in lost_2 and reserve_2[i]-1 not in ans:
            ans.append(reserve_2[i]-1)
        elif reserve_2[i]+1 in lost_2 and reserve_2[i]+1 not in ans:
            ans.append(reserve_2[i]+1)
        else:
            pass
    for j in ans:
        if j in lost_2:
            lost_2.remove(j)

    answer=n-len(lost_2)
    return answer

n=3
lost=[3]
reverse=[1]
print(solution(n,lost,reverse))
"""


"""
#2번 저번에 풀었던 풀이
def solution(n, lost, reserve):
    reserve=sorted(reserve)
    lost2 = []
    ans = []
    for k in range(0, len(lost)):
        if lost[k] in reserve:
            reserve.remove(lost[k])
        else:
            lost2.append(lost[k])
    for i in range(0, len(reserve)):
        if reserve[i] - 1 in lost2 and reserve[i] - 1 not in ans:
            ans.append(reserve[i] - 1)
        elif reserve[i] + 1 in lost2 and reserve[i] + 1 not in ans:
            ans.append(reserve[i] + 1)
        else:
            pass
    for j in ans:
        if j in lost2:
            lost2.remove(j)
    answer = n - len(lost2)
    return answer"""

#3번

def solution(n, lost, reserve):
    _reserve = [r for r in reserve if r not in lost]
    _lost = [l for l in lost if l not in reserve]

    for i in _reserve:
        f=i+1
        b=i-1
        if f in _lost:
            _lost.remove(f)
        elif b in _lost:
            _lost.remove(b)
    answer=n-len(_lost)

    return answer

n=3
lost=[3]
reverse=[1]
print(solution(n,lost,reverse))