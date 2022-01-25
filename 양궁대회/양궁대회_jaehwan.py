def check_score(lst1, lst2):
    score1, score2 = 0, 0
    for i, (a, r) in enumerate(zip(lst1, lst2)):
        if a == r == 0:
            pass
        elif a >= r:
            score1 += (10-i)
        else:
            score2 += (10-i)
    return score1, score2


def solution(n, info):
    apeach, ryan, tmp = {}, {}, {}
    apeach = {(10-i):v for i, v in enumerate(info)}
    ryan = {(10-i):0 for i, v in enumerate([0 for j in range(11)])}

    cnt = n
    for i in range(11):
        current = 10-i
        for k, v in apeach.items():
            if k >= current:
                pass
            else:
                if (v+1) <= cnt:
                    ryan[k] = v+1
                    cnt -= (v+1)
                if cnt == 0:
                    break
        
        apeach_score, ryan_score = check_score(apeach.values(), ryan.values())
        
        if apeach_score < ryan_score:
            tmp[abs(apeach_score - ryan_score)] = list(ryan.values())
        
    if len(tmp) == 0:
        return [-1]
    else:
        m = max(tmp.keys())
        return tmp[m]
