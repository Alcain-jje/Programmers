import collections
from itertools import combinations

def solution(clothes):
    dic=collections.defaultdict(list)
    for i in range(len(clothes)):
        dic[clothes[i][1]].append(clothes[i][0])
    mult=1
    for i,j in dic.items():
        mult*=(1+len(j))
    return mult-1

#x3 + (a+b+c)x2 + (ab+bc+ca)x + (abc) -> (x+a)(x+b)(x+c) -> (1+a)(1+b)(1+c) - 1

#clothes=[["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
clothes=[["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]

print(solution(clothes))


