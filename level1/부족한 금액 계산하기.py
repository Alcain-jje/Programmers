def solution(price, money, count):
    ans=0
    for i in range(1,count+1):
        ans+=(price*i)
    answer=ans-money
    if answer > 0:
        return answer
    else:
        return 0

price= 3
money= 20
count=4
result=10
print(solution(price,money,count))
