def solution(s):
    answer=False
    s=s.lower()
    if s.count('p') == s.count('y'):
        answer = True
    return answer

from collections import Counter
def numPY(s):
    c = Counter(s.lower())
    return c['y'] == c['p']

s="pPoooyY"
print(solution(s))
print(numPY(s))