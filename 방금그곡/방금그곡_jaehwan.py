def solution(m, musicinfos):
    lst = {}
    for musicinfo in musicinfos:
        tmp = musicinfo.split(',')
        H1, M1 = list(map(int, tmp[0].split(':')))
        H2, M2 = list(map(int, tmp[1].split(':')))
        t = abs(H2-H1) + abs(M2-M1)
        replay = t // len(tmp[3])
        
        if replay >= 2:
            play = tmp[3][:t] * replay
        else:
            play = tmp[3][:t]
        
        if m in play:
            lst[tmp[2]] = len(play)
    result = [k for k, v in lst.items() if v == max(lst.values())] 
    if len(result) == 0:
        return "(None)"
    else:
        return result[0]
