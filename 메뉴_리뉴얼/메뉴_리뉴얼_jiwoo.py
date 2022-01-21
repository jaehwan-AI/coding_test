from collections import defaultdict
from itertools import combinations


def solution(orders, course):

    cnt_dic = defaultdict(list)

    for i in range(len(orders)):
        for ii in range(i+1, len(orders)):  # 모든 요소끼리의 교집합을 본다
            inter = set(str(orders[i])).intersection(set(str(orders[ii])))

            if len(inter) > 1:
                k = list(inter)

                string = sorted(inter)
                string = ''.join(string)

                if i not in cnt_dic[string]:
                    cnt_dic[string].append(i)

                if ii not in cnt_dic[string]:
                    cnt_dic[string].append(ii)

                for c in range(2, len(inter)):  # 교집합이 2개 이상일때 또 다른 교집합이 생길 수 있으므로
                    comb = list(combinations(k, c))
                    for cc in comb:
                        string = sorted(cc)
                        string = ''.join(string)

                        if i not in cnt_dic[string]:
                            cnt_dic[string].append(i)

                        if ii not in cnt_dic[string]:
                            cnt_dic[string].append(ii)
    answer = []

    for c in course:
        cnt = []
        string = []
        for k, val in cnt_dic.items():
            if len(k) == c:
                cnt.append(len(val))
                string.append(k)
        if cnt:
            max_val = max(cnt)
            for i, val in enumerate(cnt):
                if max_val == val:
                    answer.append(string[i])

    answer.sort()
    return answer
