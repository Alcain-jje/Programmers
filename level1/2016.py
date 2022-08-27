"""#내 풀이
def solution(a, b):
    date=['THU','FRI','SAT','SUN','MON','TUE','WED']
    months = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    num=0
    for i in range(a):
        b+=months[i]
    answer = date[b%7]
    return answer
a=1
b=31
print(solution(a,b))"""

# 다른 풀이
def solution(a, b):
    date=['THU','FRI','SAT','SUN','MON','TUE','WED']
    months = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return date[(sum(months[:a])+b)%7]

a=5
b=24
print(solution(a,b))

#1 금, 2 토, 3 일, 4 월 5 화 6 수, 7 목
#8 금, 9 토, 10 일, 11 월, 12 화, 13 수, 14 목
#15                                    21
#22                                    28
#29금,30토,31일,1 월,




#1,3,5,7,8,10,12

#2,4,6,9,11
