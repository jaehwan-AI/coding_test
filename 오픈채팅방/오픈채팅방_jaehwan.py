def solution(record):
    answer = []
    users = {re.split(' ')[1]:re.split(' ')[2] for re in record if re.split(' ')[0] == "Enter" or re.split(' ')[0] == "Change"}
    for reco in record:
        tmp = reco.split(' ')
        if tmp[0] == "Enter":
            answer.append(f"{users[tmp[1]]}님이 들어왔습니다.")
        elif tmp[0] == "Leave":
            answer.append(f"{users[tmp[1]]}님이 나갔습니다.")
    return answer
