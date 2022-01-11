def is_char(str):
    if 65 > ord(str) or 90 < ord(str) < 97 or 122 < ord(str):
        return False
    return True

def solution(str1, str2):
    answer = 0
    str1_dict = {}
    for i in range(len(str1)-1):
        if is_char(str1[i]) and is_char(str1[i+1]):
            tmp = (str1[i]+str1[i+1]).lower()
            if tmp in str1_dict:
                str1_dict[tmp] += 1
            else:
                str1_dict[tmp] = 1
    str2_dict = {}
    for i in range(len(str2)-1):
        if is_char(str2[i]) and is_char(str2[i+1]):
            tmp = (str2[i]+str2[i+1]).lower()
            if tmp in str2_dict:
                str2_dict[tmp] += 1
            else:
                str2_dict[tmp] = 1
    if len(str1_dict) == 0 and len(str2_dict) == 0:
        return 1 * 65536
    inter = 0
    union = 0
    tmp = []
    for s1 in str1_dict.items():
        for s2 in str2_dict.items():
            if s1[0] == s2[0]:
                inter += min(s1[1],s2[1])
                union += max(s1[1],s2[1])
                tmp.append(s1[0])
    for s1 in str1_dict.items():
        if s1[0] not in tmp:
            union += s1[1]
    for s2 in str2_dict.items():
        if s2[0] not in tmp:
            union += s2[1]
    return int(inter / union * 65536)
