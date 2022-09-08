#print(int('437674', 3))
def solution(n, k):
    rev_base = ''
    while n > 0:
        n, mod = divmod(n, k)
        rev_base += str(mod)
    answer=rev_base[::-1]

    answer=answer.split("0")
    num=0
    error=0
    for i in answer:
        if i == "":
            pass
        else:
            i=int(i)
            if i > 1:
                for j in range(2,int(i**0.5)+1):
                    if i % j == 0:
                        error+=1
                        break
                if error == 0:
                    num+=1
    return num


def ss(n,k):
    rev_base = ''
    while n > 0:
        n, mod = divmod(n, k)
        rev_base += str(mod)
    answer=rev_base[::-1]
    return answer

# n=110011
# k=10

n=437674
k=3
#print(ss(n,k))
print(solution(n, k))

