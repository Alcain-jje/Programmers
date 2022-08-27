"""def solution(answers):
    li_1=[1,2,3,4,5]
    li_2=[2,1,2,3,2,4,2,5]
    li_3=[3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ans=[0,0,0]
    answer=[]
    for i in range(len(answers)):
        if answers[i] - li_1[i%5] ==0:
            ans[0]+=1
        if answers[i] - li_2[i%8] ==0:
            ans[1] += 1
        if answers[i] - li_3[i % 10] == 0:
            ans[2] += 1
    for i in range(3):
        if max(ans) == ans[i]:
            answer.append(i+1)
        else:
            pass
    return answer

answers=[1,3,2,4,2]
print(solution(answers))"""

def solution(answers):
    li_1=[1,2,3,4,5]
    li_2=[2,1,2,3,2,4,2,5]
    li_3=[3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ans=[0,0,0]
    answer=[]
    for i in range(len(answers)):
        if answers[i] ==li_1[i%5]:
            ans[0]+=1
        if answers[i] == li_2[i%8]:
            ans[1] += 1
        if answers[i] == li_3[i % 10]:
            ans[2] += 1
    for i in range(3):
        if max(ans) == ans[i]:
            answer.append(i+1)

    return answer

answers=[1,3,2,4,2]
print(solution(answers))