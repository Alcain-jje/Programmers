

from itertools import permutations
"""def solution(numbers):
    n=999999
    sosu = [False, False] + [True] * (n - 1)
    prime = []
    for i in range(n + 1):
        if sosu[i]:
            prime.append(str(i))
            for j in range(2 * i, n + 1, i):
                sosu[j] = False
    nn=list(numbers)
    ans=0
    for i in range(1,len(numbers)+1):
        for j in set(permutations(nn,i)):
            if "".join(j) in prime:
                ans+=1
    
    return ans"""



from itertools import permutations
def solution(numbers):
    nn = list(numbers)
    li=[]
    ans = 0
    for i in range(1,len(numbers)+1):
        for j in set(permutations(nn,i)):
            if int("".join(j)) == 1:
                pass
            elif int("".join(j)) == 0:
                pass
            else:
                li.append(int("".join(j)))
    li=list(set(li))
    for k in range(len(li)):
        non_s=False
        for l in range(2,li[k]):
            if li[k]%l==0:
                non_s=True
                break
        if non_s == False:
            ans+=1
    return ans


numbers="17"
print(solution(numbers))