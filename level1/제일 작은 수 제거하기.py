"""def solution(arr):
    answer=[-1]
    if len(arr) > 1:
        arr.pop(arr.index(min(arr)))
        answer=arr
    return answer
"""

def solution(arr):
    answer=[-1]
    if len(arr)>1:
        arr.remove(min(arr))
        answer=arr
    return answer

arr=[4,3,2,1]
print(solution(arr))

