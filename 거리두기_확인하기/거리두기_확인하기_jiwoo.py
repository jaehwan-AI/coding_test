from itertools import combinations


def distance(a, b, c, d):  # 거리 구하는 함수
    return abs(a-c)+abs(b-d), a-c, b-d


def solution(places):
    answer = []
    idx = 0
    for pl in places:
        idx += 1
        p_lst = []
        for row, row_val in enumerate(pl):
            for col, val in enumerate(row_val):
                if val == 'P':
                    p_lst.append((row, col))
        p_comb = combinations(p_lst, 2)  # P간의 모든 조합
        flag = False
        for (a, b), (c, d) in p_comb:
            dis, dis_x, dis_y = distance(a, b, c, d)  # P끼리의 거리
            if dis <= 1:
                flag = True
                break
            elif dis == 2:
                mx, my = max(a, c), max(b, d)
                # 아래 4개의 케이스는 거리가 2이며, 대각선상의 위치하는 경우
                if dis_x == -1 and dis_y == -1:
                    if not(pl[mx-1][my] == 'X' and pl[mx][my-1] == 'X'):
                        flag = True
                        break
                elif dis_x == -1 and dis_y == 1:
                    if not(pl[a][b-1] == 'X' and pl[a+1][b] == 'X'):
                        flag = True
                        break
                elif dis_x == 1 and dis_y == 1:
                    if not(pl[a-1][b] == 'X' and pl[a][b+1] == 'X'):
                        flag = True
                        break
                # 거리가 2이며, 일직선상에 위치하는 경우
                elif dis_x == 0:
                    if not(pl[mx][my-1] == 'X'):
                        flag = True
                        break
                elif dis_y == 0:
                    if not(pl[mx-1][my] == 'X'):
                        flag = True
                        break
        if flag == True:
            answer.append(0)
        else:
            answer.append(1)
    return answer
