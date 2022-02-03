def solution(record):
    # 유저 아이디별로 마지막 닉네임 저장 dict에 enter, change시 값변경
    # 유저아이디 : 닉네임
    dic = {}
    for r in record:
        r = r.split()
        if r[0] == 'Enter' or r[0] == 'Change':
            dic[r[1]] = r[2]

    answer = []
    # record에서 enter, leave만 출력
    for r in record:
        r = r.split()
        if r[0] == 'Enter':
            answer.append(f'{dic[r[1]]}님이 들어왔습니다.')
        elif r[0] == 'Leave':
            answer.append(f'{dic[r[1]]}님이 나갔습니다.')
    return answer
