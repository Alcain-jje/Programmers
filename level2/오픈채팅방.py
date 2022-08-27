def solution(record):
    dic={}
    answer = []
    for i in range(len(record)):
        a=record[i].split()
        answer.append((a[0],a[1]))
        if len(a) == 2:
            pass
        else:
            dic[a[1]] = a[2]
    ans=[]
    for i in range(len(answer)):
        if answer[i][0] == "Enter":
            ans.append(dic[answer[i][1]]+"님이 들어왔습니다.")
        elif answer[i][0] == "Leave":
            ans.append(dic[answer[i][1]] + "님이 나갔습니다.")
    return ans

record= ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
print(solution(record))

def solution(record):
    user_id = {EC.split()[1]:EC.split()[-1] for EC in record if EC.startswith('Enter') or EC.startswith('Change')}
    return [f'{user_id[E_L.split()[1]]}님이 들어왔습니다.' if E_L.startswith('Enter') else f'{user_id[E_L.split()[1]]}님이 나갔습니다.' for E_L in record if not E_L.startswith('Change')]

record= ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
print(solution(record))