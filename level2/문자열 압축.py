"""def solution(s):
    ans=1e9
    if len(s) == 1:
        return 1
    for i in range(1,len(s)//2+1):
        cnt=1
        strr=""
        pre=s[0:i]
        for j in range(i,len(s)+i,i):
            print(j,j+i)
            if pre == s[j:j+i]:
                cnt+=1
            else:
                if cnt !=1:
                    strr+=str(cnt)+pre
                else:
                    strr+=pre
                cnt=1
                pre=s[j:j+i]
        ans=min(ans,len(strr))
    return ans

s = "ababcdcdababcdcd"
s="abcabcabcabcdededededede"
s="aabbaccc"
print(solution(s))

def solution(s):
    result = []
    if len(s) == 1:
        return 1
    for i in range(1, len(s)//2 + 1):
        b = ''
        cnt = 1
        tmp = s[:i]

        for j in range(i, len(s) + i, i):
            if tmp == s[j:i + j]:
                cnt += 1
            else:
                if cnt != 1:
                    b = b + str(cnt) + tmp
                else:
                    b = b + tmp
                tmp = s[j:j + i]
                cnt = 1

        result.append(len(b))

    return min(result)

s = "ababcdcdababcdcd"
#s="abcabcabcabcdededededede"
print(solution(s))

"""

# 풀이 2
def solution(s):
    if len(s)<3:
        return len(s)
    answer=len(s)
    max_cand= int(len(s)/2)
    for interval in range(1,max_cand+1):
        start = interval
        res=[]
        num=1
        pre_s=s[0:interval]
        while True:
            now_s=s[start:start+interval]
            if pre_s == now_s:
                num+=1
            else:
                res.append([num,pre_s])
                num=1
                pre_s=now_s
            if start>len(s)-1:
                break
            start+=interval

        len_cand=0
        for k in range(len(res)):
            if res[k][0] == 1:
                len_cand+=len(res[k][1])
            else:
                len_cand+=len(str(res[k][0]))
                len_cand+=len(res[k][1])
        answer=min(answer,len_cand)
    return answer

#s = "ababcdcdababcdcd"
s="abcabcabcabcdededededede"
print(solution(s))



