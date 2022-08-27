"""
# 1번 풀이
def solution(s):
    answer=False
    if s.isdigit():
        if len(s) == 4 or len(s)==6: answer = True
        else: answer=False
    else:
        answer=False
    return answer

s='a234'
print(solution(s))
"""

# 2번 풀이 (refactor)
def solution(s):
    answer=False
    if s.isdigit():
        if len(s) == 4 or len(s)==6: answer = True
    return answer

s='1234'
print(solution(s))

# 다른 클린 풀이
def solution(s):
    return s.isdigit() and len(s) in (4,6)