def bfs(case):
    x = [1,-1,0,0,-1,1,-1,1,2,-2,0,0]
    y = [0,0,1,-1,-1,-1,1,1,0,0,2,-2]
    # 모든 자리 확인
    for i in range(5):
        for j in range(5):
            if case[i][j] == 'P': # 해당 자리에 사람이 있는 경우
                for k in range(len(x)): # 상하좌우, 대각선, 2칸 상하좌우 check
                    n_x, n_y = i + x[k], j + y[k]
                    if 0 <= n_x < 5 and 0 <= n_y < 5 and case[n_x][n_y] == 'P': # 좌석 안에 있으면서 사람이 있는 경우
                        if k // 4 == 0: # 상하좌우
                            return 0
                        elif k//4 == 1 and [case[n_x][j], case[i][n_y]] != ['X','X']: # 대각선
                            return 0
                        elif k//4 ==2 and case[i+(x[k]//2)][j+(y[k]//2)] != 'X': # 2칸 상하좌우
                            return 0
    return 1
    
def solution(places):
    answer = []
    for case in places:
        answer.append(bfs(case))
    return answer
