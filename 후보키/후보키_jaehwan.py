# 관계 데이터베이스에서 릴레이션(Relation)의 튜플(Tuple)을 유일하게 식별할 수 있는 속성(Attribute) 또는 속성의 집합 중,
# 다음 두 성질을 만족하는 것을 후보 키(Candidate Key)라고 한다.
# 유일성(uniqueness) : 릴레이션에 있는 모든 튜플에 대해 유일하게 식별되어야 한다.
# 최소성(minimality) : 유일성을 가진 키를 구성하는 속성(Attribute) 중 하나라도 제외하는 경우 유일성이 깨지는 것을 의미한다.
# 즉, 릴레이션의 모든 튜플을 유일하게 식별하는 데 꼭 필요한 속성들로만 구성되어야 한다.
# 후보키의 최대 개수를 구해라

relation = [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]

from itertools import combinations


def solution(relation):
    row = len(relation)
    col = len(relation[0])
    
    candidates = []
    for i in range(1, col+1):
        candidates.extend(combinations(range(col), i))

    unique = []
    for cand in candidates:
        tmp = [tuple(item[i] for i in cand) for item in relation]
        if len(set(tmp)) == row:
            unique.append(cand)
    
    mini = set(unique)
    for i in range(len(unique)):
        for j in range(i+1, len(unique)):
            if len(unique[i]) == len(set(unique[i]) & set(unique[j])):
                mini.discard(unique[j])

    return len(mini)

print(solution(relation))
