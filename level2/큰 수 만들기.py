"""
def solution(number, k):
    number=list(number)
    num=0
    while num < k:
        for i in range(len(number)-k):
            if number[i] == 9 or number[i+1] ==9:
                pass
            elif number[i] < number[i+1]:
                number.pop(i)
                num+=1
                break
        else:
            number.pop()
            num += 1
    return "".join(number)"""
def solution(number, k):
    answer = []
    for i in number:
        if not answer:
            answer.append(i)
            continue
        while answer[-1] < i and k > 0:
            answer.pop()
            k -= 1
            if not answer or k <= 0:
                break
        answer.append(i)
        if len(answer) == len(number) - k:
            break
    return ''.join(answer)


number="1924"
k=2
print(solution(number,k))

"""else:
number.pop()
num += 1"""