# 내 풀이
from collections import deque
def solution(brown, yellow):
    summ=brown+yellow
    li=deque([])
    for i in range(1,summ+1):
        if summ % i ==0:
            li.append(i)
    while True:
        if len(li) == 1:
            x=li.popleft()
            y=x
        else:
            x=li.pop()
            y=li.popleft()
        if (x-2)*(y-2) == yellow:
            return [x,y]
        else:
            pass

# 다른 풀이
def solution2(brown,yellow):
    w=(brown/2)+1
    h=1
    while w>=h:
        if (w-2)*(h-2) == yellow:
            return [int(w),int(h)]
        w-=1
        h+=1

# brown=24
# yellow=24

# brown=50
# yellow=22

print(solution2(brown,yellow))

