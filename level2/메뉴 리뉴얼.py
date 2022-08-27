"""import collections
from itertools import combinations
def solution(orders, course):
    answer = []
    dic=collections.defaultdict(int)
    for i in orders:
        for j in range(2,len(i)+1):
            a=combinations(i,j)
            for k in a:
                dic["".join(sorted(k))]+=1
    maxx=max(dic.values())
    dd=[0]
    for i in range(maxx,1,-1):
        for j in dic.keys():
            if dic[j] == i and len(j)>dd[0]:
                answer.append(j)
        dd[0]=len(answer[-1])
    answer.sort()
    return answer

orders=["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]
course=[2,3,5]

#orders= ["XYZ", "XWY", "WXA"]
#course=[2,3,4]
print(solution(orders,course))"""



"""
import collections
from collections import Counter
from itertools import combinations
def solution(orders, course):
    answer = []
    for j in course:
        ans = []
        for i in orders:
            for k in combinations(i,j):
                ans.append(''.join(sorted(k)))
        sorted_= Counter(ans).most_common()
        #answer+=[i for i,j in sorte if j >1 and j == sorte[0][1]]
        answer += [menu for menu, cnt in sorted_ if cnt > 1 and cnt == sorted_[0][1]]

    return sorted(answer)


#orders=["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]
#course=[2,3,5]

orders= ["XYZ", "XWY", "WXA"]
course=[2,3,4]
print(solution(orders,course))


from itertools import combinations
from collections import Counter
def solution(orders, course):
    answer = []
    for k in course:
        candidates = []
        for menu_li in orders:
            for li in combinations(menu_li, k):
                res = ''.join(sorted(li))
                candidates.append(res)

        sorted_candidates = Counter(candidates).most_common()
        #print(sorted_candidates)
        answer += [menu for menu, cnt in sorted_candidates if cnt > 1 and cnt == sorted_candidates[0][1]]
    return sorted(answer)

orders= ["XYZ", "XWY", "WXA"]
course=[2,3,4]
"""





















from itertools import combinations
from collections import Counter
def solution(orders, course):
    answer=[]
    for i in course:
        ans=[]
        for j in orders:
            for k in combinations(j,i):
                ans.append("".join(sorted(k)))
    
        sort_=Counter(ans).most_common()
        answer+=[m for m,c in sort_ if c > 1 and c == sort_[0][1]]
    return sorted(answer)



orders=["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]
course=[2,3,5]

orders= ["XYZ", "XWY", "WXA"]
course=[2,3,4]
print(solution(orders,course))