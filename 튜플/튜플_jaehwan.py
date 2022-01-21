def solution(s):
    answer, tmp, result = [], [], []
    t = ''
    for c in s[1:-1]:
        if c == "{":
            t = ''
            tmp = []
        if c.isdigit():
            t += c
        if c == ',':
            tmp.append(t)
            t = ''
        if c == '}':
            tmp.append(t)
            answer.append(tmp)
            tmp = []
    
    answer.sort(key=len)
    for a in answer:
        for i in range(len(a)):
            if a[i] not in result:
                result.append(a[i])

    return list(map(int, result))
