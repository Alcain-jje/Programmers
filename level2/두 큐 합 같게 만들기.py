# 시간을 줄이기 위해 sum은 한번 만 씀.
# 나머지는 append 할 때마다 더하기 빼기로 계산

from collections import deque
def solution(queue1, queue2):
    qu_1=deque(queue1)
    qu_2=deque(queue2)
    sum_1=sum(qu_1)
    sum_2=sum(qu_2)
    for i in range(len(queue1)*3):
        if sum_1 == sum_2:
            return i
        if sum_1>sum_2:
            num=qu_1.popleft()
            qu_2.append(num)
            sum_1-=num
            sum_2+=num
        else:
            num = qu_2.popleft()
            qu_1.append(num)
            sum_2 -= num
            sum_1 += num

    return -1

# queue1 = [3, 2, 7, 2]
# queue2 = [4, 6, 5, 1]
queue1 = [1,2,1,2]
queue2 = [1,10,1,2]
print(solution(queue1,queue2))


