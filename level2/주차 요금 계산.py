import collections
import math
# 내 풀이
def solution(fees, records):
    answer = []
    li=[]
    end=23 * 60 + 59
    dic=collections.defaultdict(list)
    for i in records:
        a=str(i).split(" ")
        for j in range(len(a)):
            if j == 2:
                time_ = str(a[0]).split(":")
                ans = int(time_[0]) * 60 + int(time_[1])
                if a[j] =='IN':
                    dic[a[1]].append(ans)
                    dic[a[1]].append('True')
                elif a[j] == 'OUT':
                    dic[a[1]].pop()
                    dic[a[1]][-1]=ans-dic[a[1]][-1]

    for j,i in dic.items():
        if 'True' in i:
            i.pop()
            i[-1]=end-i[-1]
            answer.append([j,sum(i)])
        else:
            answer.append([j,sum(i)])
    answer.sort(key=lambda x:x[0])
    for i in range(len(answer)):
        if answer[i][1] > fees[0]:
            li.append(fees[1] + math.ceil((answer[i][1]-fees[0])/fees[2])*fees[3])
        else:
            li.append(fees[1])
    return li


# 다른 풀이
def sol(fees, records):
    answer = []
    car = collections.defaultdict(list)
    for record in records:
        time, num, io = record.split()
        h, m = time.split(':')
        time = int(h) * 60 + int(m)
        car[num].append([time, io])
    for num in car:
        if car[num][-1][1] == 'IN':
            car[num].append([23 * 60 + 59, 'OUT'])
    car=dict(sorted(car.items()))
    print(car)
    for num in car:
        total = 0
        for i in range(0, len(car[num]), 2):
            total += car[num][i + 1][0] - car[num][i][0]
        if total <= fees[0]:
            answer.append(fees[1])
        else:
            answer.append(fees[1] + math.ceil((total - fees[0]) / fees[2]) * fees[3])
    return answer


#fees=[180, 5000, 10, 600]
#records=["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
fees=[120, 0, 60, 591]
records=["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"]
print(solution(fees,records))

