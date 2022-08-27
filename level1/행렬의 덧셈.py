"""def solution(arr1, arr2):
    li=[]
    answer=[]
    for i in range(len(arr1)):
        for j in range(len(arr1[0])):
            ans= arr1[i][j] + arr2[i][j]
            li.append(ans)
        answer.append(li)
        li=[]
    return answer"""

def solution(arr1, arr2):
    for i in range(len(arr1)):
        for j in range(len(arr1[0])):
            arr1[i][j] += arr2[i][j]
    return arr1

#arr1=[[1,2],[2,3]]
#arr2=[[3,4],[5,6]]

arr1=[[1],[2]]
arr2=[[3],[4]]
print(solution(arr1,arr2))