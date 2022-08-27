# 내 풀이
def solution(s,n):
    answer=""
    for i in s:
        if i.isupper():
            answer+= chr((ord(i)-ord('A')+n)%26+ord('A'))
        elif i.islower():
            answer+=chr((ord(i)-ord('a')+n)%26+ord('a'))
        else:
            answer+=i
    return answer


s="a B z"
n=4
print(solution(s,n))

# 내 풀이 2
def solution2(s, n):
    # 소문자 대문자 별로 나눠서 풀이
    answer = ''
    for i in s:
        if i == " ":
            answer+=i
        elif i.islower() and ord(i)+n >122:
            answer += chr(ord(i) -26 + n)
        elif i.isupper() and ord(i)+n > 90:
            answer += chr(ord(i) - 26 + n)
        else:
            answer+=chr(ord(i)+n)
    return answer

s="a B z"
n=4
print(solution2(s,n))

#  리스트로 변환한 풀이
def caesar(s, n):
    s = list(s)
    for i in range(len(s)):
        if s[i].isupper():
            s[i]=chr((ord(s[i])-ord('A')+ n)%26+ord('A'))
        elif s[i].islower():
            s[i]=chr((ord(s[i])-ord('a')+ n)%26+ord('a'))

    return "".join(s)

print(caesar(s,n))


# 특이한 풀이
import string

def caesar2(s, n):
    result = ""
    base = ""
    for c in s:
        if c in string.ascii_lowercase:
            base = string.ascii_lowercase
        elif c in string.ascii_uppercase:
            base = string.ascii_uppercase
        else:
            result += c
            continue
        a = base.index(c) + n
        result += base[a % len(base)]
    return result
s="a B z"
n=4
print(caesar2(s,n))



"""def solution(s, n):
    answer = ''
    for i in s:
        if i == " ":
            answer+=" "
        else:
            if i.isupper():
                answer += chr((ord(i) - ord('A') + n)%26+ord('A'))
            elif i.islower():
                answer += chr((ord(i) - ord('a') + n)%26+ord('a'))
    return answer

s="ab"
n=1
print(solution(s,n))"""