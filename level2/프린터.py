from collections import deque

"""def solution(priorities, location):
    li=deque([])
    for i,j in enumerate(priorities):
        li.append([i,j])
    ans=0
    while True:
        i=0
        maxx=max(li, key=lambda x: x[1])[1]
        if li[i][0] == location and li[i][1] == maxx:
            ans+=1
            break
        if li[i][1]<maxx:
            li.append(li.popleft())
        elif li[i][1]==maxx:
            li.popleft()
            ans+=1

    return ans"""

"""def solution(priorities, location):
    li=deque([])
    for i,j in enumerate(priorities):
        li.append([i,j])
    ans=0
    while True:
        i=0
        maxx=max(li, key=lambda x: x[1])[1]
        if li[i][1]<maxx:
            li.append(li.popleft())
        elif li[i][1]==maxx:
            ans += 1
            if li[i][0] == location:
                break
            else:
                li.popleft()
    return ans
"""
def solution(priorities, location):
    queue = [(i,p) for i,p in enumerate(priorities)]
    answer=0
    while True:
        cur=queue.pop(0)
        if any(cur[1] < q[1] for q in queue):
            queue.append(cur)
        else:
            answer+=1
            if cur[0]==location:
                return answer
priorities=[1, 1, 9, 1, 1, 1]
location=0
print(solution(priorities,location))


