def solution(n):
    answer = sorted(str(n),reverse=True)
    return int("".join(answer))
n=118372
print(solution(n))


def solution(n):
    return int("".join(sorted(str(n), reverse=True)))