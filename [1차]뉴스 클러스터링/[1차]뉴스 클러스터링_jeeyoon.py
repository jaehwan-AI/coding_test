def solution(str1, str2):
    can1 = [str1[i:i + 2].lower() for i in range(len(str1) - 1)]
    can2 = [str2[i:i + 2].lower() for i in range(len(str2) - 1)]
    for i in range(len(can1) - 1, -1, -1):
        if not can1[i].isalpha():
            can1.pop(i)
        if not can2[i].isalpha():
            can2.pop(i)
    count = 0
    total = len(can1) + len(can2)
    for s in can1:
        if s in can2:
            idx = can2.index(s)
            can2.pop(idx)
            count += 1
    try:
        answer = int(count / (total - count) * 65536)
        return answer
    except:
        return 65536
