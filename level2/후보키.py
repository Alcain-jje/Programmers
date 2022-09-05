from itertools import combinations

def solution(relation):
    row = len(relation)
    col = len(relation[0])
    #가능한 속성의 모든 인덱스 조합
    combi = []
    for i in range(1, col+1):
        combi.extend(combinations(range(col), i))
    unique = []
    for i in combi:
        tmp = [tuple([item[key] for key in i]) for item in relation]
        if len(set(tmp)) == row:
            put =True
            for x in unique:
                if set(x).issubset(set(i)):
                    put=False
                    break
            if put:unique.append(i)
    return len(unique)

relation=[["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]
print(solution(relation))


# 0 1, 1 2, 2 3
# 0 2, 1 3, 2 4



        #print(j,i,i+2)
        #print(j,i,i+1)

"""c = combinations(relation, i)
for j in c:
    print(j)"""