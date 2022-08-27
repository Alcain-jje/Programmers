# 풀이 1
def solution(s):
    s=s.split(" ")
    answer=""
    for i in range(len(s)):
        for j in range(len(s[i])):
            if j % 2 == 0:
                answer += s[i][j].upper()
            else:
                answer += s[i][j].lower()
        answer+=" "

    return answer[0:-1]
s="try hello world"
print(solution(s))

# 풀이 2
def solution2(s):
    return " ".join(map(lambda x:"".join([a.lower() if i%2 else a.upper() for i,a in enumerate(x)]),s.split(" ")))

s="try hello world"
print(solution2(s))

# 풀이 3

def solution3(s):
    res=[]
    for i in s.split(" "):
        word = ""
        for j in range(len(i)):
            c=i[j].upper() if j%2 == 0 else i[j].lower()
            word+=c
        res.append(word)
    return " ".join(res)

s="try hello world"
print(solution3(s))
