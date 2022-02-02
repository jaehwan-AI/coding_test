def lower_bound(array, target):
    lower = 0
    upper = len(array)
    while lower < upper:
        mid = (lower+upper)//2
        if array[mid] >= target:
            upper = mid
        else:
            lower = mid+1
    return lower


def solution(info, query):
    # 모든 경우의 수 dict 만들기
    dic = {}
    for i in ['cpp', 'java', 'python', '-']:
        for ii in ['backend', 'frontend', '-']:
            for iii in ['junior', 'senior', '-']:
                for iiii in ['chicken', 'pizza', '-']:
                    dic[(i, ii, iii, iiii)] = []

    for p in info:
        p = p.split()
        for i in [p[0], '-']:
            for ii in [p[1], '-']:
                for iii in [p[2], '-']:
                    for iiii in [p[3], '-']:
                        dic[(i, ii, iii, iiii)].append(int(p[4]))
    for key in dic:
        dic[key].sort()

    answer = []
    for qs in query:
        qs = qs.split()
        array = dic[(qs[0], qs[2], qs[4], qs[6])]
        answer.append(len(array) - lower_bound(array, int(qs[7])))
    return answer
