characters = 'abcdefghijklmnopqrstuvwxyz'

def solution(str1, str2):
    str1, str2 = str1.lower(), str2.lower()
    
    lst_str1 = [str1[x-1]+str1[x] for x in range(1,len(str1)) if str1[x-1] in characters and str1[x] in characters]
    lst_str2 = [str2[y-1]+str2[y] for y in range(1,len(str2)) if str2[y-1] in characters and str2[y] in characters]
    
    intersection = []
    for string2 in lst_str2:
        if string2 in lst_str1:
            lst_str1.remove(string2)
            intersection.append(string2)
    
    tmp_str1, union = lst_str1.copy(), lst_str1.copy()
    for s2 in lst_str2:
        union.append(s2) if s2 not in tmp_str1 else tmp_str1.remove(s2)
    
    if len(intersection) == 0:
        return 0
    elif len(union) == 0:
        return 65536
    else:
        return int(len(intersection)/len(union)*65536)
