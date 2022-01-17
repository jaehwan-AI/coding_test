def solution(s):
    length = len(s)
    for i in range(len(s)):
        cnt, current, tmp = 1, s[:i+1], ''
        for j in range(i+1, len(s), i+1):
            if current == s[j:j+i+1]:
                cnt += 1
            else:
                if cnt == 1:
                    tmp += current
                else:
                    tmp += str(cnt)
                    tmp += current
                cnt, current = 1, s[j:j+i+1]
        if cnt == 1:
            tmp += current
        else:
            tmp += str(cnt)
            tmp += current
        length = min(length, len(tmp))
    return length
