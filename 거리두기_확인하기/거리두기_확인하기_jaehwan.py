dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

di = [-1, -1, 1, 1]
dj = [-1, 1, -1, 1]

ddx = [-2, 2, 0, 0]
ddy = [0, 0, -2, 2]


def check(c, dic):
    for i in range(4):
        nx, ny = c[0]+dx[i], c[1]+dy[i]
        if nx >= 0 and nx <= 4 and ny >= 0 and ny <= 4:
            target = (nx, ny)
            if dic[target] == 'P':
                return 0
        
        ni, nj = c[0]+di[i], c[1]+dj[i]
        if ni >= 0 and ni <= 4 and nj >= 0 and nj <= 4:
            target = (ni, nj)
            target1 = (c[0], nj)
            target2 = (ni, c[1])
            if dic[target] == 'P':
                if dic[target1] == 'O' or dic[target2] == 'O':
                    return 0
        
        nnx, nny = c[0]+ddx[i], c[1]+ddy[i]
        if nnx >= 0 and nnx <= 4 and nny >= 0 and nny <= 4:
            target1 = (nx, ny)
            target2 = (nnx, nny)
            if dic[target2] == 'P':
                if dic[target1] == 'O' or dic[target1] == 'P':
                    return 0
    return 1


def solution(places):
    answer = []
    for place in places:
        dic = {}
        flag = "True"
        for i, p in enumerate(place):
            for j, v in enumerate(p):
                dic[(i, j)] = v
        for k, v in dic.items():
            if v == 'P':
                if check(k, dic) == 0:
                    flag = "False"
        if flag == "True":
            answer.append(1)
        else:
            answer.append(0)
    return answer
