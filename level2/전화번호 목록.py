"""
#1번째 풀이
def solution(s):
    s.sort()
    for i in range(len(s)-1):
        if s[i]<s[i+1] and s[i+1][:len(s[i])] == s[i]:
            return False
    return True

phone_book=["12","123","1235","567","88"]
print(solution(phone_book))"""

"""#2번째 풀이
def solution(s):
    s.sort()
    for i in range(len(s)-1):
        if s[i+1].startswith(s[i]):
            return False
    return True

phone_book=["123","456","789"]
print(solution(phone_book))"""

# 3번째 풀이

def solution(s):
    dic={}
    for i in range(len(s)):
        dic[s[i]]=1
    for j in s:
        temp=""
        for nn in j:
            temp+=nn
            if temp in dic and temp!=j:
                return False
    return True

phone_book=["123","456","789"]
print(solution(phone_book))