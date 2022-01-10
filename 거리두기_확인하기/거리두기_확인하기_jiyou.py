from collections import deque
def bfs(place, i, j, dist):
    visited = [[False]*5 for _ in range(5)]
    point_xs = [0,1,-1,0]
    point_ys = [-1,0,0,1]
    que = deque([(i,j,dist)])
    while que:
        dx, dy, dd = que.popleft()
        visited[dx][dy] = True
        for point_x, point_y in zip(point_xs, point_ys):
            x = dx + point_x
            y = dy + point_y
            d = dd + 1
            if x >= 0 and y >= 0 and x <5 and y <5 and visited[x][y] == False:
                visited[x][y] = True
                if place[x][y] == 'P':
                    if d <= 2:
                        return False
                elif place[x][y] == 'O':
                    if d<= 2:
                        que.append((x,y,d))
    return True


def solution(places):
    answer = []
    for place in places:
        tmp = []
        for i in range(len(place)):
            for j in range(len(place[i])):
                if place[i][j] == 'P':
                    result = bfs(place, i, j, 0)
                    tmp.append(result)
        if False in tmp:
            answer.append(0)
        else:
            answer.append(1)
    return answer
