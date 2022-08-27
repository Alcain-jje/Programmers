"""def solution(num):
    dic={1:'Odd',0:'Even'}
    answer = dic[num%2]
    return answer"""

# 비트연산자를 사용한 풀이 1은 00000001이기 때문에 1과 0으로만 반환된다.
def solution(num):
    return ["Even", "Odd"][num & 1]
num=4
print(solution(num))
