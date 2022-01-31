import numpy as np
from itertools import combinations

def solution(relation):
    c = len(relation[0])
    answer_lst = [[] for _ in range(c+1)]
    array = np.array(relation)
    
    # 속성 개수별로
    cols = list(range(c))
    for col_num in range(1, c+1):
        # 속성 조합
        comb = list(combinations(cols, col_num))
        for case in comb:
            # 최소성 체크
            flag = False
            for bc_all in answer_lst:
                for bc in bc_all:
                    if set(bc).intersection(set(case)) == set(bc):
                        flag = True
            if flag:
                continue

            # 해당 컬럼 stack
            for i, col in enumerate(case):
                if i==0: col_array = array[:, col]
                else:
                    col_array = np.column_stack((col_array, array[:, col]))
                    
            # 유일성 체크
            if len(set(map(tuple, col_array)))==len(col_array):
                answer_lst[col_num].append(case)
    answer = 0
    for i in answer_lst:
        answer += len(i)
    return answer
    