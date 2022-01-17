# -*- coding: utf-8 -*-
from itertools import permutations
from collections import defaultdict
def solution(orders, course):
    answer = []
    can = []
    # 가능한 모든 알파벳 조합 저장하기
    for alpha in orders:
        li = []
        for j in range(2, len(alpha)+1):
            permu = permutations(alpha, j)
            li += [''.join(sorted(i)) for i in permu] # 알파벳 순서와 상관 없이 오름차순으로 저장
        can += list(set(li))
    # 각 알파벳 조합의 개수 세기
    dict = defaultdict(int)
    can = [''.join(i) for i in can]
    for i in can:
        dict[i] += 1
    dict = sorted(dict.items(), key=lambda x : [x[1], len(x[0])], reverse=True) # 개수와 길이 순으로 sort
    print(dict)
    check = dict[0][1] + 1
    idx = 0
    string = ''
    # 개수가 1이 아닌 경우 while 문 돌리기 (1인 경우 stop)
    while check != 1:
        if dict[idx][1] == check-1:
            check -= 1
            if check == 1:
                 break
            string = dict[idx][0]
            answer.append(string)
        elif dict[idx][1] == check:
            if len(string) == len(dict[idx][0]):
                answer.append(dict[idx][0])
        idx += 1
    print(sorted(answer))
    return sorted(answer)

solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2,3,5])