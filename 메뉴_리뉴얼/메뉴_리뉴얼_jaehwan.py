from itertools import combinations


def solution(orders, course):
    answer = []
    for i in course:
        dic = {}
        for order in orders:
            comb = list(combinations(sorted(order), i))
            for c in comb:
                if c not in dic.keys():
                    dic[c] = 1
                else:
                    dic[c] += 1
        
        for k, v in dic.items():
            if max(dic.values()) == v and v >= 2:
                answer.append(''.join(k))
                
    answer.sort()
    return answer
