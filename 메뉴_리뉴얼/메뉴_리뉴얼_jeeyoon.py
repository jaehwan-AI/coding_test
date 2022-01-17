from itertools import combinations
from collections import defaultdict
def solution(orders, course):
    answer = []
    for n in course:
        dict = defaultdict(int)
        for s in orders:
            comb = combinations(s, n)
            for i in comb:
                i = tuple(sorted(i))
                dict[i] += 1
        for k, v in dict.items():
            if v == max(dict.values()) and v >= 2:
                answer.append(''.join(k))
    return sorted(answer)