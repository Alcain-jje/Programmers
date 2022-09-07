import collections
from collections import deque

#정답 풀이
def solution(bridge_length, weight, truck_weights):
    stack=[0]*bridge_length
    ans=0
    while stack:
        stack.pop(0)
        ans+=1
        if truck_weights:
            if sum(stack)+truck_weights[0] <=weight:
                stack.append(truck_weights.pop(0))
            else:
                stack.append(0)
    return ans

# 시간초과
def solution(bridge_length, weight, truck_weights):
    stack=deque([0])*bridge_length
    truck_weights=deque(truck_weights)
    ans=0
    while stack:
        stack.popleft()
        ans+=1
        if truck_weights:
            if sum(stack)+truck_weights[0] <=weight:
                stack.append(truck_weights.popleft())
            else:
                stack.append(0)
    return ans

"""def solution(bridge_length, weight, truck_weights):
    queue=deque([0]*bridge_length)+deque(truck_weights)
    ans=0
    while len(queue)>1:
        summ=0
        for i in range(0,bridge_length):
            try:
                summ+=queue[i]
            except IndexError:
                pass
        if summ<=weight:
            queue.popleft()
            ans+=1
        else:
            queue.popleft()
            queue.appendleft(0)
            ans+=1
    return ans+1"""

# bridge_length=2
# weight=10
# truck_weights=[7,4,5,6]

bridge_length=5
weight=5
truck_weights=[2,2,2,2,1,1,1,1,1]
print(solution(bridge_length,weight,truck_weights))
#[0,0,7,4,5,6]
#[0,0,7,0,4,5,0,6]