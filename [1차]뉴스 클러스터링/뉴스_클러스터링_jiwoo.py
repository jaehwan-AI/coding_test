import re
from collections import defaultdict


def make_two(string):  # 2개씩 끊어서 단어 리스트 만들기
    words = []
    for idx in range(len(string)):
        if idx == len(string)-1:
            break
        else:
            w = string[idx] + string[idx+1]
            if not(re.search('[^a-z]', w)):
                words.append(w)
    return words


def solution(str1, str2):
    words1 = make_two(str1.lower())
    words2 = make_two(str2.lower())

    if len(words1) == 0 and len(words2) == 0:
        return 65536

    dic1 = defaultdict(int)
    dic2 = defaultdict(int)

    for w1 in words1:
        dic1[w1] += 1

    for w2 in words2:
        dic2[w2] += 1

    set1 = set(words1)
    set2 = set(words2)

    inter = set1.intersection(set2)
    union = set1.union(set2)

    all_union = 0
    all_inter = 0
    for inter_item in inter:
        if dic1[inter_item] > 1 or dic2[inter_item] > 1:
            inter_val = min(dic1[inter_item], dic2[inter_item])
            union_val = max(dic1[inter_item], dic2[inter_item])
            all_union += union_val
            all_inter += inter_val

        else:  # str1, str2에서 개수가 1인 경우
            all_union += 1
            all_inter += 1

    all_union = sum(dic1.values()) + sum(dic2.values()) - all_inter

    return int(all_inter/all_union*65536)
