from itertools import permutations
def solution(numbers):
    numbers=list(map(str,numbers))
    numbers.sort(key=lambda x:x*2,reverse=True)
    print(numbers)
numbers=[99,991]
print(solution(numbers))















"""def solution(num): 
    num = list(map(str, num)) 
    num.sort(key = lambda x : x*3, reverse = True) 
    return str(int(''.join(num)))"""