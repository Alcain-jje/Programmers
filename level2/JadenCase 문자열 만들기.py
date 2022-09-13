def solution(s):
    answer = ''
    stack=[]
    for i in range(len(s)):
        if i == 0 and not s[i].isdigit():
            answer+=s[i].upper()
        elif s[i] == " ":
            if stack:
                answer += " "
            else:
                stack.append(0)
                answer+=" "
        elif not s[i]== " " and stack:
            stack.pop()
            answer += s[i].upper()
        else:
            answer+=s[i].lower()

    return answer

def solution2(s):
    answer = s[0].upper()
    for i in range(1, len(s)):
        if s[i-1] == " " and s[i] != " ":
            answer += s[i].upper()
        else:
            answer += s[i].lower()
    return answer

s="a  aa  b  c"
print(solution(s))

