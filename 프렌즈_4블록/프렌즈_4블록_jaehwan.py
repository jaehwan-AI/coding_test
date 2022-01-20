# m, n = 6, 6
# board = ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]

m, n = 4, 5
board = ["CCBDE", "AAADE", "AAABF", "CCBBF"]

def check_pop(m, n, board):
    pop_num = 0
    graph = [i[:] for i in board]
    for i in range(1, n):
        for j in range(1, m):
            if board[i][j] == -1:
                continue
            if board[i][j] == board[i-1][j] == board[i][j-1] == board[i-1][j-1]:
                graph[i][j], graph[i-1][j], graph[i][j-1], graph[i-1][j-1] = 1, 1, 1, 1

    for i, v in enumerate(graph):
        cnt = v.count(1)
        pop_num += cnt
        graph[i] = [-1]*cnt + [a for a in v if a != 1]

    return graph, pop_num


def solution(m, n, board):
    answer = 0
    board = list(map(list, zip(*board)))
    while 1:
        board, pop_cnt = check_pop(m, n, board)
        print(board)
        if pop_cnt == 0:
            return answer
        answer += pop_cnt

print(solution(m, n, board))
