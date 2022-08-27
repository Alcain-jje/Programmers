"""def solution(phone_number):
    answer=list(phone_number)
    for i in range(len(phone_number)-4):
        answer[i]='*'
    return "".join(answer)

p="01033334444"
p="027778888"
print(solution(p))"""

def solution(p):
    return '*'*(len(p)-4)+p[-4:]

p="01033334444"
#p="027778888"
print(solution(p))