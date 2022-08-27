# 첫 번째 풀이
def solution(num):
    answer = 0
    for i in range(500):
        if num == 1:
            break
        elif num % 2 == 0:
            num /= 2
        else:
            num=(num * 3) + 1
        answer += 1
    if num != 1:
        answer=-1
    return answer

num=626331
print(solution(num))

#두 번째 풀이

def solution2(num):
    answer=0
    while True:
        if num == 1:
            return answer
        if answer == 500:
            #break
            return -1
        answer += 1
        if num % 2 == 0:
            num = num / 2
        else:
            num=(num * 3) + 1

    #return -1

num=626331
print(solution2(num))

"""while True:
    if num == 1:
        break
    answer += 1
    if num % 2 == 0:
        num = num / 2
    else:
        (num * 3) + 1
return answer"""