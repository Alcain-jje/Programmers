# 내 풀이
def solution(arr):
    answer=[]
    dupli=False
    for i in range(len(arr)-1):
        if arr[i] == arr[i+1]:
            dupli= True
            if i == len(arr)-2:
                answer.append(arr[i])
            else:
                pass
        else:
            dupli=False
            answer.append(arr[i])
    if dupli == False:
        answer.append(arr[-1])
    return answer


#조건 설정 1. 연속 중복값일 때, 중복 True로 체크 후 넘김.
# 2. 연속 중복X면 중복 False로 체크 후 중복 2개중 맨 앞 숫자를 리스트에 넣음
# 3. 만약 1번일 때, i가 마지막 인덱스 -1 를 가리키고 있다면, 맨 앞 숫자를 리스트에 넣음
# 4. 반복문이 다 끝난후 마지막 숫자 2개가 중복이 아니라면, 맨 마지막 숫자를 리스트에 넣는다.


# 다른 사람 풀이 1
def solution2(s):
    a = []
    for i in s:
        if a[-1:] == [i]: continue
        a.append(i)
    return a

# 다른 사람 풀이 2

def solution3(s):
    return [s[i] for i in range(len(s)) if [s[i]] != s[i+1:i+2]]

#인덱스는 범위를 벗어나도 오류가 나지 않는다.

arr=[1,1,3,3,0,1,1]
print(solution3(arr))

