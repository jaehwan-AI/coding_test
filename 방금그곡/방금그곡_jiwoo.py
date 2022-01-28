def calcul_time(start, end):
    ss, sb, es, eb = map(int, [start[:2], start[3:], end[:2], end[3:]])
    return (es-ss)*60 + eb - sb

    # 암호화 m, melody
def coding(m):
    for a,b in zip(["A#", "C#", "D#", "F#", "G#"], ["T","U","I","O","P"]):
        m = m.replace(a,b)  
    return m
            
def create_mel(time, melody):
    if time < len(melody):
        return melody[:time]
    else:
        moc = time // len(melody)
        nam = time % len(melody)
        return moc*melody + melody[:nam]
    
    
def solution(m, musicinfos):
    # {name: [time, song]}
    # song_dic = {}
    song_dict = {}
    m = coding(m)
    for idx, info in enumerate(musicinfos):
        info = info.split(',')
        lst = []
        time = calcul_time(info[0], info[1])
        lst.append(time)
        lst.append(create_mel(time, coding(info[3])))
        song_dict[info[2]] = lst
        
    match_song = []
    for name, lst in song_dict.items():
        if m in lst[1]:
            match_song.append([name, lst[0]])


    if match_song:
        return sorted(match_song, reverse=True, key=lambda x : x[1])[0][0]

    else:
        return '(None)'