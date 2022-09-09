import collections

def solution(n):
    num=bin(n).count('1')
    while True:
        n+=1
        if num == bin(n).count('1'):
            return n


def solution2(n):
    n_two=bin(n)[2:]
    dic=collections.defaultdict(int)
    for i in n_two:
        if i == '1':
            dic[i]+=1
    result=True

    while result:
        dic_2 = collections.defaultdict(int)
        n+=1
        n_result=bin(n)[2:]
        for i in n_result:
            if i == '1':
                dic_2[i]+=1
        if dic_2['1'] == dic['1']:
            return n





n=15
print(solution(n))