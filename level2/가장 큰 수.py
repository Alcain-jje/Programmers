"""def solution(num):
    num = list(map(str, num))
    num.sort(key = lambda x : x*3, reverse = True)
    return str(int(''.join(num)))


numbers=[6,10,2]
print(solution(numbers))"""

import functools
def comparator(a, b):
    t1 = a + b
    t2 = b + a
    return (int(t1) > int(t2)) - (int(t1) < int(t2))

def solution(numbers):
    n = [str(x) for x in numbers]
    n = sorted(n, key=functools.cmp_to_key(comparator), reverse=True)
    answer = str(int(''.join(n)))
    return answer


numbers=[3, 30, 34, 5, 9]
print(solution(numbers))


#9 5 34 3 30
# print(t1, t2)
# print((int(t1) > int(t2)) - (int(t1) < int(t2)))