#nonlocal과 global의 차이점 https://www.daleseo.com/python-global-nonlocal/
#product 사용법 https://hinos.tistory.com/94


#global 키워드는 일반함수 내에서 전역 변수를 대상으로 사용
#nonlocal 키워드는 중첩함수 내에서 비지역 변수를 대상으로 사용

"""
#dfs 풀이
def solution(numbers, target):
    answer=0
    lenn=len(numbers)
    def dfs(idx,result):
        if idx == lenn:
            if result == target:
                nonlocal answer
                answer+=1
            return
        else:
            dfs(idx+1,result+numbers[idx])
            dfs(idx + 1, result - numbers[idx])
    dfs(0,0)
    return answer

numbers=[1, 1, 1, 1, 1]
target=3
print(solution(numbers,target))"""


"""
#product 중복순열을 통해 구하기 

from itertools import product
def solution(numbers, target):  # numbers : [4, 1, 2, 1], target : 4
    answer = 0
    num_list = []
    for n in numbers:  # [[4, -4], [1, -1], [2, -2], [1, -1]]
        li = [n, -n]
        num_list.append(li)
    comb = list(product(*num_list))  # [(4, 1, 2, 1), (4, 1, 2, -1), ..., (-4, -1, -2, -1)]

    for c in comb:
        if sum(c) ==target:
            answer+=1
    return answer

numbers=[4, 1, 2, 1]
target=4
print(solution(numbers,target))"""


"""# 분할정복풀이 (재귀)
def solution(numbers, target):
    if not numbers and target == 0 :
        return 1
    elif not numbers:
        return 0
    else:
        return solution(numbers[1:], target-numbers[0]) + solution(numbers[1:], target+numbers[0])

numbers = [4, 1, 2, 1]
target = 4
print(solution(numbers, target))"""

# BFS 풀이

from collections import deque
def solution(numbers, target):
    answer = 0
    queue = deque()
    n = len(numbers)
    queue.append([numbers[0],0])
    queue.append([-1*numbers[0],0])
    while queue:
        temp, idx = queue.popleft()
        idx += 1
        if idx < n:
            queue.append([temp+numbers[idx], idx])
            queue.append([temp-numbers[idx], idx])
        else:
            if temp == target:
                answer += 1
    return answer

numbers = [4, 1, 2, 1]
target = 4
print(solution(numbers, target))