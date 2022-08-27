#내 풀이
"""import collections
def solution(N, stages):
    stages=sorted(stages)
    num=len(stages)
    dic=collections.defaultdict(int)
    stages_set=list(set(stages))
    number = 0
    for i in range(len(stages_set)):
        if stages_set[i] <= N:
            if i == 0:
                dic[stages_set[i]]=stages.count(stages_set[i])/num
            else:
                dic[stages_set[i]] = stages.count(stages_set[i]) / (num -  number)
            number += stages.count(stages_set[i])
        else:
            pass
    for i in range(1,N+1):
        if i not in dic:
            dic[i]+=0
    dic = sorted(dic.items(),key=lambda x: x[1],reverse=True)
    answer=[]
    for i,j in dic:
        answer.append(i)
    return answer

"""



# 다른 풀이 1
def solution1(N,stages):
    result={}
    num=len(stages)
    for i in range(1,N+1):
        if num > 0:
            count=stages.count(i)
            result[i]=count/num
            num-=count
        else:
            result[i]=0
    return sorted(result, key=lambda x:result[x], reverse=True)


# 다른 풀이 2
def solution2(N,stages):
    fail={}
    for i in range(1,N+1):
        try:
            fail_=len([a for a in stages if a == i])/len([a for a in stages if a>=i])
        except:
            fail_=0
        fail[i]=fail_
    return sorted(fail,key=lambda x:fail[x],reverse=True)


# 다른 풀이 3
def solution3(N,stages):
    answer=[]
    fail=[]
    info=[0]*(N+2)
    for stage in stages:
        info[stage]+=1
    for i in range(N):
        be=sum(info[(i+1):])
        yet=info[i+1]
        if be == 0:
            fail.append((i+1,0))
        else:
            fail.append((i+1,yet/be))
    for item in sorted(fail,key=lambda x:x[1],reverse=True):
        answer.append(int(item[0]))
    return answer


N=5
stages=[2, 1, 2, 6, 2, 4, 3, 3]

print(solution1(N,stages))