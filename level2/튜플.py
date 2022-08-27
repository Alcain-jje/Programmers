import collections
import operator
import re

"""
def solution(s):
    #s1=s.lstrip('{').rstrip('}').split('},{')
    #print(s1)
    s = s[:-2].replace('{', '').replace(',', ' ').split('}')
    for i, v in enumerate(s):
        s[i] = v.split()
    answer = []
    dic=collections.defaultdict(int)
    for i in s:
        for j in i:
            dic[j]+=1
    dic = sorted(dic.items(),key=lambda x:x[1],reverse=True)
    for i,j in dic:
        answer.append(int(i))
    return answer"""


"""def solution(s):
    answer = []

    s_list = s.replace("{", "").replace("}}", "").split("},")
    s_list.sort(key=len)

    for st in s_list:
        st_li = list(map(int, st.split(',')))
        for num in st_li:
            if num not in answer:
                answer.append(num)

    return answer"""

def solution(s):
    s = eval(s.replace("{", "[").replace("}", "]"))
    answer = list({num:0 for k in sorted(s, key=lambda x: len(x)) for num in k}.keys())
    return answer
    #s = collections.Counter(re.findall('\d+', s))
    #return list(map(int,[k for k,v in sorted(s.items(),key=lambda x:x[1],reverse=True)]))



def solution(s):
    new_s = [sss.replace('{','').replace('}','') for sss in s.split(',')]
    print(new_s)
    s=s.replace('{','').replace('}','')
    print(s)
    print(list(s))
    print(list(eval(s)))
    #print(new_s)
    #return [int(c[0]) for c in sorted(collections.Counter(new_s).items(), key = lambda x: x[1], reverse=True)]


#s="{{2},{2,1},{2,1,3},{2,1,3,4}}"
s="{{20,111},{111}}"
#s="{{123}}"
print(solution(s))