import collections

def solution(participant, completion):
    answer=[]
    dic=collections.defaultdict(int)
    for i in participant:
        dic[i]+=1
    for j in completion:
        dic[j]-=1
    for i,j in dic.items():
        if j !=0:
            answer.append(i)
    return answer[0]

def solution2(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]


def solution3(participant, completion):
    participant.sort()
    completion.sort()
    answer=[]
    save=[]
    for i in participant:
        if i in completion and i not in save :
            save.append(i)
        else:
            answer.append(i)

    return answer[0]

# participant=["marina", "josipa", "nikola", "vinko", "filipa"]
# completion=["josipa", "filipa", "marina", "nikola"]
participant=["mislav", "stanko", "mislav", "ana"]
completion=	["stanko", "ana", "mislav"]
print(solution(participant,completion))




