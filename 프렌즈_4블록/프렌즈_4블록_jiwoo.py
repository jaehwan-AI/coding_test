import numpy as np
dx = [0, 1, 1]
dy = [1, 1, 0]


def check_box(x, y, character):
    # 시작점을 기준으로 이웃 3개 블럭이 같은 블럭인지 체크
    cnt = 0
    for i in range(3):
        nx, ny = x+dx[i], y+dy[i]
        if nx < 0 or nx > (m-1) or ny < 0 or ny > (n-1) or grid[nx][ny] != character:
            flag = False
            break
        if grid[nx][ny] == character:
            cnt += 1
    if cnt == 3:
        flag = True
    else:
        flag = False
    return flag


def solution(mm, nn, board):
    answer = 0
    global grid
    global m
    global n
    m = mm
    n = nn
    grid = [list(row) for row in board]
    visited = [[False for _ in range(n)] for _ in range(m)]
    iteration = 0

    while True:
        visited = [[False for _ in range(n)] for _ in range(m)]

        iteration += 1
        for rownum in range(m):
            for colnum in range(n):
                character = grid[rownum][colnum]
                if character != 0:
                    if check_box(rownum, colnum, character):
                        visited[rownum][colnum] = True
                        for i in range(3):
                            nx, ny = rownum+dx[i], colnum+dy[i]
                            visited[nx][ny] = True

        array = np.array(visited)
        cnt = int(sum(sum(array)))

        if cnt != 0:
            answer += cnt
        else:
            break  # 없앨 블럭이 없으면 break
        for row in range(m):
            for col in range(n):
                if visited[row][col]:
                    grid[row][col] = 0

        for col in range(n):
            for row in range(m-1, -1, -1):  # 아래 행부터 옮겨준다 안그러면 덮어씌워지는 경우생김
                # 자신보다 아래의 visited 개수
                if visited[row][col] != True:
                    cnt = sum(array[row+1:, col])
                    if cnt > 0:
                        grid[row+cnt][col] = grid[row][col]
                        grid[row][col] = 0

    return answer
