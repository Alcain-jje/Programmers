# 1번 풀이
def solution(arr):
    answer=sum(arr)/len(arr)
    return answer

arr=[1,2,3,4]
print(solution(arr))

# 2번 풀이
import statistics

def solution2(arr):
    return statistics.mean(arr)
arr=[1,2,3,4]
print(solution2(arr))